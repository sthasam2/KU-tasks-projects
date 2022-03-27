CREATE DATABASE assignment;

USE assignment;

CREATE TABLE suppliers(
	sid int,
	sname varchar(255),
	address varchar(1000),
	PRIMARY KEY (sid)
);

/*
 describe suppliers;
 +---------+---------------+------+-----+---------+-------+
 | Field   | Type          | Null | Key | Default | Extra |
 +---------+---------------+------+-----+---------+-------+
 | sid     | int           | NO   | PRI | NULL    |       |
 | sname   | varchar(255)  | YES  |     | NULL    |       |
 | address | varchar(1000) | YES  |     | NULL    |       |
 +---------+---------------+------+-----+---------+-------+
 */
CREATE TABLE parts(
	pid int,
	pname varchar(255),
	color varchar(1000),
	PRIMARY KEY (pid)
);

/*
 describe parts;
 +-------+--------------+------+-----+---------+-------+
 | Field | Type         | Null | Key | Default | Extra |
 +-------+--------------+------+-----+---------+-------+
 | pid   | int          | NO   | PRI | NULL    |       |
 | pname | varchar(500) | YES  |     | NULL    |       |
 | color | varchar(50)  | YES  |     | NULL    |       |
 +-------+--------------+------+-----+---------+-------+
 */
CREATE TABLE catalog(
	sid int,
	pid int,
	FOREIGN KEY (sid) REFERENCES suppliers(sid),
	FOREIGN KEY (pid) REFERENCES parts(pid),
	cost float(2)
);

/*
 describe catalog;
 +-------+-------+------+-----+---------+-------+
 | Field | Type  | Null | Key | Default | Extra |
 +-------+-------+------+-----+---------+-------+
 | sid   | int   | YES  | MUL | NULL    |       |
 | pid   | int   | YES  | MUL | NULL    |       |
 | cost  | float | YES  |     | NULL    |       |
 +-------+-------+------+-----+---------+-------+
 */
INSERT INTO
	suppliers
VALUES
(1, "Modi parts and distributions", "New Delhi"),
(2, "Computex Hardware", "221 Packer Street"),
(3, "Yosemite Sham", "Kathmandu"),
(4, "Linus Media Suppliers", "Montreal"),
(5, "Marques Camera and Equipment", "New York"),
(6, "Mauville Mechanical Solutions", "Hoenn");

/*
 select * from suppliers;
 +-----+-------------------------------+-------------------+
 | sid | sname                         | address           |
 +-----+-------------------------------+-------------------+
 |   1 | Modi parts and distributions  | New Delhi         |
 |   2 | Computex Hardware             | 221 Packer Street |
 |   3 | Yosemite Sham                 | Kathmandu         |
 |   4 | Linus Media Suppliers         | Montreal          |
 |   5 | Marques Camera and Equipment  | New York          |
 |   6 | Mauville Mechanical Solutions | Hoenn             |
 +-----+-------------------------------+-------------------+
 */
INSERT INTO
	parts
VALUES
	(5, "Dummy Part", "red"),
	(6, "Dummy Part", "green");

/*
 select * from parts;
 +-----+------------+-------+
 | pid | pname      | color |
 +-----+------------+-------+
 |   5 | Dummy Part | red   |
 |   6 | Dummy Part | green |
 +-----+------------+-------+
 */
INSERT INTO
	catalog
VALUES
	(1, 5, 200.1),
(2, 5, 200.4),
(2, 6, 523.12),
(3, 5, 230.1),
(4, 5, 199.1),
(5, 5, 210.1),
(5, 6, 501.4),
(6, 6, 411.4);

/*
 SHOW * FROM catalog;
 +------+------+--------+
 | sid  | pid  | cost   |
 +------+------+--------+
 |    1 |    5 |  200.1 |
 |    2 |    5 |  200.4 |
 |    2 |    6 | 523.12 |
 |    3 |    5 |  230.1 |
 |    4 |    5 |  199.1 |
 |    5 |    5 |  210.1 |
 |    5 |    6 |  501.4 |
 |    6 |    6 |  411.4 |
 +------+------+--------+
 */
---QUESTIONS
---1
SELECT
	s.sname
FROM
	suppliers s
	INNER JOIN parts p
	INNER JOIN catalog c ON (
		p.pid = c.pid
		AND s.sid = c.sid
	)
WHERE
	p.color = "red";

