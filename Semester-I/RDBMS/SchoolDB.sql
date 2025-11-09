-- 1. Create a database named 'SchoolDB' 
CREATE DATABASE SchoolDB;
USE SchoolDB;


-- 2. Inside this database, create a table named 'Students' with the following columns:
--    - student_id (INT, Primary Key)
--    - name (VARCHAR(50))
--    - age (INT)
--    - grade (VARCHAR(10))
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    sname VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);


-- 3. Insert dummy records into the 'Students' table
INSERT INTO Students (student_id, sname, age, grade) VALUES
(1, 'Alice', 14, '8th'),
(2, 'Bob', 15, '9th'),
(3, 'Charlie', 13, '7th'),
(4, 'David', 14, '8th'),
(5, 'Eva', 15, '9th'),
(6, 'Frank', 16, '10th'),
(7, 'Grace', 12, '6th'),
(8, 'Helen', 14, '8th');

-- 4. Select all records from 'Students'.
SELECT * FROM Students;


-- 5. Select names and grades of students only.
SELECT sname, grade FROM Students;


-- 6. Select students who are older than 14 years.
SELECT * FROM Students
WHERE age > 14;


-- 7. Select students in '8th' grade.
SELECT * FROM Students
WHERE grade = '8th';




-- 8. Update Alice age from 14 to 15.
SET SQL_SAFE_UPDATES = 0;

UPDATE Students
SET age = 15
WHERE sname = 'Alice';

-- SELECT * FROM Students WHERE sname = 'Alice';


-- 9. Delete a student record with student_id = 3.
DELETE FROM Students
WHERE student_id = 3;


-- 10. Delete all students in '7th' grade.
DELETE FROM Students
WHERE grade = '7th';

-- SELECT * FROM Students;


-- 11. Write an SQL query to drop the 'Students' table from the database.
DROP TABLE Students;

