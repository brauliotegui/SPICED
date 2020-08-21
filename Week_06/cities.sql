DROP TABLE cities;
-- comments: Drop table if it alraedy exists

CREATE TABLE cities (
  id SERIAL PRIMARY KEY, -- name, data type, constraints. Primary Key = unique!
  name VARCHAR(50),
  population INTEGER, -- 2**32 = 4,294,967,296
  country VARCHAR(50) NOT NULL
);

INSERT INTO cities (name, population, country)
VALUES ('Berlin', 3800000, 'Germany');
INSERT INTO cities (name, population, country)
VALUES ('Paris', 8000000, 'France');
INSERT INTO cities (name, population, country)
VALUES ('New York City', 12000000, 'USA');
