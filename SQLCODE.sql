--File for describe SQL code required on DB


--VIEWS

--for client Attendances
create view clientesView as select CLIENTS.client_name as id, CLIENT_ATTENDANCES.date as date from CLIENTS, CLIENT_ATTENDANCES where CLIENTS.client_id=CLIENT_ATTENDANCES.client_id;

  --for Trainer Attendances
  create view trainerAttendanceView as select TRAINNERS.trainer_name as id, TRAINNERS.trainer_surname as trainer_surname, TRAINNERS.trainer_phone as trainer_phone, TRAINNERS_ATTENDANCES.date as register_date, TRAINNERS_ATTENDANCES.description as description from TRAINNERS, TRAINNERS_ATTENDANCES where TRAINNERS.trainer_id=TRAINNERS_ATTENDANCES.trainer_id;
