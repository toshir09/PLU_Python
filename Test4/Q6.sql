create database schooldb;
use schooldb;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    CourseID INT
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

INSERT INTO Student (StudentID, Name, CourseID)
VALUES
(1, 'Rahul', 201),
(2, 'Neha', 202),
(3, 'Aman', NULL);

INSERT INTO Course (CourseID, CourseName)
VALUES
(201, 'Python'),
(202, 'SQL');

SELECT
Student.Name,
Course.CourseName
FROM Student
LEFT JOIN Course
ON Student.CourseID = Course.CourseID;