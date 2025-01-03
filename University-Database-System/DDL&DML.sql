
------------------------------------- region DDL

CREATE DATABASE University_

USE University_

CREATE TABLE Employees (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
	job_title VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    salary FLOAT NOT NULL,
    DOB DATE NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
	department_id INT 
    );
	
CREATE TABLE Departments (
  id INT PRIMARY KEY IDENTITY,
  name VARCHAR(50) NOT NULL,
  location VARCHAR(50) NOT NULL,
  description VARCHAR(100) NOT NULL,
  manager_id INT 
  );
  
  ALTER TABLE Employees
    ADD CONSTRAINT FK_Employees_Departments
    FOREIGN KEY (department_id) REFERENCES Departments(id) 
	ON DELETE SET NULL
	ON UPDATE CASCADE
	;

  CREATE TABLE professors (
    employee_id INT PRIMARY KEY,
    researches VARCHAR(50) NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employees(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
  );
 ALTER TABLE Departments
    ADD CONSTRAINT FK_Professors_Departments
    FOREIGN KEY (manager_id) REFERENCES Professors(employee_id);
	
	CREATE TABLE Levels (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(50) NOT NULL,
);
CREATE TABLE Scholarships (
    id INT PRIMARY KEY IDENTITY,
	name VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    rules VARCHAR(50) NOT NULL,
);
CREATE TABLE Student (
    id INT PRIMARY KEY IDENTITY ,
    address VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    phone VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    level_id INT NOT NULL,
    Scholar_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(id)
	ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES Levels(id)
	ON UPDATE CASCADE,
    FOREIGN KEY (Scholar_id) REFERENCES scholarships(id)
	ON DELETE SET NULL
	ON UPDATE CASCADE
);
CREATE TABLE Courses (
   id INT PRIMARY KEY IDENTITY,
   name VARCHAR(50) NOT NULL,
   hours INT NOT NULL,
   level_id INT NOT NULL,
   department_id INT NOT NULL,
   FOREIGN KEY (level_id) REFERENCES Levels(id) ON UPDATE CASCADE,
   FOREIGN KEY (department_id) REFERENCES Departments(id) ON UPDATE CASCADE
);
  CREATE TABLE places (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR (50)NOT NULL,
    capacity INT NOT NULL,
    floor INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL,
);
CREATE TABLE StudentsCourses (
    course_id INT ,
    student_id INT ,
	date  DATE ,
    PRIMARY KEY (course_id, student_id,date),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
        ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES Student(id)
        ON DELETE CASCADE
);
CREATE TABLE CoursesPrerequisites (
    course_id INT ,
    prerequisite_id INT ,
    PRIMARY KEY (course_id,Prerequisite_id),
    FOREIGN KEY (course_id) REFERENCES Courses(id),
    FOREIGN KEY (Prerequisite_id) REFERENCES Courses(id)
     
);

CREATE TABLE CoursesProfessors(
   professor_id INT ,
   course_id INT ,
   year VARCHAR(5) ,
   semester INT,
   PRIMARY KEY (professor_id, course_id,year,semester),
   FOREIGN KEY (professor_id) REFERENCES professors(employee_id)
   ON DELETE CASCADE ,
   FOREIGN KEY (course_id) REFERENCES courses(id)
   ON DELETE CASCADE,
);
CREATE TABLE Exams(
   id INT PRIMARY KEY IDENTITY ,
   date DATE NOT NULL,
   type VARCHAR(50) NOT NULL,
   duration VARCHAR(50) NOT NULL,
   course_id INT NOT NULL,
   professor_id INT NOT NULL,
   level_id INT NOT NULL,
   FOREIGN KEY (course_id) REFERENCES courses(id),
   FOREIGN KEY (professor_id) REFERENCES professors(employee_id),
   FOREIGN KEY (level_id) REFERENCES Levels(id)
);
CREATE TABLE StudentExams (
   exam_id INT PRIMARY KEY ,
   student_id INT ,
   status VARCHAR(20),
   grade VARCHAR(2) NOT NULL,
   FOREIGN KEY (student_id) REFERENCES Student(id) 
   ON DELETE CASCADE 
   ON UPDATE CASCADE,
   FOREIGN KEY (exam_id) REFERENCES Exams(id)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
CREATE TABLE Devices (
    id INT IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    last_maintenance DATE NOT NULL,
    company VARCHAR(50) NOT NULL,
    buy_date DATE NOT NULL,
    warranty INT NOT NULL,
    place_id INT,
    FOREIGN KEY (place_id) REFERENCES Places(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE Books (
    id INT IDENTITY PRIMARY KEY,
    year_of_publication INT NOT NULL,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
CREATE TABLE studentScholarship (
    scholarship_id INT ,
    student_id INT,
start_date DATE ,
end_date DATE NOT NULL,

    PRIMARY KEY (scholarship_id, student_id,start_date),
    FOREIGN KEY (scholarship_id) REFERENCES Scholarships(id),
    FOREIGN KEY (student_id) REFERENCES Student(id)
);

CREATE TABLE Lectures (
    course_id INT ,
    place_id INT ,
    day VARCHAR(20) ,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    PRIMARY KEY (course_id, place_id, day),
    FOREIGN KEY (course_id) REFERENCES Courses(id),
    FOREIGN KEY (place_id) REFERENCES Places(id)
);


------------------------------------- DML -------------------------------------
INSERT INTO Departments (name, location, description)
VALUES 
('Computer Science', 'Building A', 'Department focusing on software engineering, algorithms, and AI'),
('Mathematics', 'Building B', 'Department for mathematical theories, calculus, and applied mathematics'),
('Physics', 'Building C', 'Department for studying physical sciences, quantum mechanics, and thermodynamics'),
('Biology', 'Building D', 'Department focusing on molecular biology, genetics, and ecology'),
('Chemistry', 'Building E', 'Department of organic, inorganic, and physical chemistry');

INSERT INTO Employees (name, phone, job_title, hire_date, salary, DOB, email, address, department_id)
VALUES 
('John Doe', '555-1234', 'Professor', '2010-01-01', 50000, '1980-02-15', 'johndoe@example.com', '123 Elm St', 1),
('Jane Smith', '555-5678', 'Administrator', '2015-06-20', 45000, '1990-03-25', 'janesmith@example.com', '456 Oak St', 2),
('Alice Johnson', '555-8765', 'Lecturer', '2018-07-15', 40000, '1985-11-10', 'alicejohnson@example.com', '789 Pine St', 3),
('Bob Lee', '555-3456', 'Technician', '2020-09-05', 35000, '1992-04-30', 'boblee@example.com', '101 Birch St', 4),
('Eva Green', '555-2468', 'Researcher', '2017-12-10', 42000, '1993-07-22', 'evagreen@example.com', '202 Maple St', 5);


INSERT INTO professors (employee_id, researches)
VALUES 
(2, 'Mathematical Theories and Calculus'),
(3, 'Quantum Mechanics and Thermodynamics'),
(4, 'Genetics and Molecular Biology'),
(5, 'Chemical Reactions and Organic Chemistry'),
(6, 'Artificial Intelligence and Machine Learning')


INSERT INTO Levels (name)
VALUES 
('Level 1'),
('Level 2'),
('Level 3'),
('Level 4'),
('Level 5');


INSERT INTO Scholarships ( capacity , name  , rules)
VALUES 
(10, 'AI' , 'Must maintain a GPA of 3.5'),
(5, 'Security' , 'Awarded based on financial need'),
(15, 'Web' , 'Available for STEM majors'),
(8, 'Mobile' , 'Renewable annually based on performance'),
(12, 'Cloud ' , 'For international students only');


INSERT INTO Courses (name, hours, level_id, department_id)
VALUES 
('Introduction to Programming', 3, 1, 1),
('Calculus I', 4, 1, 2),
('General Physics', 3, 2, 3),
('Molecular Biology', 3, 2, 4),
('Organic Chemistry', 3, 3, 5);


INSERT INTO Student (address, gender, name, DOB, phone, email, department_id, level_id, Scholar_id)
VALUES 
('111 Main St', 'Male', 'Michael Brown', '2000-05-10', '555-9876', 'michaelb@example.com', 1, 1, NULL),
('222 High St', 'Female', 'Sophia Wilson', '1999-11-20', '555-6543', 'sophiaw@example.com', 2, 2, 1),
('333 Oak St', 'Male', 'Ethan Clark', '2001-02-15', '555-3210', 'ethanc@example.com', 3, 3, 2),
('444 Pine St', 'Female', 'Olivia Johnson', '2000-09-05', '555-4321', 'oliviaj@example.com', 4, 4, 3),
('555 Birch St', 'Male', 'James Lee', '1998-12-30', '555-8765', 'jamesl@example.com', 5, 5, NULL);


INSERT INTO Places (name, capacity, floor, type, location)
VALUES 
('Lecture Hall A', 100, 1, 'Classroom', 'Building A'),
('Lecture Hall B', 80, 2, 'Classroom', 'Building B'),
('Lab Room 1', 20, 1, 'Laboratory', 'Building C'),
('Auditorium', 200, 3, 'Auditorium', 'Building D'),
('Seminar Room', 30, 1, 'Meeting Room', 'Building E');


INSERT INTO StudentsCourses (course_id, student_id, date)
VALUES 
(1, 1, '2024-01-10'),
(2, 2, '2024-01-15'),
(3, 3, '2024-01-20'),
(4, 4, '2024-01-25'),
(5, 5, '2024-01-30');


INSERT INTO CoursesPrerequisites (course_id, prerequisite_id)
VALUES 
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(1, 2);



INSERT INTO CoursesProfessors (professor_id, course_id, year, semester)
VALUES 
(2, 2, '2024', 1),
(3, 3, '2024', 1),
(4, 4, '2024', 2),
(5, 5, '2024', 2),
(6, 1, '2024', 1)


INSERT INTO Exams (date, type, duration, course_id, professor_id, level_id)
VALUES 
('2024-06-20', 'Midterm', '1.5 hours', 2, 2, 2),
('2024-06-25', 'Final', '2 hours', 3, 3, 2),
('2024-06-30', 'Midterm', '1.5 hours', 4, 4, 3),
('2024-07-05', 'Final', '2 hours', 5, 5, 3),
('2024-06-15', 'Final', '2 hours', 1, 6, 1)


INSERT INTO StudentExams (student_id, exam_id, grade)
VALUES 
(1, 6, 'A'),
(2, 2, 'B'),
(3, 3, 'C'),
(4, 4, 'F'),
(5, 5, 'F');


INSERT INTO Devices (name, last_maintenance, company, buy_date, warranty, place_id)
VALUES 
('Projector', '2024-01-01', 'Samsung', '2020-05-10', 2, 1),
('Computer', '2023-12-15', 'Dell', '2021-03-22', 3, 2),
('Printer', '2024-02-10', 'HP', '2022-07-05', 1, 3),
('Microscope', '2023-11-30', 'Zeiss', '2021-08-19', 5, 4),
('Air Conditioner', '2024-01-20', 'Daikin', '2020-09-01', 2, 5);


INSERT INTO Books (year_of_publication, title, author, course_id)
VALUES 
(2020, 'Programming Basics', 'John Smith', 1),
(2019, 'Advanced Calculus', 'Sarah Brown', 2),
(2021, 'Physics for Engineers', 'David Green', 3),
(2018, 'Molecular Genetics', 'Emily White', 4),
(2022, 'Organic Chemistry Principles', 'Mark Taylor', 5);


INSERT INTO studentScholarship (scholarship_id, student_id, start_date, end_date)
VALUES 
(1, 1, '2024-01-01', '2024-12-31'),
(2, 2, '2024-01-15', '2025-01-15'),
(3, 3, '2024-03-01', '2025-03-01'),
(4, 4, '2024-02-01', '2025-02-01'),
(5, 5, '2024-04-01', '2025-04-01');


INSERT INTO Lectures (course_id, place_id, day, start_time, end_time)
VALUES 
(1, 1, 'Monday', '10:00', '12:00'),
(2, 2, 'Tuesday', '14:00', '16:00'),
(3, 3, 'Wednesday', '09:00', '11:00'),
(4, 4, 'Thursday', '11:00', '13:00'),
(5, 5, 'Friday', '13:00', '15:00');


