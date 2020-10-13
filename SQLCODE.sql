--File for describe SQL code required on DB

--/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
--
-- ATTENTION: Don't run Django App/Server before executing this SQL code into MySql
--This code is in comments due to the steps in the installation instructions. It is still important for the database
--CREATE DATABASE IOGYM
--GO
--CREATE USER 'djangoDB'@'localhost' IDENTIFIED BY 'AfterByte';
--GO
--GRANT ALL PRIVILEGES ON IOGYM.* TO 'djangoDB'@'localhost';
--USE IOGYM


--//////////////////
--TRIGGERS
DELIMITER $$
CREATE TRIGGER DeleteClass BEFORE DELETE ON GYMCLASSES FOR EACH ROW
    BEGIN
        DELETE FROM MEMBERSHIPS_included_classes WHERE MEMBERSHIPS_included_classes.gymclasses_id = old.gymclass_id;
        DELETE FROM GROUPS WHERE GROUPS.gymclass_id = old.gymclass_id;
    END$$

CREATE TRIGGER DeleteTrainer BEFORE DELETE ON TRAINNERS FOR EACH ROW
    BEGIN
        UPDATE GROUPS SET trainer_id = NULL WHERE trainer_id = old.trainer_id;
        DELETE FROM TRAINNERS_ATTENDANCES WHERE TRAINNERS_ATTENDANCES.trainer_id = olFROMainer_id;
    END$$
CREATE TRIGGER DeleteClient BEFORE DELETE ON CLIENTS FOR EACH ROW
    BEGIN
        DELETE FROM MEMBERSHIPS WHERE MEMBERSHIPS.client_id = old.client_id;
        DELETE FROM CLIENT_ATTENDANCES WHERE CLIENT_ATTENDANCES.client_id = old.client_id;
    END$$


DELIMITER ;


--VIEWS

--for client Attendances
CREATE OR REPLACE VIEW clientAttendanceView AS SELECT row_number() OVER () AS id, CLIENTS.client_name AS client_name, CLIENTS.client_surname AS client_surname, CLIENTS.client_rfid AS client_rfid, CLIENT_ATTENDANCES.date AS date FROM CLIENTS, CLIENT_ATTENDANCES WHERE CLIENTS.client_id=CLIENT_ATTENDANCES.client_id order by date DESC;


--for Trainer Attendances
CREATE OR REPLACE VIEW trainerAttendanceView AS SELECT row_number() OVER () AS id, TRAINNERS.trainer_name AS trainer_name, TRAINNERS.trainer_surname AS trainer_surname, TRAINNERS.trainer_rfid AS trainer_rfid, TRAINNERS_ATTENDANCES.date AS register_date, TRAINNERS_ATTENDANCES.description AS description FROM TRAINNERS, TRAINNERS_ATTENDANCES WHERE TRAINNERS.trainer_id=TRAINNERS_ATTENDANCES.trainer_id ORDER BY register_date DESC;


--General stats
CREATE OR REPLACE VIEW GeneralStats AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(*) AS clients FROM CLIENTS) AS CLIENTS,
  (SELECT COUNT(*) AS trainers FROM TRAINNERS) AS TRAINNERS,
  (SELECT COUNT(*) AS groups FROM GROUPS) AS GROUPS,
  (SELECT COUNT(*) AS classes FROM GYMCLASSES) AS CLASSES,
  (SELECT COUNT(*) AS active_memberships FROM MEMBERSHIPS WHERE DATE(expiration_date) > CURDATE() OR DATE(expiration_date) = CURDATE()) AS A_MEMBERSHIPS,
  (SELECT COUNT(*) AS expirated_memberships FROM MEMBERSHIPS WHERE DATE(expiration_date) < CURDATE()) AS E_MEMBERSHIPS
);

