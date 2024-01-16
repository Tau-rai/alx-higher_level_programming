# MySQL Basics

This README provides a brief overview of MySQL, a popular relational database management system.

## Contents

1. [What's a Database?](#whats-a-database)
2. [What's a Relational Database?](#whats-a-relational-database)
3. [What does SQL Stand for?](#what-does-sql-stand-for)
4. [What's MySQL?](#whats-mysql)
5. [How to Create a Database in MySQL](#how-to-create-a-database-in-mysql)
6. [What does DDL and DML Stand for?](#what-does-ddl-and-dml-stand-for)
7. [How to CREATE or ALTER a Table](#how-to-create-or-alter-a-table)
8. [How to SELECT Data from a Table](#how-to-select-data-from-a-table)
9. [How to INSERT, UPDATE or DELETE Data](#how-to-insert-update-or-delete-data)
10. [What are Subqueries?](#what-are-subqueries)
11. [How to Use MySQL Functions](#how-to-use-mysql-functions)

## What's a Database?

A database is an organized collection of data stored and accessed electronically. It is designed to hold data that is structured in a way that makes data accessible, reliable, and fast to retrieve.

## What's a Relational Database?

A relational database is a type of database that organizes data into tables, and links them based on relationships between different data points. These relationships enable the efficient retrieval of data from multiple tables within the database.

## What does SQL Stand for?

SQL stands for Structured Query Language. It's a standard language for managing and manipulating databases.

## What's MySQL?

MySQL is an open-source relational database management system (RDBMS) that uses SQL for processing the data in the database. MySQL provides a flexible way to store, manage and retrieve data.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the `CREATE DATABASE` command followed by the name of the database.

```sql
CREATE DATABASE database_name;
```

## What does DDL and DML Stand for?

DDL stands for Data Definition Language. It includes SQL commands such as `CREATE`, `ALTER`, and `DROP` which define or modify the structure of database objects.

DML stands for Data Manipulation Language. It includes SQL commands such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE` which are used to manipulate the data present in the database.

## How to CREATE or ALTER a Table

To create a table in MySQL, you can use the `CREATE TABLE` command. For example:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

To alter a table, you can use the `ALTER TABLE` command. For example, to add a column:

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

## How to SELECT Data from a Table

To select data from a table, you can use the `SELECT` command. For example, to select all data from a table:

```sql
SELECT * FROM table_name;
```

## How to INSERT, UPDATE or DELETE Data

To insert data into a table, you can use the `INSERT INTO` command:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

To update data in a table, you can use the `UPDATE` command:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

To delete data from a table, you can use the `DELETE` command:

```sql
DELETE FROM table_name WHERE condition;
```

## What are Subqueries?

A subquery is a query nested inside another query. It can be used to return data that will be used in the main query as a condition to further restrict the data to be retrieved.

## How to Use MySQL Functions

MySQL provides various functions like `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`, etc. to perform operations on the data. These functions can be used in the SQL queries.

For example, to get the total number of records in a table:

```sql
SELECT COUNT(*) FROM table_name;
```
