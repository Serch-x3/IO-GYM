--File for describe SQL code required on DB


--VIEWS

--for client Attendances
create view clientesView as select CLIENTS.client_name as id, CLIENT_ATTENDANCES.date as date from CLIENTS, CLIENT_ATTENDANCES where CLIENTS.client_id=CLIENT_ATTENDANCES.client_id;
