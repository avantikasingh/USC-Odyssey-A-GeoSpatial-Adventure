CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
--Create Table
CREATE TABLE LOCATION (name varchar, geom geometry);
INSERT INTO LOCATION VALUES
	('Leavey','POINT(-118.283273 34.021643)'),
	('Doheny', 'POINT(-118.284206 34.020280)'),
	('Sc Eng', 'POINT(-118.288937 34.019427)'),
	('RockReily', 'POINT(-118.2841499714709 34.024143737824254)'),
	('Parkside', 'POINT(-118.29120391259077 34.01861479359072)'),
	('RTC', 'POINT(-118.286008 34.020616)'),
	('Generations', 'POINT(-118.28328280156035 34.02227379657735)'),
	('Cinematics', 'POINT(-118.286413 34.023482)'),
	('TrojanHorse', 'POINT(-118.285177 34.020304)'),
	('Accounting', 'POINT(-118.285881 34.019207)'),
	('Roski', 'POINT(-118.287356 34.019531)'),
	('Herman Ostrow', 'POINT(-118.285765 34.023601)'),
	('Home', 'POINT(-118.288650 34.032033)');

SELECT name, ST_AsText(geom) FROM LOCATION;

--Convex Hull
SELECT ST_AsText(ST_ConvexHull(ST_Collect(geom))) FROM LOCATION;

--Nearest Neighbors of SAL
SELECT name, ST_Astext(geom) as location, ST_Distance(geom,'POINT(-118.288650 34.032033)') as distance
FROM LOCATION
WHERE name<>'Home'
ORDER BY ST_Distance(geom,'POINT(-118.288650 34.032033)')
limit 4;