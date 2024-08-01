## Sales Manager

Sales Manager is an online program designed for Salesman to view and access their sales. Allowing clients to reach out to salesmen through the program and salesmen to look at their sales and make changes as needed. 

## Table of Contents
- [Features](#features)
- [Project-Structure](#project-structure)
- [Technologies](#technologies)
- [Installation](#installation)
- [License](#license)

## Features

Create: Clients can reach out to salesmen and create a sale for the salesman to view
Inventory: Salesman can view all sales under their name
Management: Salesman can manage their sales and update where the sales are at in the process
Data: Salesmen can look at their sales and see if the sale is In Progress, Sold, or lost.

## Project-Structure

Lib/ 
All necessary files are under the lib folder

companies.py -> cli.py

cli.py - has the necessary CLI code to run the program on the terminal
companies.py - has the Python elements that hold the ORM and the classes of the program
seed.sql - Starter SQL data 
company.db - SQL database

## Technologies

Python3
Sqlite3

## Installation

Ensure you have the following Installed:

- Python 3.8+
- sqlite3

Setup

Fork and clone this repository:
    ```
    git clone https://github.com/your-username/Phase-3-Final-Project
    cd Phase-3-Final-Project
    ```

Create a virtual environment with pipenv:
    ```
    pipenv install
    ```
cd into the lib/ folder:
    ```
    cd lib/
    ```

Enter in a virtual environment with pipenv shell:
    ```
    pipenv shell
    ```

Run seed.sql file to start database:
start by entering a sqlite3 terminal:
    ```
    sqlite3
    ```
    ```
    .read seed.sql
    ```

Exit sqlite3 terminal
Start the program with python3 cli.py:
    ```
    python3 cli.py
    ```

## License

Open Source Program

