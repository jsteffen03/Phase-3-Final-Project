DROP TABLE salesman;
DROP TABLE sales;
DROP TABLE clients;

CREATE TABLE IF NOT EXISTS salesman(
    id INTEGER PRIMARY KEY,
    name TEXT,
    company_name TEXT
);

CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone INTEGER,
    budget INTEGER
);

CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    sales_id INT,
    client_id INT,
    price INT,
    next_appointment DATE,
    last_contact DATE,
    progress TEXT,
    FOREIGN KEY (sales_id) REFERENCES salesman(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

INSERT INTO salesman(name, company_name)
VALUES("Trevin", "Zebrascapes");
INSERT INTO salesman(name, company_name)
VALUES("Justin", "Zebrascapes");
INSERT INTO salesman(name, company_name)
VALUES("Josh", "Zebrascapes");
INSERT INTO salesman(name, company_name)
VALUES("David", "Zebrascapes");

INSERT INTO clients(name, phone, budget)
VALUES("Nancy", 7198456251, 45000);

INSERT INTO sales(sales_id, client_id, price, next_appointment, last_contact, progress)
VALUES(1, 1, 45000, "2024-03-15", "2024-03-05", "In Progress");


