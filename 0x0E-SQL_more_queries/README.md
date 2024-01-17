
# More MySQL

This readme provides an overview of various MySQL operations and concepts.

## Table of Contents

1. [Creating a New MySQL User](#creating-a-new-mysql-user)
2. [Managing User Privileges](#managing-user-privileges)
3. [Understanding PRIMARY KEY](#understanding-primary-key)
4. [Understanding FOREIGN KEY](#understanding-foreign-key)
5. [Using NOT NULL and UNIQUE Constraints](#using-not-null-and-unique-constraints)
6. [Retrieving Data from Multiple Tables](#retrieving-data-from-multiple-tables)
7. [Understanding Subqueries](#understanding-subqueries)
8. [Understanding JOIN and UNION](#understanding-join-and-union)

## Creating a New MySQL User

To create a new MySQL user, use the following command:

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

## Managing User Privileges

To grant all privileges to a user on a specific database, use the following command:

```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

## Understanding PRIMARY KEY

A PRIMARY KEY is a unique identifier for a record in a table. A table can have only one PRIMARY KEY.

## Understanding FOREIGN KEY

A FOREIGN KEY is a field (or collection of fields) in a table, that is used to establish a link between the data in two tables.

## Using NOT NULL and UNIQUE Constraints

NOT NULL is a constraint that ensures a column cannot have a NULL value. UNIQUE is a constraint that ensures all values in a column are different.

## Retrieving Data from Multiple Tables

To retrieve data from multiple tables in one request, you can use JOIN statements.

## Understanding Subqueries

A subquery is a query that is embedded in the WHERE or HAVING clause of another SQL query.

## Understanding JOIN and UNION

JOIN is used to combine rows from two or more tables, based on a related column. UNION operator is used to combine the result-set of two or more SELECT statements.
```