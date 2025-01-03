------------------------------- Stored Procedure --------------------------
-- Add new student to Student table

CREATE PROCEDURE setStudent
    @StudName VARCHAR(255),
    @Address VARCHAR(50),
    @Email VARCHAR(50),
    @phone VARCHAR(50),
	@Gender VARCHAR(50),
	@DOB DATE, 
	@DeptId INT,
	@LevelId INT,
	@ScholarId INT
AS
BEGIN
    INSERT INTO [student] (name, DOB, gender, address, phone, email, department_id, level_id,Scholar_id)
    VALUES (@StudName, @DOB, @Gender, @Address, @phone, @Email, @DeptId, @LevelId,@ScholarId);
END;

EXEC setStudent
    @StudName = 'John Doe',
    @Address = '123 Main St',
    @Email = 'johndoe@example.com',
    @phone = '123-456-7890',
    @Gender = 'Male',
    @DOB = '2000-01-01',
    @DeptId = 1,
    @LevelId = 2,
    @ScholarId = 3;

SELECT * FROM Student

-----------------------------------------------------------------------------------------------------------
-- Get all students
CREATE PROCEDURE GetAllStudents

AS
BEGIN
    SELECT id , name , address , gender , DOB , phone , email , department_id , level_id , Scholar_id
    FROM Student
END;

EXEC GetAllStudents
-------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE GetOneStudent
	@studId int
AS
BEGIN
    SELECT *
    FROM Student
	where id = @studId
END;

EXEC GetOneStudent 2
-------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE DeleteStudent 
	@studId INT 
AS
BEGIN
    DELETE FROM Student
	WHERE id = @studId
END;

EXEC DeleteStudent  6
--------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE UpdateStudent
	@studId int,
    @StudName VARCHAR(255),
    @Address VARCHAR(50),
    @Email VARCHAR(50),
    @phone VARCHAR(50),
	@Gender VARCHAR(50),
	@DOB DATE, 
	@DeptId INT,
	@LevelId INT,
	@ScholarId INT
AS
BEGIN
    UPDATE [student]
    SET name = @StudName, DOB = @DOB, 
		gender = @Gender, address = @Address, 
		phone = @phone, email = @Email, 
		department_id = @DeptId, level_id = @LevelId,
		Scholar_id = @ScholarId
	WHERE Id = @studId;
END;

--EXEC UpdateStudent BLA BLA
----------------------------------------------------------------------------


CREATE PROCEDURE GetStudentWithName
    @studName VARCHAR(50)
AS
BEGIN
    SELECT  id , name , address , gender , DOB , phone , email , department_id , level_id , Scholar_id
    FROM Student
    WHERE name LIKE '%' + @studName + '%'
END;

EXEC GetStudentWithName @studName = 'Michael Brown' 
-------------------------------------------------------------------------------
CREATE PROCEDURE Getlevel
AS
BEGIN
    SELECT id , name 
    FROM Levels
END;

EXEC Getlevel
-------------------------------------------------------------------------------------
CREATE PROCEDURE GetScholarships
AS
BEGIN
    SELECT id , name 
    FROM Scholarships
END;

EXEC GetScholarships
----------------------------------------------------------------------------------------
CREATE PROCEDURE GetDepartments
AS
BEGIN
    SELECT id , name 
    FROM Departments
END;

EXEC GetDepartments
-----------------------------------------------------------------------------------------
CREATE PROCEDURE GetCoursec
AS
BEGIN
    SELECT id , name 
    FROM Courses
END;

EXEC GetCoursec
-----------------------------------------------------------------------------------------
CREATE PROCEDURE GetStudWithGrade
	@grade VARCHAR(2),
	@courseId VARCHAR(50),
	@levelId INT
AS
BEGIN
		SELECT  id , name , address , gender , DOB , phone , email , department_id , level_id , Scholar_id 
        FROM Student 
        WHERE id IN (
            SELECT student_id 
            FROM StudentExams 
            WHERE grade = @grade 
              AND exam_id IN (
                  SELECT id 
                  FROM Exams 
                  WHERE course_id = @courseId AND level_id = @levelId
              )
        ) 
          AND level_id = @levelId;
END;

EXEC GetStudWithGrade 'A' , 2 ,1
---------------------------------------------------------------------------------------
---------------------------------------Views------------------------------------
CREATE VIEW Schedule AS
SELECT 
    C.[name] AS CourseName,
    P.[name] AS PlaceName,
    L.[day] AS [Day],
    L.start_time AS StartTime,
    L.end_time AS EndTime
FROM 
    Lectures L
JOIN 
    Courses C ON L.course_id = C.id
JOIN 
    Places P ON L.place_id = P.id;


SELECT * FROM Schedule

---------------------------------------------------

CREATE VIEW CourseDetails AS
SELECT 
    C.[name] AS CourseName,
    C.[hours] AS [Hours],
    L.[name] AS LevelName,
    D.[name] AS DepartmentName
