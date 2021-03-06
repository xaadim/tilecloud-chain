CREATE EXTENSION postgis;

CREATE SCHEMA tests;

CREATE TABLE tests.point (gid serial Primary KEY, name varchar(10));
SELECT AddGeometryColumn('tests', 'point','the_geom',21781,'POINT',2);

CREATE TABLE tests.line (gid serial Primary KEY, name varchar(10));
SELECT AddGeometryColumn('tests', 'line','the_geom',21781,'LINESTRING',2);

CREATE TABLE tests.polygon (gid serial Primary KEY, name varchar(10));
SELECT AddGeometryColumn('tests', 'polygon','the_geom',21781,'POLYGON',2);


INSERT INTO tests.point VALUES (0, 'point1', ST_GeomFromText('POINT (600000 200000)', 21781));
INSERT INTO tests.point VALUES (1, 'point2', ST_GeomFromText('POINT (530000 150000)', 21781));

INSERT INTO tests.line VALUES (0, 'line1', ST_GeomFromText('LINESTRING (600000 200000,530000 150000)', 21781));

INSERT INTO tests.polygon VALUES (0, 'polygon1', ST_GeomFromText('POLYGON ((600000 200000,600000 150000,530000 150000, 530000 200000, 600000 200000))', 21781));