--Client flow per week days last month
CREATE OR REPLACE VIEW CFLM AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS monday FROM clientAttendanceView WHERE WEEKDAY(date) = 0 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS LUNES,
  (SELECT COUNT(id) AS tuesday FROM clientAttendanceView WHERE WEEKDAY(date) = 1 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS MARTES,
  (SELECT COUNT(id) AS wednesday FROM clientAttendanceView WHERE WEEKDAY(date) = 2 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS MIERCOLES,
  (SELECT COUNT(id) AS thursday FROM clientAttendanceView WHERE WEEKDAY(date) = 3 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS JUEVES,
  (SELECT COUNT(id) AS friday FROM clientAttendanceView WHERE WEEKDAY(date) = 4 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS VIERNES,
  (SELECT COUNT(id) AS saturday FROM clientAttendanceView WHERE WEEKDAY(date) = 5 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS SABADO,
  (SELECT COUNT(id) AS sunday FROM clientAttendanceView WHERE WEEKDAY(date) = 6 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 MONTH) AND NOW()) AS DOMINGO
);

--Client Flow per week days last 3 months
CREATE OR REPLACE VIEW CFL3M AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS monday FROM clientAttendanceView WHERE WEEKDAY(date) = 0 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS LUNES,
  (SELECT COUNT(id) AS tuesday FROM clientAttendanceView WHERE WEEKDAY(date) = 1 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS MARTES,
  (SELECT COUNT(id) AS wednesday FROM clientAttendanceView WHERE WEEKDAY(date) = 2 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS MIERCOLES,
  (SELECT COUNT(id) AS thursday FROM clientAttendanceView WHERE WEEKDAY(date) = 3 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS JUEVES,
  (SELECT COUNT(id) AS friday FROM clientAttendanceView WHERE WEEKDAY(date) = 4 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS VIERNES,
  (SELECT COUNT(id) AS saturday FROM clientAttendanceView WHERE WEEKDAY(date) = 5 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS SABADO,
  (SELECT COUNT(id) AS sunday FROM clientAttendanceView WHERE WEEKDAY(date) = 6 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 3 MONTH) AND NOW()) AS DOMINGO
);

--Client Flow average per week days last 6 months
CREATE OR REPLACE VIEW CFL6M AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS monday FROM clientAttendanceView WHERE WEEKDAY(date) = 0 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS LUNES,
  (SELECT COUNT(id) AS tuesday FROM clientAttendanceView WHERE WEEKDAY(date) = 1 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS MARTES,
  (SELECT COUNT(id) AS wednesday FROM clientAttendanceView WHERE WEEKDAY(date) = 2 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS MIERCOLES,
  (SELECT COUNT(id) AS thursday FROM clientAttendanceView WHERE WEEKDAY(date) = 3 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS JUEVES,
  (SELECT COUNT(id) AS friday FROM clientAttendanceView WHERE WEEKDAY(date) = 4 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS VIERNES,
  (SELECT COUNT(id) AS saturday FROM clientAttendanceView WHERE WEEKDAY(date) = 5 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS SABADO,
  (SELECT COUNT(id) AS sunday FROM clientAttendanceView WHERE WEEKDAY(date) = 6 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 6 MONTH) AND NOW()) AS DOMINGO
);

--Client Flow average per week days last year
CREATE OR REPLACE VIEW CFLY AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS monday FROM clientAttendanceView WHERE WEEKDAY(date) = 0 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS LUNES,
  (SELECT COUNT(id) AS tuesday FROM clientAttendanceView WHERE WEEKDAY(date) = 1 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS MARTES,
  (SELECT COUNT(id) AS wednesday FROM clientAttendanceView WHERE WEEKDAY(date) = 2 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS MIERCOLES,
  (SELECT COUNT(id) AS thursday FROM clientAttendanceView WHERE WEEKDAY(date) = 3 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS JUEVES,
  (SELECT COUNT(id) AS friday FROM clientAttendanceView WHERE WEEKDAY(date) = 4 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS VIERNES,
  (SELECT COUNT(id) AS saturday FROM clientAttendanceView WHERE WEEKDAY(date) = 5 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS SABADO,
  (SELECT COUNT(id) AS sunday FROM clientAttendanceView WHERE WEEKDAY(date) = 6 AND date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW()) AS DOMINGO
);

--Historic client flow per week day
CREATE OR REPLACE VIEW HCLYD AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS monday FROM clientAttendanceView WHERE WEEKDAY(date) = 0 ) AS LUNES,
  (SELECT COUNT(id) AS tuesday FROM clientAttendanceView WHERE WEEKDAY(date) = 1 ) AS MARTES,
  (SELECT COUNT(id) AS wednesday FROM clientAttendanceView WHERE WEEKDAY(date) = 2 ) AS MIERCOLES,
  (SELECT COUNT(id) AS thursday FROM clientAttendanceView WHERE WEEKDAY(date) = 3 ) AS JUEVES,
  (SELECT COUNT(id) AS friday FROM clientAttendanceView WHERE WEEKDAY(date) = 4 ) AS VIERNES,
  (SELECT COUNT(id) AS saturday FROM clientAttendanceView WHERE WEEKDAY(date) = 5 ) AS SABADO,
  (SELECT COUNT(id) AS sunday FROM clientAttendanceView WHERE WEEKDAY(date) = 6 ) AS DOMINGO
);


--Client flow last year by months
CREATE OR REPLACE VIEW CFLYM AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS records, MONTHNAME(date) AS month_number, YEAR(date) AS year FROM clientAttendanceView WHERE date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW() GROUP BY MONTH(date) ORDER BY YEAR(date),MONTH(date)) AS RESULTS
);

--Historic client flow per month
CREATE OR REPLACE VIEW HCFM AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(id) AS records, MONTHNAME(date) AS month_number, YEAR(date) AS year FROM clientAttendanceView GROUP BY MONTH(date) ORDER BY YEAR(date), MONTH(date)) AS RESULTS
);

--New clients last year by months
CREATE OR REPLACE VIEW NCLYM AS SELECT * FROM (
  (SELECT COUNT(*) AS id FROM CLIENTS) AS ID,
  (SELECT COUNT(membership_id) AS records, MONTHNAME(register_date) AS month_number, YEAR(register_date) AS year FROM MEMBERSHIPS WHERE register_date BETWEEN SUBDATE(CURDATE(), INTERVAL 1 YEAR) AND NOW() GROUP BY MONTH(register_date),YEAR(register_date) ORDER BY YEAR(register_date)) AS RESULTS
);
