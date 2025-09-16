

create table Students(StudentID int, Name varchar(20), Age int, DepartmentID int);
create table Departments (DepartmentID int , DepartmentName varchar(20));
create table Marks (MarkID int, StudentID int, Subject varchar(10), Marks int);

insert into Students(StudentID, Name, Age, DepartmentID) values 
(1, 'Amit', 20, 1),
(2, 'Riya', 22, 2),
(3, 'Arjun', 20, 2),
(4, 'Karan', 21, 1),
(5, 'Neha', 23, 3);


insert into Departments(DepartmentID, DepartmentName ) values (1, 'Computer Science'), (2, 'Mathematic'), (3, 'Physics');

insert into Marks (MarkID, StudentID, Subject, Marks) values 
(1, 1, 'DBMS', 85),
(2, 1, 'AI', 90),
(3, 2, 'DBMS', 75),
(4, 2, 'AI', 80),
(5, 3, 'DBMS', 88),
(6, 4, 'AI', 92),
(7, 5, 'DBMS', 70);



-- select * from Students;


-- 1. Retrieve all students along with their department names.

select s.Name, d.DepartmentName from Students as s  join Departments as d on d.DepartmentID = s.DepartmentID;

-- SELECT 
--     RIGHT('000' + CAST(s.StudentID AS VARCHAR(3)), 3) AS StudentID,
--     s.Name,
--     s.Age,
--     d.DepartmentName
-- FROM Students s
-- JOIN Departments d
--     ON s.DepartmentID = d.DepartmentID;



-- 2. Find the average marks obtained by each student.


SELECT s.Name, AVG(m.Marks) as AverageMarks from Students as s JOIN Marks as m on s.StudentID=m.StudentID GROUP BY s.StudentID, s.Name;



-- 3. Find the maximum marks in each subject.
-- 4. List students who scored more than 80 in all subject.
-- 5. Retrieve all students ordered by their average marks in descending order.
-- 6. Find the total marks scored by students in each department.
-- 7. Display students who have not received any marks yet.
-- 8. Retrieve department names along with the number of students enrolled in each department.
-- 9. Find the student with the highest marks in AI subject.
-- 10. Display all students along with their average marks (if any), showing 0 where marks are not available.