/*
 SELECT * FROM suppliers s INNER JOIN parts p INNER JOIN catalog c ON (p.pid = c.pid AND s.sid = c.sid) WHERE p.color="red";
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+-------+
 | sid | sname                        | address           | pid | pname      | color | sid  | pid  | cost  |
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+-------+
 |   1 | Modi parts and distributions | New Delhi         |   5 | Dummy Part | red   |    1 |    5 | 200.1 |
 |   2 | Computex Hardware            | 221 Packer Street |   5 | Dummy Part | red   |    2 |    5 | 200.4 |
 |   3 | Yosemite Sham                | Kathmandu         |   5 | Dummy Part | red   |    3 |    5 | 230.1 |
 |   4 | Linus Media Suppliers        | Montreal          |   5 | Dummy Part | red   |    4 |    5 | 199.1 |
 |   5 | Marques Camera and Equipment | New York          |   5 | Dummy Part | red   |    5 |    5 | 210.1 |
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+-------+
 
 EXTRACTING sname FROM QUERY:
 SELECT s.sname FROM suppliers s INNER JOIN parts p INNER JOIN catalog c ON (p.pid = c.pid AND s.sid = c.sid) WHERE p.color="red";
 +------------------------------+
 | sname                        |
 +------------------------------+
 | Modi parts and distributions |
 | Computex Hardware            |
 | Yosemite Sham                |
 | Linus Media Suppliers        |
 | Marques Camera and Equipment |
 +------------------------------+
 */
---2
SELECT
	s.sid
FROM
	suppliers s
	INNER JOIN parts p ON (
		p.color = "red"
		OR p.color = "green"
	)
	INNER JOIN catalog c ON (
		p.pid = c.pid
		AND s.sid = c.sid
	);

/*
 SELECT * FROM suppliers s INNER JOIN parts  p ON (p.color= "red" OR p.color="green") INNER JOIN catalog c ON (p.pid = c.pid AND s.sid = c.sid);
 +-----+-------------------------------+-------------------+-----+------------+-------+------+------+--------+
 | sid | sname                         | address           | pid | pname      | color | sid  | pid  | cost   |
 +-----+-------------------------------+-------------------+-----+------------+-------+------+------+--------+
 |   1 | Modi parts and distributions  | New Delhi         |   5 | Dummy Part | red   |    1 |    5 |  200.1 |
 |   2 | Computex Hardware             | 221 Packer Street |   5 | Dummy Part | red   |    2 |    5 |  200.4 |
 |   3 | Yosemite Sham                 | Kathmandu         |   5 | Dummy Part | red   |    3 |    5 |  230.1 |
 |   4 | Linus Media Suppliers         | Montreal          |   5 | Dummy Part | red   |    4 |    5 |  199.1 |
 |   5 | Marques Camera and Equipment  | New York          |   5 | Dummy Part | red   |    5 |    5 |  210.1 |
 |   2 | Computex Hardware             | 221 Packer Street |   6 | Dummy Part | green |    2 |    6 | 523.12 |
 |   5 | Marques Camera and Equipment  | New York          |   6 | Dummy Part | green |    5 |    6 |  501.4 |
 |   6 | Mauville Mechanical Solutions | Hoenn             |   6 | Dummy Part | green |    6 |    6 |  411.4 |
 +-----+-------------------------------+-------------------+-----+------------+-------+------+------+--------+
 
 EXTRACTING sid FROM SAME QUERY:
 SELECT s.sid FROM suppliers s INNER JOIN parts  p ON (p.color= "red" OR p.color="green") INNER JOIN catalog c ON (p.pid = c.pid AND s.sid = c.sid);
 +-----+
 | sid |
 +-----+
 |   1 |
 |   2 |
 |   3 |
 |   4 |
 |   5 |
 |   2 |
 |   5 |
 |   6 |
 +-----+
 +-------------------------------+
 */
---3 
SELECT
	s.sid
FROM
	suppliers s
	INNER JOIN parts p
	INNER JOIN catalog c ON (
		s.sid = c.sid
		AND p.pid = c.pid
	)
WHERE
	p.color = "red"
	OR s.address = "221 Packer Street";

/*
 SELECT *  FROM suppliers s INNER JOIN parts p INNER JOIN catalog c ON (s.sid = c.sid AND p.pid = c.pid) WHERE p.color="red" OR s.address="221 Packer Street";
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+--------+
 | sid | sname                        | address           | pid | pname      | color | sid  | pid  | cost   |
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+--------+
 |   1 | Modi parts and distributions | New Delhi         |   5 | Dummy Part | red   |    1 |    5 |  200.1 |
 |   2 | Computex Hardware            | 221 Packer Street |   5 | Dummy Part | red   |    2 |    5 |  200.4 |
 |   3 | Yosemite Sham                | Kathmandu         |   5 | Dummy Part | red   |    3 |    5 |  230.1 |
 |   4 | Linus Media Suppliers        | Montreal          |   5 | Dummy Part | red   |    4 |    5 |  199.1 |
 |   5 | Marques Camera and Equipment | New York          |   5 | Dummy Part | red   |    5 |    5 |  210.1 |
 |   2 | Computex Hardware            | 221 Packer Street |   6 | Dummy Part | green |    2 |    6 | 523.12 |
 +-----+------------------------------+-------------------+-----+------------+-------+------+------+--------+
 
 EXTRACTING sids:
 SELECT s.sid  FROM suppliers s INNER JOIN parts p INNER JOIN catalog c ON (s.sid = c.sid AND p.pid = c.pid) WHERE p.color="red" OR s.address="221 Packer Street";
 +-----+
 | sid |
 +-----+
 |   1 |
 |   2 |
 |   3 |
 |   4 |
 |   5 |
 |   2 |
 +-----+
 */