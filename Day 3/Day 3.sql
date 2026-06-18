CREATE DATABASE intern_db;
use intern_db;
CREATE TABLE students
(
student_id int primary key,
s_name varchar(255),
age int,
email varchar(255),
course char(255),
phone varchar(15));

INSERT INTO students
(student_id, s_name, age, email, course, phone)
VALUES
(1, 'Aarav Sharma', 19, 'aarav@gmail.com', 'CSE', 987654321),
(2, 'Diya Patel', 20, 'diya@gmail.com', 'AI', 987654322),
(3, 'Arjun Nair', 21, 'arjun@gmail.com', 'ECE', 987654323),
(4, 'Ananya Singh', 22, 'ananya@gmail.com', 'CSE', 987654324),
(5, 'Rahul Verma', 23, 'rahul@gmail.com', 'ME', 987654325),
(6, 'Sneha Reddy', 20, 'sneha@gmail.com', 'AI', 987654326),
(7, 'Karthik Rao', 24, 'karthik@gmail.com', 'CSE', 987654327),
(8, 'Priya Menon', 21, 'priya@gmail.com', 'ECE', 987654328),
(9, 'Vivek Kumar', 25, 'vivek@gmail.com', 'ME', 987654329),
(10, 'Meera Joshi', 22, 'meera@gmail.com', 'AI', 987654330);

SELECT * from students
WHERE age > 20;

UPDATE students SET course = "EEE" where student_id = 3;

delete from students where student_id = 10;

select count(*) as "Number of Students" from students;

