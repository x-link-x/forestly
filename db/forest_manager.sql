DROP TABLE IF EXISTS trees;
DROP TABLE IF EXISTS tree_types;
DROP TABLE IF EXISTS areas;

CREATE TABLE tree_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    easting VARCHAR(255),
    northing VARCHAR(255)
);

CREATE TABLE trees (
    id SERIAL PRIMARY KEY,
    approx_age INT,
    tree_type VARCHAR(255),
    x INT,
    y INT,
    area VARCHAR(255)
);

