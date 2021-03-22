'''
Higher Link: https://www.linkedin.com/posts/eric-weber-060397b7_data-datascience-sql-activity-6765982620477128704-7h2x
Actual Link: https://lnkd.in/g3c5JGC
SQL (Easy-level) Questions from Leetcode
'''

`Problem: Second Highest Salary
Task: Write a SQL query to get the second highest salary from the Employee table. If there is no second highest salary, then the query should return null.
Employee
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
`
SELECT (
  SELECT DISTINCT
    Salary
  FROM
    Employee
  ORDER BY SALARY DESC
  LIMIT 1, 1 -- LIMIT 1 OFFSET 1
) AS SecondHighestSalary
;

`Problem: Combine Two Tables
Task: Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
`
SELECT
	p.FirstName,
  p.LastName,
	a.City,
	a.State
FROM
	Person p
	LEFT JOIN
	Address a
	USING (PersonId)
;

`Problem: Delete Duplicate Emails
Task: Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
Person
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
`
-- Approach 1 (Join)
DELETE p1 FROM
  Person p1,
  Person p2
WHERE
  p1.Email = p2.Email
  AND p1.Id > p2.Id;

-- Approach 2 (Faster: 2x)
with deletable_id AS (
  SELECT
    MIN(Id) Id
  FROM
    Person
  GROUP BY
    Email
)
DELETE FROM
  Person
WHERE Id NOT IN (SELECT Id From deletable_id)
;

`Problem:
Task:
`
`Problem: Employees Earning More Than Their Managers
Task: The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id. Given the Employee table, write a SQL query that finds out employees who earn more than their managers.
`
SELECT
  e.Name Employee
FROM
  Employee e,
  Employee m
WHERE
  e.ManagerId = m.Id
  AND e.Salary > m.Salary;

`Problem: Swap boolean values
Task: Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temp table(s).
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
Result table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
`
UPDATE Salary
SET
    sex = IF(sex='m', 'f', 'm')
;

`Problem: Triangle Judgement
Task: writing a query to judge if these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
`
SELECT
    *,
    IF(x + y > z, IF(y + z > x, IF(z + x > y, 'Yes', 'No'), 'No'), 'No') triangle
FROM
    triangle;

`Problem: Pivot Table View
Task: Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
`
SELECT
	id,
	SUM(IF(month='Jan', revenue, NULL)) 'Jan_Revenue',
	SUM(IF(month='Feb', revenue, NULL)) 'Feb_Revenue',
	SUM(IF(month='Mar', revenue, NULL)) 'Mar_Revenue',
	SUM(IF(month='Apr', revenue, NULL)) 'Apr_Revenue',
	SUM(IF(month='May', revenue, NULL)) 'May_Revenue',
	SUM(IF(month='Jun', revenue, NULL)) 'Jun_Revenue',
	SUM(IF(month='Jul', revenue, NULL)) 'Jul_Revenue',
	SUM(IF(month='Aug', revenue, NULL)) 'Aug_Revenue',
	SUM(IF(month='Sep', revenue, NULL)) 'Sep_Revenue',
	SUM(IF(month='Oct', revenue, NULL)) 'Oct_Revenue',
	SUM(IF(month='Nov', revenue, NULL)) 'Nov_Revenue',
	SUM(IF(month='Dec', revenue, NULL)) 'Dec_Revenue'
FROM
	Department
GROUP BY
	id
ORDER BY
	id
;

`Problem: Find Users With Valid E-Mails
Task: Write an SQL query to find the users who have valid emails. A valid e-mail has a prefix name and a domain where:
The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.' and/or dash '-'. The prefix name must start with a letter. The domain is '@leetcode.com'.
Users
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
`
SELECT
  *
FROM
  Users
WHERE
  mail REGEXP '^[A-Za-z0-9]+[A-Za-z0-9_.*]@leetcode\.com$'
ORDER BY
  user_id;

`Problem: Rising Temperature
Task: Write an SQL query to find all dates' id with higher temperature compared to its previous dates (yesterday).
`
-- Using Window Function
WITH windowed_aggregation AS (
	SELECT
		*,
		(LAG(recordDate, 1) OVER(ORDER BY recordDate)) previousDay,
		(LAG(Temperature, 1) OVER(ORDER BY recordDate)) previousTemperature
	FROM
		Weather
	)
SELECT
    id
FROM
    windowed_aggregation
WHERE
    DATEDIFF(recordDate, previousDay) = 1
    AND Temperature > previousTemperature;

-- Using Join
SELECT
    w1.id
FROM
    Weather w1
    JOIN
    Weather w2
    ON (
        DATEDIFF(w1.recordDate, w2.recordDate) = 1
        AND w1.temperature > w2.temperature
    )
ORDER BY
    id
;

`Problem: All Valid Triplets That Can Represent a Country
Task: Write an SQL query to find all the possible triplets representing the country under the given constraints.
SchoolA table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
+------------+--------------+
SchoolB table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
+------------+--------------+
SchoolC table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 3          | Tom          |
| 2          | Jerry        |
| 10         | Alice        |
+------------+--------------+
Result table:
+----------+----------+----------+
| member_A | member_B | member_C |
+----------+----------+----------+
| Alice    | Tom      | Jerry    |
| Bob      | Tom      | Alice    |
+----------+----------+----------+
`
SELECT
    a.student_name member_A,
    b.student_name member_B,
    c.student_name member_C
FROM
    SchoolA a,
    SchoolB b,
    SchoolC c
WHERE
    a.student_id <> b.student_id
    AND b.student_id <> c.student_id
    AND a.student_id <>  c.student_id
    AND a.student_name <> b.student_name
    AND b.student_name <> c.student_name
    AND a.student_name <> c.student_name
;
`Problem: Immediate Food Delivery I
Task: If the preferred delivery date of the customer is the same as the order date then the order is called immediate otherwise it's called scheduled. Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+
Result table:
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
The orders with delivery id 2 and 3 are immediate while the others are scheduled.
`
SELECT
    ROUND(SUM(IF(customer_pref_delivery_date = order_date, 1, 0))*100/COUNT(*), 2) immediate_percentage
FROM
    Delivery
;

`Problem: Consecutive Available Seats
Task: Several friends at a cinema ticket office would like to reserve consecutive available seats.
Can you help to query all the consecutive available seats order by the seat_id using the following cinema table?
| seat_id | free |
|---------|------|
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
Your query should return the following result for the sample case above.
| seat_id |
|---------|
| 3       |
| 4       |
| 5       |
`
SELECT DISTINCT
    c1.seat_id
FROM
    cinema c1,
    cinema c2
WHERE
    abs(c1.seat_id - c2.seat_id) = 1
    AND c1.free = 1
    AND c2.free = 1
ORDER BY
    seat_id
;

`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
`Problem:
Task:
`
