# SQL NOTES


### Schema

- Schema in the MS SQL Server world is considered to be the category that a groups a set of tables.
- For example, the schema for tables (student_info, classes, login_info) could be bard_college.
```
bard_college.classes
```
- Schema can also refer to the actual layout of the tables. For example, Table One is connected to Table Two via this relationship. Table One carries this information while Table Two carries this information. Essentially, it is the connections and distribution of the information across multiple tables in one diagram.


### Tip to Back Up Table

- An easy way to back up a table in case you want to do some manipulation and do not want to lose/overwrite information is to run the follow command:
```
SELECT * INTO destination_table FROM (SELECT * FROM original_table)
```
- Provided the schema is the same for the desitination table, this will create a duplicate.
- NOTE This may take a while if the table is large and indexes and such may not transfer over.

### UNION

- Union is used to combine the results of two queries vertically. Imagine, you have two tables that have student information for seperate classes. The information is the same column wise but the data is storeds seperately. If you wanted to see all the info together, you can use UNION to combine them vertically into one table.
- For example:
```
SELECT * FROM physics_table UNION SELECT * FROM chemistry_table
```
- This will combine these two tables vertically.
- NOTE The above statement will only keep the UNIQUE VALUES meaning duplicates will be lossed.
- NOTE In addition, you can specify which columns in either SELECT statement because they do need to match in number of columns.
- To keep duplicates, you need to use UNION ALL
```
SELECT * FROM physics_table UNION ALL SELECT * FROM chemistry_table
```

### VIEW

- A view is a dynamically generated table that is read only. For example, lets say you have a few tables that are combined in an intricate way to produce a sub table. Now this operation at the time of its execution creates the temp table we are interested in. But maybe we want to save this somewhere for later. If we save it into a table, the table will only have a snapshot of the information at that time. A view will store the operation necessary to create itself and run that operation each time it is called, thus pulling the latest information.
- NOTE A View is read-only!!
```
CREATE VIEW "name_of_the_view" AS 
"SELECT * FROM employee_table AS emp 
INNER JOIN salary_table AS sal 
ON sal.employee_id = emp.id"
```
- Each time the view is called, the join operation will be executed and any new information that fulfills the condition above will appear.

### INDEXES

- Indexes are used to be able to grab information faster. The index provides a unique location for each row of data and, based on this key, can retrieve the information alot faster than navigating through a table one by one.
- Types of Indexes:
	- Unique Index - This enforces that each index is unique. Generally, we see this used as the INTEGER ID number in every table. 
	- Clustered Index - This enforces SQL to write the table to the disck in the order you have specified.
- NOTE Everytime more indexes are being added to any table, the amount of time taken to "write" to the table increases being each row needs to examined and placed in its corresponding index file. 

### Creating Functions

- Functions are useful because they are reusable blocks of code that allow you to keep your code organized and D.R.Y (Don't Repeat Yourself).
```
CREATE FUNCTION next_year(@salary INTEGER)
RETURNS INTEGER
AS
BEGIN

SET @answer = @salary * 1.10

RETURN @answer

END
```

### Creating Procedure

- A Procedure or commonly referred to as a Store Procedure is used to create a set of operations (similar to a function) which explain a set of SQL statements that need to be executed together. For example, if you add an employee to a company, there would need to be multiple tables across the company's database that need to be updated. Therefore, someone would create a store procedure that will do the following and only write it once.
```
CREATE PROCEDURE add_employee(@name VARCHAR,@position VARCHAR,@salary FLOAT)
AS
BEGIN

INSERT INTO employee_table(name, position) VALUES (@name, @position)

SET @new_id = SELECT id FROM employee_table WHERE name = @name AND position = @position;

INSERT INTO salary_table(employee_id, salary) VALUES (@new_id, @salary)

END
```
- To invoke the function, write the command as such:
```
EXEC add_employee("Ted Dibiase", "Wrestler", 1000000.00)
```


### Useful Aggregate Functions

#### isnull()

- isnull() allows you to provide a certain value in that column if the value found is NULL.
- For example,
```
SELECT name, isnull(age,"Unknown"), birthday FROM employee_table
```









