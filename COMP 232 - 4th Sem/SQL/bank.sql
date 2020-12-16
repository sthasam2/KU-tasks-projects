-- 1. Create a database of your name and create the tables as specified above.
CREATE DATABASE aashutosh;

CREATE DATABASE CREATE TABLE branch (
    branch_id VARCHAR(8),
    branch_add VARCHAR(128) NOT NULL,
    assets NUMERIC,
    PRIMARY KEY (branch_id)
);

CREATE TABLE staff(
    staff_id VARCHAR(8),
    branch_id VARCHAR(8),
    name VARCHAR(64) NOT NULL,
    address VARCHAR(128),
    PRIMARY KEY (staff_id),
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

CREATE TABLE customer (
    cust_id VARCHAR(8),
    cust_name VARCHAR(64) NOT NULL,
    cust_address VARCHAR(128) NOT NULL,
    cust_phone VARCHAR(64) NOT NULL,
    cust_dob DATE NOT NULL,
    PRIMARY KEY (cust_id)
);

CREATE TABLE loan (
    loan_number VARCHAR(8),
    branch_id VARCHAR(8),
    amount NUMERIC,
    PRIMARY KEY (loan_number),
    FOREIGN key (branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

CREATE TABLE borrower (
    cust_id VARCHAR(8),
    loan_number VARCHAR(8),
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (loan_number) REFERENCES loan(loan_number) ON DELETE CASCADE
);

CREATE TABLE account (
    account_number VARCHAR(8),
    branch_id VARCHAR(8),
    balance NUMERIC CHECK (balance > 0),
    PRIMARY KEY (account_number),
    FOREIGN key (branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

CREATE TABLE depositor (
    cust_id VARCHAR(8),
    account_number VARCHAR(8),
    FOREIGN key (cust_id) REFERENCES customer(cust_id) ON DELETE CASCADE,
    FOREIGN key (account_number) REFERENCES account(account_number) ON DELETE CASCADE
);

-- 2. Populate at least 10 data records in each tables. Your value should look realistic.
insert into
    branch (branch_id, branch_add, assets)
values
    (1, 'Gaushala', '8309965.78');

-- 3. Display all the data of each tables
SELECT
    *
FROM
    branch;

--  branch_id | branch_add  |   assets   
-- -----------+-------------+------------
--  1         | Gaushala    | 8309965.78
--  2         | Nayasadak   | 8801243.88
--  3         | Baneshowr   | 9328771.92
--  4         | Chabahil    | 6743650.29
--  5         | Maharajgunj | 6814413.52
--  6         | Putalisadak | 8811608.24
--  7         | Bouddha     | 9901030.71
--  8         | Banepa      | 7003840.84
--  9         | Thapathali  | 9337531.50
--  10        | Lainchour   | 5742353.15
-- (10 rows)
SELECT
    *
FROM
    staff;

--  staff_id | branch_id |        name         |   address    
-- ----------+-----------+---------------------+--------------
--  2        | 1         | Richmound Stratton  | Jorpati
--  3        | 8         | Griff Muino         | Mitrapark
--  4        | 8         | Scotti Lawday       | Sinamangal
--  5        | 7         | Lind Tebbutt        | Nayabazar
--  6        | 10        | Der Quinlan         | Chuchhepati
--  7        | 4         | Floria Leschelle    | Chuchhepati
--  8        | 8         | Dinnie Farrears     | Nayabazar
--  9        | 2         | Charles Portigall   | Putalisadak
--  10       | 5         | Petr Bosley         | Suryabinayak
--  11       | 4         | Jaquelin Oda        | Nayabazar
--  12       | 10        | Darci Lobb          | Sinamangal
--  13       | 6         | Langston Worrall    | Chabahil
--  14       | 6         | Tanhya Barkus       | Mitrapark
--  15       | 10        | Selina Olech        | Sukedhara
--  16       | 5         | Harrison Dumbare    | Chabahil
--  17       | 5         | Horacio Ubee        | Sukedhara
--  18       | 2         | Lion Koppelmann     | Chabahil
--  19       | 3         | Pauline Kenvin      | Jorpati
--  20       | 4         | Pen Husband         | Chabahil
--  21       | 2         | Trev Laban          | Mitrapark
--  22       | 8         | Corliss Underhill   | Chabahil
--  23       | 2         | Cece Wainer         | Nayabazar
--  24       | 8         | Fred McClary        | Suryabinayak
--  25       | 6         | Bord Marsy          | Putalisadak
--  26       | 2         | Poul McCanny        | Chabahil
--  27       | 3         | Maddi Padginton     | Mitrapark
--  28       | 3         | Yard Naris          | Suryabinayak
--  29       | 9         | Ferdinanda Fowler   | Chuchhepati
--  30       | 6         | Marita Waldie       | Chabahil
--  31       | 1         | Godfree Bohden      | Sinamangal
--  32       | 3         | Page Klaggeman      | Mitrapark
--  33       | 6         | Petronella Lambrick | Bagbazar
--  34       | 9         | Danit Geeraert      | Chabahil
--  35       | 4         | Theo Holah          | Jorpati
--  36       | 5         | Glynnis Macellar    | Sinamangal
--  37       | 4         | Abagael Bisp        | Sukedhara
--  38       | 3         | Ivan Suerz          | Sinamangal
--  39       | 8         | Min Simonato        | Jorpati
--  40       | 9         | Ernaline Porcas     | Chabahil
--  1        | 10        | Smith               | Suryabinayak
-- (40 rows)
SELECT
    *
from
    customer;

--  cust_id |      cust_name      | cust_address |  cust_phone  |  cust_dob  
-- ---------+---------------------+--------------+--------------+------------
--  1       | Maris Poulden       | Chabahil     | 193-979-1684 | 1999-07-08
--  2       | Cassius Glavis      | Bagbazar     | 183-137-1695 | 1985-05-30
--  3       | Ashleigh Vlasyev    | Chabahil     | 860-272-8515 | 2000-10-20
--  4       | Riccardo Scruby     | Sinamangal   | 951-937-9147 | 2002-01-22
--  5       | Osgood Fauguel      | Putalisadak  | 259-358-8140 | 2012-09-05
--  6       | Blinnie Arlow       | Mitrapark    | 512-816-7931 | 1996-03-23
--  7       | Kristofor Dossetter | Bagbazar     | 943-859-9441 | 2004-02-12
--  8       | Millisent Cundict   | Chabahil     | 657-692-7277 | 1987-08-15
--  9       | Samson Foley        | Mitrapark    | 564-562-1225 | 1998-12-31
--  10      | Lucais Rizzotto     | Nayabazar    | 657-782-0348 | 1997-02-18
--  11      | Leonie Weeks        | Chabahil     | 626-202-0720 | 1986-12-10
--  12      | Shaylynn Planque    | Mitrapark    | 912-931-2419 | 1998-09-30
--  13      | Nobe Bullant        | Nayabazar    | 314-590-7627 | 1991-03-08
--  14      | Burl Cornbill       | Suryabinayak | 587-279-6128 | 1987-03-31
--  15      | Eolande Godfree     | Chabahil     | 794-650-0419 | 1998-05-18
--  16      | Sheila McLinden     | Chuchhepati  | 187-273-7371 | 1992-12-17
--  17      | Brenna Hammerson    | Putalisadak  | 753-330-2751 | 2010-10-31
--  18      | Zerk Barosch        | Mitrapark    | 750-635-2373 | 1993-08-21
--  19      | Wendye Hurdidge     | Suryabinayak | 454-493-1959 | 1981-04-20
--  20      | Crista Beernaert    | Suryabinayak | 137-987-8846 | 1999-02-05
-- (20 rows)
SELECT
    *
FROM
    loan;

--  loan_number | branch_id |  amount   
-- -------------+-----------+-----------
--  1           | 5         | 100332.17
--  2           | 3         | 241126.46
--  3           | 9         |  68099.26
--  4           | 6         | 456621.28
--  5           | 3         | 129951.35
--  6           | 7         | 306229.25
--  7           | 8         | 351399.44
--  8           | 4         | 394821.72
--  9           | 10        | 169758.74
--  10          | 5         | 118672.43
-- (10 rows)
SELECT
    *
FROM
    borrower;

--  cust_id | loan_number 
-- ---------+-------------
--  7       | 1
--  11      | 2
--  6       | 3
--  12      | 4
--  4       | 5
--  8       | 6
--  17      | 7
--  20      | 8
--  1       | 9
--  18      | 10
-- (10 rows)
SELECT
    *
FROM
    account;

--  account_number | branch_id |  balance  
-- ----------------+-----------+-----------
--  650U           | 4         | 840044.44
--  733B           | 1         | 538920.88
--  539J           | 8         | 373259.43
--  012T           | 4         | 406465.40
--  094P           | 6         |  31384.70
--  389T           | 4         | 337307.32
--  576X           | 4         | 138661.70
--  125X           | 5         |  89529.99
--  567K           | 10        | 945810.04
--  325Z           | 6         | 234232.56
--  756U           | 9         | 643204.79
--  031R           | 3         | 236112.75
--  328B           | 5         | 635061.10
--  127Y           | 3         | 918927.07
--  248O           | 6         |  84487.73
--  114M           | 3         | 704202.27
--  345K           | 2         | 588398.74
--  969P           | 3         | 505094.89
--  348D           | 8         | 110911.79
--  111W           | 3         | 123608.42
--  005S           | 3         | 130508.42
-- (21 rows)
SELECT
    *
FROM
    depositor;

--  cust_id | account_number 
-- ---------+----------------
--  19      | 650U
--  16      | 733B
--  4       | 539J
--  7       | 012T
--  1       | 094P
--  10      | 389T
--  13      | 576X
--  20      | 567K
--  12      | 031R
--  5       | 345K
-- (10 rows)
-- 4. Add an attribute in the table staff as designation.
ALTER TABLE
    staff
ADD
    COLUMN designation VARCHAR(32);

ALTER TABLE
    -- 5. Display all the data of staff.
SELECT
    *
FROM
    staff;

--  staff_id | branch_id |        name         |   address    | designation 
-- ----------+-----------+---------------------+--------------+-------------
--  2        | 1         | Richmound Stratton  | Jorpati      | 
--  3        | 8         | Griff Muino         | Mitrapark    | 
--  4        | 8         | Scotti Lawday       | Sinamangal   | 
--  5        | 7         | Lind Tebbutt        | Nayabazar    | 
--  6        | 10        | Der Quinlan         | Chuchhepati  | 
--  7        | 4         | Floria Leschelle    | Chuchhepati  | 
--  8        | 8         | Dinnie Farrears     | Nayabazar    | 
--  9        | 2         | Charles Portigall   | Putalisadak  | 
--  10       | 5         | Petr Bosley         | Suryabinayak | 
--  11       | 4         | Jaquelin Oda        | Nayabazar    | 
--  12       | 10        | Darci Lobb          | Sinamangal   | 
--  13       | 6         | Langston Worrall    | Chabahil     | 
--  14       | 6         | Tanhya Barkus       | Mitrapark    | 
--  15       | 10        | Selina Olech        | Sukedhara    | 
--  16       | 5         | Harrison Dumbare    | Chabahil     | 
--  17       | 5         | Horacio Ubee        | Sukedhara    | 
--  18       | 2         | Lion Koppelmann     | Chabahil     | 
--  19       | 3         | Pauline Kenvin      | Jorpati      | 
--  20       | 4         | Pen Husband         | Chabahil     | 
--  21       | 2         | Trev Laban          | Mitrapark    | 
--  22       | 8         | Corliss Underhill   | Chabahil     | 
--  23       | 2         | Cece Wainer         | Nayabazar    | 
--  24       | 8         | Fred McClary        | Suryabinayak | 
--  25       | 6         | Bord Marsy          | Putalisadak  | 
--  26       | 2         | Poul McCanny        | Chabahil     | 
--  27       | 3         | Maddi Padginton     | Mitrapark    | 
--  28       | 3         | Yard Naris          | Suryabinayak | 
--  29       | 9         | Ferdinanda Fowler   | Chuchhepati  | 
--  30       | 6         | Marita Waldie       | Chabahil     | 
--  31       | 1         | Godfree Bohden      | Sinamangal   | 
--  32       | 3         | Page Klaggeman      | Mitrapark    | 
--  33       | 6         | Petronella Lambrick | Bagbazar     | 
--  34       | 9         | Danit Geeraert      | Chabahil     | 
--  35       | 4         | Theo Holah          | Jorpati      | 
--  36       | 5         | Glynnis Macellar    | Sinamangal   | 
--  37       | 4         | Abagael Bisp        | Sukedhara    | 
--  38       | 3         | Ivan Suerz          | Sinamangal   | 
--  39       | 8         | Min Simonato        | Jorpati      | 
--  40       | 9         | Ernaline Porcas     | Chabahil     | 
--  1        | 10        | Smith               | Suryabinayak | 
-- (40 rows)
-- 6. Update your table with at least 2 managers, 5 assistants, 2 officers, 1 guard.
-- 7. Display all the data of staff.
SELECT
    *
FROM
    staff;

--  staff_id | branch_id |        name         |   address    | designation 
-- ----------+-----------+---------------------+--------------+-------------
--  1        | 10        | Smith               | Suryabinayak | Guard
--  2        | 1         | Richmound Stratton  | Jorpati      | Assistant
--  3        | 8         | Griff Muino         | Mitrapark    | Assistant
--  4        | 8         | Scotti Lawday       | Sinamangal   | Assistant
--  5        | 7         | Lind Tebbutt        | Nayabazar    | Assistant
--  6        | 10        | Der Quinlan         | Chuchhepati  | Guard
--  7        | 4         | Floria Leschelle    | Chuchhepati  | Assistant
--  8        | 8         | Dinnie Farrears     | Nayabazar    | Assistant
--  9        | 2         | Charles Portigall   | Putalisadak  | Guard
--  10       | 5         | Petr Bosley         | Suryabinayak | Assistant
--  11       | 4         | Jaquelin Oda        | Nayabazar    | Assistant
--  12       | 10        | Darci Lobb          | Sinamangal   | Assistant
--  13       | 6         | Langston Worrall    | Chabahil     | Assistant
--  14       | 6         | Tanhya Barkus       | Mitrapark    | Assistant
--  15       | 10        | Selina Olech        | Sukedhara    | Assistant
--  16       | 5         | Harrison Dumbare    | Chabahil     | Assistant
--  17       | 5         | Horacio Ubee        | Sukedhara    | Assistant
--  18       | 2         | Lion Koppelmann     | Chabahil     | Officer
--  19       | 3         | Pauline Kenvin      | Jorpati      | Manager
--  20       | 4         | Pen Husband         | Chabahil     | Assistant
--  21       | 2         | Trev Laban          | Mitrapark    | Guard
--  22       | 8         | Corliss Underhill   | Chabahil     | Assistant
--  23       | 2         | Cece Wainer         | Nayabazar    | Assistant
--  24       | 8         | Fred McClary        | Suryabinayak | Assistant
--  25       | 6         | Bord Marsy          | Putalisadak  | Assistant
--  26       | 2         | Poul McCanny        | Chabahil     | Guard
--  27       | 3         | Maddi Padginton     | Mitrapark    | Assistant
--  28       | 3         | Yard Naris          | Suryabinayak | Assistant
--  29       | 9         | Ferdinanda Fowler   | Chuchhepati  | Guard
--  30       | 6         | Marita Waldie       | Chabahil     | Assistant
--  31       | 1         | Godfree Bohden      | Sinamangal   | Assistant
--  32       | 3         | Page Klaggeman      | Mitrapark    | Assistant
--  33       | 6         | Petronella Lambrick | Bagbazar     | Assistant
--  34       | 9         | Danit Geeraert      | Chabahil     | Assistant
--  35       | 4         | Theo Holah          | Jorpati      | Assistant
--  36       | 5         | Glynnis Macellar    | Sinamangal   | Assistant
--  37       | 4         | Abagael Bisp        | Sukedhara    | Assistant
--  38       | 3         | Ivan Suerz          | Sinamangal   | Officer
--  39       | 8         | Min Simonato        | Jorpati      | Manager
--  40       | 9         | Ernaline Porcas     | Chabahil     | Assistant
-- (40 rows)
-- 8. Smith is no longer the staff in the bank. Update the table/s accordingly.
DELETE FROM
    staff
WHERE
    name = 'Smith';

DELETE 1 -- 9. Display all the data of staff and look whether smith is there or not.
SELECT
    *
FROM
    staff;

--  staff_id | branch_id |        name         |   address    | designation 
-- ----------+-----------+---------------------+--------------+-------------
--  2        | 1         | Richmound Stratton  | Jorpati      | Assistant
--  3        | 8         | Griff Muino         | Mitrapark    | Assistant
--  4        | 8         | Scotti Lawday       | Sinamangal   | Assistant
--  5        | 7         | Lind Tebbutt        | Nayabazar    | Assistant
--  6        | 10        | Der Quinlan         | Chuchhepati  | Guard
--  7        | 4         | Floria Leschelle    | Chuchhepati  | Assistant
--  8        | 8         | Dinnie Farrears     | Nayabazar    | Assistant
--  9        | 2         | Charles Portigall   | Putalisadak  | Guard
--  10       | 5         | Petr Bosley         | Suryabinayak | Assistant
--  11       | 4         | Jaquelin Oda        | Nayabazar    | Assistant
--  12       | 10        | Darci Lobb          | Sinamangal   | Assistant
--  13       | 6         | Langston Worrall    | Chabahil     | Assistant
--  14       | 6         | Tanhya Barkus       | Mitrapark    | Assistant
--  15       | 10        | Selina Olech        | Sukedhara    | Assistant
--  16       | 5         | Harrison Dumbare    | Chabahil     | Assistant
--  17       | 5         | Horacio Ubee        | Sukedhara    | Assistant
--  18       | 2         | Lion Koppelmann     | Chabahil     | Officer
--  19       | 3         | Pauline Kenvin      | Jorpati      | Manager
--  20       | 4         | Pen Husband         | Chabahil     | Assistant
--  21       | 2         | Trev Laban          | Mitrapark    | Guard
--  22       | 8         | Corliss Underhill   | Chabahil     | Assistant
--  23       | 2         | Cece Wainer         | Nayabazar    | Assistant
--  24       | 8         | Fred McClary        | Suryabinayak | Assistant
--  25       | 6         | Bord Marsy          | Putalisadak  | Assistant
--  26       | 2         | Poul McCanny        | Chabahil     | Guard
--  27       | 3         | Maddi Padginton     | Mitrapark    | Assistant
--  28       | 3         | Yard Naris          | Suryabinayak | Assistant
--  29       | 9         | Ferdinanda Fowler   | Chuchhepati  | Guard
--  30       | 6         | Marita Waldie       | Chabahil     | Assistant
--  31       | 1         | Godfree Bohden      | Sinamangal   | Assistant
--  32       | 3         | Page Klaggeman      | Mitrapark    | Assistant
--  33       | 6         | Petronella Lambrick | Bagbazar     | Assistant
--  34       | 9         | Danit Geeraert      | Chabahil     | Assistant
--  35       | 4         | Theo Holah          | Jorpati      | Assistant
--  36       | 5         | Glynnis Macellar    | Sinamangal   | Assistant
--  37       | 4         | Abagael Bisp        | Sukedhara    | Assistant
--  38       | 3         | Ivan Suerz          | Sinamangal   | Officer
--  39       | 8         | Min Simonato        | Jorpati      | Manager
--  40       | 9         | Ernaline Porcas     | Chabahil     | Assistant
-- (39 rows)
-- 10. Find the account number who has the maximum balance.
SELECT
    *
FROM
    account
WHERE
    balance = (
        SELECT
            max(balance)
        FROM
            account
    );

--  account_number | branch_id |  balance  
-- ----------------+-----------+-----------
--  567K           | 10        | 945810.04
-- (1 row)
-- 11. Can you tell how much balance will remain after I withdraw 5000 from my account number ‘005S’.
UPDATE
    account
SET
    balance = balance - 5000
WHERE
    account_number = '005S';

UPDATE
    1
SELECT
    *
FROM
    account
WHERE
    account_number = '005S';

--  account_number | branch_id |  balance  
-- ----------------+-----------+-----------
--  005S           | 3         | 125508.42
-- (1 row)
-- 12. Find the youngest customer in the bank.
SELECT
    *,
    AGE(cust_dob)
FROM
    customer
WHERE
    AGE(cust_dob) = (
        SELECT
            MIN(AGE(cust_dob))
        FROM
            customer
    );

--  cust_id|  cust_name    | cust_address |  cust_phone  |  cust_dob  |    age       
-- ---------+----------------+--------------+--------------+------------+-----------
--  5      |Osgood Fauguel | Putalisadak  | 259-358-8140 | 2012-09-05 | 8 years 12days
-- (1 row)
-- 13. List the ID of the branches which have issued the loan amount greater than 10000.
-- 14. Can you list the number of customers from address “Nayasadak”.
SELECT
    COUNT(*)
FROM
    customer
WHERE
    cust_add = 'Nayasadak';

--  count 
-- -------
--      0
-- (1 row)
-- 15. Drop your database name.
DROP DATABASE aashutosh;

DROP DATABASE