FROM 
    Courses C
JOIN 
    Levels L ON C.level_id = L.id
JOIN 
    Departments D ON C.department_id = D.id;

SELECT * FROM CourseDetails
---------------------------------------------------

CREATE VIEW ExamResults AS
SELECT 
    S.[name] AS StudentName,
    E.[date] AS ExamDate,
    E.[type] AS ExamType,
    SE.[status] AS [Status],
    SE.grade AS Grade
FROM 
    StudentExams SE
JOIN 
    Exams E ON SE.exam_id = E.id
JOIN 
    Student S ON SE.student_id = S.id;

SELECT * FROM ExamResults

-------------------------------------------

CREATE VIEW StudentBooks AS
SELECT 
    B.title AS BookTitle,
    B.author AS Author,
    C.[name] AS CourseName
FROM 
    Books B
JOIN 
    Courses C ON B.course_id = C.id;

SELECT * FROM StudentBooks

-------------------------------------

CREATE VIEW StudentsCountByDepartment AS
SELECT 
    D.[name] AS DepartmentName,
    COUNT(S.id) AS StudentCount
FROM 
    Departments D
LEFT JOIN 
    Student S ON S.department_id = D.id
GROUP BY 
    D.[name];

SELECT * FROM StudentsCountByDepartment

-------------------------------------

CREATE VIEW ProfessorsOverview AS
SELECT 
    E.[name] AS ProfessorName,
	C.[name] AS CourseName,
    D.[name] AS DepartmentName,
    L.[name] AS LevelName
FROM 
    Professors P
JOIN 
    Employees E ON P.employee_id = E.id
JOIN 
    CoursesProfessors CP ON P.employee_id = CP.professor_id
JOIN 
    Courses C ON CP.course_id = C.id
JOIN 
    Levels L ON C.level_id = L.id
JOIN 
    Departments D ON C.department_id = D.id

SELECT * FROM ProfessorsOverview


---------------------------Triggers------------------------
	
CREATE TRIGGER trg_Departments_Delete
ON Departments
INSTEAD OF DELETE
AS
BEGIN
    IF EXISTS (
        SELECT 1 FROM Employees WHERE department_id IN (SELECT id FROM deleted)
    )
    BEGIN
        RAISERROR('Cannot delete department with assigned employees.', 16, 1);
        ROLLBACK TRANSACTION;
    END
    ELSE
    BEGIN
        DELETE FROM Departments WHERE id IN (SELECT id FROM deleted);
    END
END; 

DELETE FROM Departments WHERE id = 1

------------------------------------------------

CREATE TRIGGER trg_Courses_Update
ON Courses
FOR UPDATE
AS
BEGIN
    -- Check if the hours column in the updated rows is less than 10
    IF EXISTS (SELECT 1 FROM inserted WHERE hours < 10)
    BEGIN
        -- Raise an error message and roll back the transaction
        RAISERROR('Courses must have at least 10 hours.', 16, 1);
        ROLLBACK TRANSACTION;
    END
END;

UPDATE Courses 
SET hours = 5 
WHERE id = 5

-------------------------------------------------------

CREATE TRIGGER prevent_delete_level4
ON student
FOR DELETE
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM deleted
        WHERE level_id = 4
    )
    BEGIN
        RAISERROR ('Deletion is not allowed for students in level 4.', 16, 1);
        ROLLBACK TRANSACTION;
    END
END;

DELETE FROM Student 
WHERE level_id = 4

----------------------------------------------------------------

CREATE TRIGGER set_failed_status
ON studentexams
AFTER INSERT, UPDATE
AS
BEGIN
    -- Update status to 'failed' if grade is F
    UPDATE studentexams
    SET status = CASE
                   WHEN grade = 'F' THEN 'failed'
                   ELSE 'passed'
                 END
    WHERE student_id IN (SELECT student_id FROM inserted)
      AND exam_id IN (SELECT exam_id FROM inserted);
END;

--------------------------------------------- queries

-------1. number of students in each level  
SELECT l.name AS level_name, COUNT(s.id) AS student_count
FROM Levels l INNER JOIN Student s ON s.level_id = l.id
GROUP BY l.name;


----------2. number of courses and their names that each proff teach   3   
SELECT
    e.name AS professor_name,
    COUNT(cp.course_id) AS course_count,
    STRING_AGG(c.name, ', ') AS course_names
FROM Employees e
INNER JOIN Professors p ON e.id = p.employee_id
INNER JOIN CoursesProfessors cp ON p.employee_id = cp.professor_id
INNER JOIN Courses c ON cp.course_id = c.id
GROUP BY e.name;


-------3. profs that do not manage a department
SELECT e.name AS professor_name
FROM Employees e
INNER JOIN Professors p ON e.id = p.employee_id LEFT JOIN Departments d ON d.manager_id = p.employee_id
WHERE d.id IS NULL;

