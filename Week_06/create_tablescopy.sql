CREATE TABLE IF NOT EXISTS orders (
               order_id INT PRIMARY KEY,
               customer_id VARCHAR(255) ,
               employee_id INT,
               order_date VARCHAR(250),
               required_date VARCHAR(250),
               shipped_date VARCHAR(250),
               ship_via INT,
               freight REAL ,
               ship_name VARCHAR(255) ,
               ship_adress VARCHAR(255) ,
               ship_city VARCHAR(255) ,
               ship_region VARCHAR(255) ,
               ship_postalcode VARCHAR(255),
               ship_country VARCHAR(255)
       );


CREATE TABLE IF NOT EXISTS order_details (
  -- order_id INT REFERENCES orders(order_id),
  order_id INT ,
  product_id FLOAT(4) ,
  unit_price FLOAT(4),
  quantity INTEGER,
  discount FLOAT(4)
);


CREATE TABLE IF NOT EXISTS customers (
  customer_id VARCHAR(25) PRIMARY KEY,
  company_name VARCHAR(255),
  contact_name VARCHAR(255),
  contact_title VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(25),
  region VARCHAR(25),
  postalcode VARCHAR(25),
  country VARCHAR(25),
  phone VARCHAR(25),
  fax VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS employees (
  employee_id VARCHAR(25) PRIMARY KEY,
  last_name VARCHAR(255),
  first_name VARCHAR(255),
  title VARCHAR(255)
);


\COPY orders FROM '/Users/stefanroth/spiced/cohorts/logistic-lemongrass-encounter-notes/week_06/northwind_data_clean/data/orders.csv' WITH (HEADER true, FORMAT csv);

\COPY order_details FROM '/Users/stefanroth/spiced/cohorts/logistic-lemongrass-encounter-notes/week_06/northwind_data_clean/data/order_details.csv' WITH (HEADER true, FORMAT csv);

\COPY customers FROM '/Users/stefanroth/spiced/cohorts/logistic-lemongrass-encounter-notes/week_06/northwind_data_clean/data/customers.csv' WITH (HEADER true, FORMAT csv);

\COPY employees FROM PROGRAM 'cut -d "," -f 1,2,3,4 /Users/stefanroth/spiced/cohorts/logistic-lemongrass-encounter-notes/week_06/northwind_data_clean/data/employees.csv' WITH (HEADER true, FORMAT csv);
