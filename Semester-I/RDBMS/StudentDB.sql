-- Task 1: Create a Database
-- Write an SQL query to create a database named 'StudentDB'.
CREATE DATABASE StudentDB;
USE StudentDB;



-- Task 2: Create a Table
-- Inside 'StudentDB', create a table named 'Students' with the following columns:
-- - StudentID (INT, Primary Key)
-- - Name (VARCHAR(50))
-- - Age (INT)
-- - Department (VARCHAR(50))
-- - Marks (INT)
CREATE TABLE Students (
   StudentID INT PRIMARY KEY,
   StudentName VARCHAR(50),
   Age INT,
   Department VARCHAR(50),
   Marks INT
);

-- Task 3: Insert Dummy Data
-- Insert at least 5 records into the 'Students' table.
INSERT INTO 
Students	(StudentID, StudentName, Age, Department, Marks) 
VALUES
	(1, 'Ritik Raj',	21, 'Computer Science', 100),
	(2, 'Rocky',	21, 'Mathematics',		90),
	(3, 'Ironman', 22, 'Physics', 			99),
	(4, 'Price', 	20, 'Chemistry', 		88),
	(5, 'Lucifer', 	23, 'History', 100);
    

    
SELECT * FROM Students;