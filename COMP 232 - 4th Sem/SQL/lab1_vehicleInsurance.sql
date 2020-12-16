SHOW databases;

CREATE DATABASE sambeg_vehicleinsurance;

DROP DATABASE sambeg_vehicleinsurance;

CREATE DATABASE sambeg_vehicleinsurance;

SHOW databases;

USE sambeg_vehicleinsurance;

CREATE TABLE sambeg_PERSON(
  driver_id char(90),
  name varchar(20),
  address varchar(90),
  PRIMARY KEY (driver_id)
);

DROP TABLE sambeg_PERSON;

CREATE TABLE sambeg_PERSON(
  driver_id char(90),
  name varchar(20),
  address varchar(90),
  PRIMARY KEY (driver_id)
);

DESC sambeg_PERSON;

RENAME TABLE sambeg_PERSON TO PERSON;

CREATE TABLE CAR(
  reg_no CHAR(90),
  model VARCHAR(50),
  year INT,
  PRIMARY KEY(reg_no)
);

CREATE TABLE ACCIDENT(report_no INT, date DATE, location VARCHAR(90));

ALTER TABLE
  ACCIDENT
ADD
  PRIMARY KEY(report_no);

DESC ACCIDENT;

CREATE TABLE OWNS(
  driver_id char(90),
  reg_no CHAR(90),
  FOREIGN KEY (driver_id) REFERENCES PERSON((driver_id)),
  FOREIGN KEY(reg_no) REFERENCES CAR(reg_no)
);

CREATE TABLE PARTICIPATED(
  driver_id char(90),
  reg_no CHAR(90),
  report_no INT,
  damage_amount INT,
  FOREIGN KEY (driver_id) REFERENCES PERSON((driver_id)),
  FOREIGN KEY(reg_no) REFERENCES CAR(reg_no),
  FOREIGN KEY(report_no) REFERENCES ACCIDENT(report_no),
);

INSERT INTO
  PERSON(driver_id, name, address)
VALUES
  ('100a', 'Sambeg', 'Lalitpur'),
  ('100b', 'Yogesh', 'Mahendranagar'),
  ('100c', 'Sameer', 'Kathmandu'),
  ('100d', 'Aman', 'Janakpur'),
  ('100e', 'Sharawon', 'Bhaktapur');

INSERT INTO
  CAR(reg_no, model, year)
VALUES
  ('1213e321a', 'Renault', '2019'),
  ('1213e321b', 'Mercedes', '2015'),
  ('1213e321c', 'Honda', '2017'),
  ('1213e321d', 'Hummel', '2015'),
  ('1213e321e', 'MG Hector', '2009');

INSERT INTO
  OWNS(driver_id, reg_no)
VALUES
  ('100a', '1213e321a'),
  ('100b', '1213e321b'),
  ('100c', '1213e321c'),
  ('100d', '1213e321d'),
  ('100e', '1213e321e');

INSERT INTO
  ACCIDENT(report_no, date, location)
VALUES
  ('1', '2019-10-1', 'Lalitpur'),
  ('2', '2019-1-13', 'Mahendranagar'),
  ('3', '2019-11-16', 'Kathmandu'),
  ('4', '2019-12-17', 'Janakpur'),
  ('5', '2019-1-11', 'Bhaktapur');

INSERT INTO
  PARTICIPATED(driver_id, reg_no, report_no, damage_amount)
VALUES
  ('100a', '1213e321a', '1', 1323),
  ('100b', '1213e321b', '2', 135),
  ('100c', '1213e321c', '3', 13123),
  ('100d', '1213e321d', '4', 1654),
  ('100e', '1213e321e', '5', 1344);

CREATE TABLE PEOPLE AS
SELECT
  *
FROM
  PERSON;

CREATE TABLE DUP_PEOPLE AS
SELECT
  name,
  address
FROM
  PERSON;

CREATE TABLE duplicate_person AS
SELECT
  *
FROM
  PERSON
WHERE
  driver_id = '102';

SELECT
  *
FROM
  duplicate_person;

RENAME TABLE PEOPLE TO NEW_PEOPLE;