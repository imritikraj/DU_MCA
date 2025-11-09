CREATE DATABASE EmployesDB;
USE EmployesDB;

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    Salary INT,
    JoiningDate DATE
);


INSERT INTO Employees (EmpID, EmpName, Department, Salary, JoiningDate)
VALUES 	(1, "Amit",  "HR",      45000, '2020-01-15'), 
		(2, "Neha",  "IT",      60000, '2019-03-10'),
		(3, "Ravi",  "Finance", 55000, '2021-07-22'),
		(4, "Simran","IT",      70000, '2018-11-01'),
		(5, "Raj", 	 "Finance", 50000, '2020-06-18'),
		(6, "Priya", "HR",      48000, '2021-02-25'),
		(7, "Arjun", "IT",      65000, '2019-12-30');
        
-- 1. Retrieve all employees who work in the IT department.
SELECT * FROM Employees
WHERE Department = 'IT';

-- 2. Find employees with a salary greater than 55,000. 
SELECT * FROM Employees
WHERE Salary > 55000;

-- 3. Display the names of employees who joined after 2020-01-01.
SELECT * FROM Employees
WHERE JoiningDate > '2020-01-01';

-- 4. Calculate the average salary of employees in each department. 
SELECT Department, AVG(Salary) AS avg_salary
FROM Employees
GROUP BY Department;

-- 5. Find the highest salary in the Finance department. 
SELECT Department, MAX(Salary) AS max_salary
FROM Employees
WHERE Department = 'Finance';

-- 6. Count the number of employees in each department.
SELECT COUNT(*) AS NumberOfEmployes, Department
FROM Employees
GROUP BY Department;

-- 7. Display employees ordered by their salary in descending order.
SELECT EmpID, EmpName, Salary 
FROM Employees
ORDER BY salary DESC;

-- 8. Find departments having more than 2 employees.
SELECT Department, COUNT(*) AS NumberOfEmployes
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 2;

-- 9. Show the total salary expenditure of the IT department. 
SELECT sum(salary) as TotalExpenditure 
FROM Employees 
WHERE department = 'IT';

-- 10. Retrieve employees whose names start with 'R'. 
SELECT *
FROM Employees
WHERE EmpName LIKE 'R%';

