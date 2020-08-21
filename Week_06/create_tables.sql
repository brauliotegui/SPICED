-- CATEGORIES 1/11
CREATE TABLE categories (
  category_id SERIAL PRIMARY KEY,
  category_name VARCHAR(100) NOT NULL,
  description VARCHAR(250),
  picture BYTEA
);

COPY categories FROM '/Users/braulio/Documents/data/ProjectDashboard/categories.csv' DELIMITER ',' CSV HEADER;

-- CUSTOMERS 2/11
CREATE TABLE customers (
  customerID  VARCHAR(6) PRIMARY KEY,
  company_name VARCHAR(40),
  contact_name VARCHAR(25),
  contact_title VARCHAR(30),
  address VARCHAR(250),
  city VARCHAR(25),
  region VARCHAR(25),
  post_code VARCHAR(10),
  country VARCHAR(100),
  phone VARCHAR(40),
  fax VARCHAR(17)
);

COPY customers FROM '/Users/braulio/Documents/data/ProjectDashboard/customers.csv' DELIMITER ',' CSV HEADER;

-- EMPLOYEE TERRITORIES 3/11
CREATE TABLE employee_territories (
  employee_id INTEGER,
  territory_id SERIAL PRIMARY KEY
);

COPY employee_territories FROM '/Users/braulio/Documents/data/ProjectDashboard/employee_territories.csv' DELIMITER ',' CSV HEADER;

-- EMPLOYEES 4/11
CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  last_name VARCHAR(100) NOT NULL,
  first_name VARCHAR(100),
  job_title VARCHAR(250),
  title VARCHAR(5),
  birth_date DATE,
  hire_date DATE,
  address VARCHAR(250),
  city VARCHAR(40),
  region VARCHAR(3),
  post_code VARCHAR(10),
  country VARCHAR(3),
  phone VARCHAR(15),
  extension VARCHAR(5),
  photo BYTEA,
  notes TEXT,
  reports_to REAL,
  photo_path VARCHAR(250)
);

COPY employees FROM '/Users/braulio/Documents/data/ProjectDashboard/employees2.csv' DELIMITER ',' CSV HEADER;

-- ORDER DETAILS 5/11
CREATE TABLE order_details (
  order_id INTEGER,
  product_id INTEGER,
  unit_price MONEY,
  quantity INTEGER,
  discount MONEY
);

COPY order_details FROM '/Users/braulio/Documents/data/ProjectDashboard/order_details.csv' DELIMITER ',' CSV HEADER;

-- ORDERS 6/11
CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id VARCHAR(6),
  employee_id INTEGER,
  order_date DATE,
  req_date DATE,
  ship_date DATE,
  ship_via INTEGER,
  freight REAL,
  ship_name VARCHAR(50),
  ship_address VARCHAR(250),
  ship_city VARCHAR(40),
  ship_region VARCHAR(25),
  ship_postcode VARCHAR(10),
  ship_country VARCHAR(100)
);

COPY orders FROM '/Users/braulio/Documents/data/ProjectDashboard/orders2.csv' DELIMITER ',' CSV HEADER;

-- PRODUCTS 7/11
CREATE TABLE products (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(50),
  supplier_id  INTEGER,
  category_id INTEGER,
  quantity VARCHAR(50),
  unit_price MONEY,
  units_instock INTEGER,
  units_onorder INTEGER,
  reorder_level INTEGER,
  discontinued BOOLEAN
);

COPY products FROM '/Users/braulio/Documents/data/ProjectDashboard/products.csv' DELIMITER ',' CSV HEADER;

-- REGIONS 8/11
CREATE TABLE regions (
  region_id SERIAL PRIMARY KEY,
  region_description VARCHAR(50)
);

COPY regions FROM '/Users/braulio/Documents/data/ProjectDashboard/regions.csv' DELIMITER ',' CSV HEADER;

-- SHIPPERS 9/11
CREATE TABLE shippers (
  shipper_id SERIAL PRIMARY KEY,
  company_name VARCHAR(100) NOT NULL,
  phone VARCHAR(15)
);

COPY shippers FROM '/Users/braulio/Documents/data/ProjectDashboard/shippers.csv' DELIMITER ',' CSV HEADER;

-- SUPPLIERS 10/11
CREATE TABLE suppliers (
  supplier_id SERIAL PRIMARY KEY,
  company_name VARCHAR(40),
  contact_name VARCHAR(28),
  contact_title VARCHAR(30),
  address VARCHAR (47),
  city VARCHAR (15),
  region VARCHAR (10),
  post_code VARCHAR (10),
  country VARCHAR (15),
  phone VARCHAR (17),
  fax VARCHAR (17),
  homepage VARCHAR(250)
);

COPY suppliers FROM '/Users/braulio/Documents/data/ProjectDashboard/suppliers.csv' DELIMITER ',' CSV HEADER;

-- TERRITORIES 11/11
CREATE TABLE territories (
  territory_id SERIAL PRIMARY KEY,
  territory_description VARCHAR(50),
  region_id INTEGER
);

COPY territories FROM '/Users/braulio/Documents/data/ProjectDashboard/territories.csv' DELIMITER ',' CSV HEADER;
