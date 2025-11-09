CREATE DATABASE UniversityDB;
USE UniversityDB;

-- Create table: Departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL
);

-- Create table: Students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Age INT,
    DepartmentID INT
);

-- Create table: Marks
CREATE TABLE Marks (
    MarkID INT PRIMARY KEY,
    StudentID INT,
    Subjects VARCHAR(100) NOT NULL,
    Marks INT
);

-- Insert data into Departments
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics');

-- Insert data into Students
INSERT INTO Students (StudentID, StudentName, Age, DepartmentID) VALUES
(1, 'Amit',	 20, 1),
(2, 'Riya',  22, 2),
(3, 'Karan', 21, 1),
(4, 'Neha',  23, 3),
(5, 'Arjun', 20, 2);

-- Insert data into Marks
INSERT INTO Marks (MarkID, StudentID, Subjects, Marks) VALUES
(1, 1, 'DBMS', 85),
(2, 1, 'AI',   90),
(3, 2, 'DBMS', 75),
(4, 2, 'AI',   80),
(5, 3, 'DBMS', 88),
(6, 4, 'AI',   92),
(7, 5, 'DBMS', 70);


-- 1. Retrieve all students along with their department names.
SELECT s.StudentID, s.StudentName, s.Age, d.DepartmentName
FROM Students s
JOIN Departments d ON s.DepartmentID = d.DepartmentID;

-- 2. Find the average marks obtained by each student.
SELECT s.StudentID, s.StudentName, AVG(m.Marks) AS AverageMarks
FROM Students s
JOIN Marks m ON s.StudentID = m.StudentID
GROUP BY s.StudentID, s.StudentName;

-- 3. Find the maximum marks in each subject.
SELECT Subjects, MAX(Marks) AS MaxMarks
FROM Marks
GROUP BY Subjects;

-- 4. List students who scored more than 80 in all subjects.
SELECT s.StudentID, s.StudentName
FROM Students s
JOIN Marks m ON s.StudentID = m.StudentID
GROUP BY s.StudentID, s.StudentName
HAVING MIN(m.Marks) > 80;

-- 5. Retrieve all students ordered by their average marks in descending order.
SELECT s.StudentID, s.StudentName, AVG(m.Marks) AS AverageMarks
FROM Students s
JOIN Marks m ON s.StudentID = m.StudentID
GROUP BY s.StudentID, s.StudentName
ORDER BY AverageMarks DESC;

-- 6. Find the total marks scored by students in each department.
SELECT d.DepartmentName, SUM(m.Marks) AS TotalMarks
FROM Students s
JOIN Departments d ON s.DepartmentID = d.DepartmentID
JOIN Marks m ON s.StudentID = m.StudentID
GROUP BY d.DepartmentName;

-- 7. Display students who have not received any marks yet.
SELECT s.StudentID, s.StudentName
FROM Students s
LEFT JOIN Marks m ON s.StudentID = m.StudentID
WHERE m.StudentID IS NULL;

-- 8. Retrieve department names along with the number of students enrolled in each department.
SELECT d.DepartmentName, COUNT(s.StudentID) AS NumStudents
FROM Departments d
LEFT JOIN Students s ON d.DepartmentID = s.DepartmentID
GROUP BY d.DepartmentName;

-- 9. Find the student with the highest marks in AI subject.
SELECT s.StudentID, s.StudentName, m.Marks
FROM Students s
JOIN Marks m ON s.StudentID = m.StudentID
WHERE m.Subjects = 'AI'
ORDER BY m.Marks DESC
LIMIT 1;

-- 10. Display all students along with their average marks (if any), showing 0 where marks are not available.
SELECT s.StudentID, s.StudentName, COALESCE(AVG(m.Marks), 0) AS AverageMarks
FROM Students s
LEFT JOIN Marks m ON s.StudentID = m.StudentID
GROUP BY s.StudentID, s.StudentName;

