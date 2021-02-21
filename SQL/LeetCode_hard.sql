'''
Link: https://leetcode.com/problemset/database/?listId=5htp6xyg&difficulty=Hard
'''

`Problem: Find Median Given Frequency of Numbers
Task: Write a query to find the median of all numbers and name the result as median.
The Numbers table keeps the value of number and its frequency.
+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.
+--------+
| median |
+--------|
| 0.0000 |
+--------+
`
WITH tmp_frame AS (
    SELECT
        Number, Frequency,
        SUM(Frequency) OVER(Order by Number) frq_lower,
        SUM(Frequency) OVER(Order by Number DESC) frq_higher
    FROM Numbers
)

SELECT AVG(Number) AS median
FROM tmp_frame
WHERE Frequency >= ABS(frq_lower - frq_higher);

`Problem: Average Salary: Departments VS Company
Task: Given two tables as below, write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.
able: salary
            | id | employee_id | amount | pay_date   |
            |----|-------------|--------|------------|
            | 1  | 1           | 9000   | 2017-03-31 |
            | 2  | 2           | 6000   | 2017-03-31 |
            | 3  | 3           | 10000  | 2017-03-31 |
            | 4  | 1           | 7000   | 2017-02-28 |
            | 5  | 2           | 6000   | 2017-02-28 |
            | 6  | 3           | 8000   | 2017-02-28 |
The employee_id column refers to the employee_id in the following table employee.
            | employee_id | department_id |
            |-------------|---------------|
            | 1           | 1             |
            | 2           | 2             |
            | 3           | 2             |
So for the sample data above, the result is:
            | pay_month | department_id | comparison  |
            |-----------|---------------|-------------|
            | 2017-03   | 1             | higher      |
            | 2017-03   | 2             | lower       |
            | 2017-02   | 1             | same        |
            | 2017-02   | 2             | same        |
`

SELECT
    DISTINCT pay_month, department_id,
    (CASE
        WHEN department_avg_salary = company_avg_salary THEN 'same'
        WHEN department_avg_salary > company_avg_salary THEN 'higher'
        ELSE 'lower'
    END) AS comparison
FROM(
    SELECT
        s.employee_id, s.pay_date, s.amount, e.department_id AS department_id,
        LEFT(s.pay_date, 7) AS pay_month,
        AVG(s.amount) OVER(PARTITION BY s.pay_date) AS company_avg_salary,
        AVG(s.amount) OVER(PARTITION BY s.pay_date, e.department_id) AS department_avg_salary
    FROM salary s JOIN employee e
    ON s.employee_id = e.employee_id
) processed;

` Second Way: `
with department_summary AS (
  SELECT
    e.department_id department_id,
    LEFT(s.pay_date, 7) pay_month,
    AVG(s.amount) OVER(PARTITION BY s.pay_date) AS company_avg_salary,
    AVG(s.amount) OVER(PARTITION BY s.pay_date, e.department_id) AS department_avg_salary,
  FROM
    salary s JOIN employee e
    ON (s.employee_id = e.employee_id)
)
SELECT
  pay_month,
  department_id,
  CASE
    WHEN department_avg_salary > company_avg_salary THEN 'higher'
    WHEN department_avg_salary < company_avg_salary THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM
  department_summary
ORDER BY
  pay_month

`Problem: Game Play Analysis V
Task: Write an SQL query that reports for each install date, the number of players that installed the game on that day and the day 1 retention.
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-01 | 0            |
| 3         | 4         | 2016-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+------------+----------+----------------+
| install_dt | installs | Day1_retention |
+------------+----------+----------------+
| 2016-03-01 | 2        | 0.50           |
| 2017-06-25 | 1        | 0.00           |
+------------+----------+----------------+
Player 1 and 3 installed the game on 2016-03-01 but only player 1 logged back in on 2016-03-02 so the day 1 retention of 2016-03-01 is 1 / 2 = 0.50
Player 2 installed the game on 2017-06-25 but didn't log back in on 2017-06-26 so the day 1 retention of 2017-06-25 is 0 / 1 = 0.00
`

SELECT
    install_dt,
    COUNT(DISTINCT current.player_id) AS installs,
    ROUND(SUM(CASE WHEN next.event_date IS NOT NULL THEN 1 ELSE 0 END)/ COUNT(DISTINCT current.player_id), 2) AS Day1_retention
FROM
    (SELECT player_id, MIN(event_date) AS install_dt FROM Activity GROUP BY player_id) current
LEFT JOIN Activity next
ON (current.player_id = next.player_id AND current.install_dt + 1 = next.event_date)
GROUP BY install_dt;

`Problem: Get the Second Most Recent Activity
Task: Write an SQL query to show the second most recent activity of each user. If the user only has one activity, return that one. A user can't perform more than one activity at the same time. Return the result table in any order.
UserActivity table:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Travel       | 2020-02-12  | 2020-02-20  |
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Alice      | Travel       | 2020-02-24  | 2020-02-28  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
Result table:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
The most recent activity of Alice is Travel from 2020-02-24 to 2020-02-28, before that she was dancing from 2020-02-21 to 2020-02-23. Bob only has one record, we just take that one.
`

WITH processed AS (
    SELECT
        *,
        COUNT(activity) OVER (PARTITION BY username) AS activity_cnt,
        DENSE_RANK() OVER(PARTITION BY username ORDER BY startDate DESC) AS rnk
    FROM useractivity
)
SELECT username, activity, startdate, enddate
FROM processed
WHERE activity_cnt = 1 or rnk = 2;

`Problem: Trips and Users
Task: Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.Return the result table in any order. Round Cancellation Rate to two decimal points.
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| Id | Client_Id | Driver_Id | City_Id | Status              | Request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+

Users table:
+----------+--------+--------+
| Users_Id | Banned | Role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+

Result table:
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
`
with day_summary AS (
    SELECT
        t.Request_at Day,
        COUNT(t.Id) total_trips,
        COUNT(IF(t.Status = 'completed', 1, NULL)) completed_trips
    FROM
        Trips t
        JOIN
        Users u
        ON (
            t.Client_Id = u.Users_Id
            )
    WHERE
        t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
        AND
        u.Role IN ('client', 'driver')
        AND
        u.Banned = 'No'
    GROUP BY
        t.Request_at
)

SELECT
    Day,
    IF(total_trips > 0, ROUND((total_trips - completed_trips) / total_trips, 2), 0) `Cancellation Rate`
FROM
    day_summary
ORDER BY
    Day

`Without CET`
(76% over 10%!!)
SELECT
    t.Request_at Day,
    IF(COUNT(t.Id) > 0, ROUND((1 - COUNT(IF(t.Status = 'completed', 1, NULL))/COUNT(t.Id)), 2), 0) `Cancellation Rate`
FROM
    Trips t JOIN Users u ON (t.Client_Id = u.Users_Id)
WHERE
    t.Request_at BETWEEN '2013-10-01' AND '2013-10-03' AND u.Role IN ('client', 'driver') AND u.Banned = 'No'
GROUP BY t.Request_at
ORDER BY Day


`Problem: Human Traffic of Stadium
Task: Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each. Return the result table ordered by visit_date in ascending order.
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
`
SELECT DISTINCT
    l1.*
FROM
    Stadium l1, Stadium l2, Stadium l3
WHERE
    l1.people > 99 AND l2.people > 99 AND l3.people > 99
    AND (
        (l1.id + 1 = l2.id AND l2.id + 1 = l3.id)  -- l1, l2, l3
        OR
        (l2.id + 1 = l1.id AND l1.id + 1 = l3.id) -- l2, l1, l3
        OR
        (l3.id + 1 = l2.id AND l2.id + 1 = l1.id) -- l3, l2, l1
    )
ORDER BY
    visit_date;


`Problem: Department Top Three Salaries
Task: Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows (order of rows does not matter).
The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
`
with employee_cte AS (
    SELECT
        d.Name Department, e.Name Employee, e.Salary Salary,
        DENSE_RANK() OVER(PARTITION BY d.Name ORDER BY e.Salary DESC) AS dep_rank
    FROM
        Employee e
        JOIN
        Department d
        ON ( e.DepartmentId = d.Id)
)
SELECT
    Department,
    Employee,
    Salary
FROM
    employee_cte
WHERE
    dep_rank <= 3;

`Problem: Sales by Day of the Week
Task: Write an SQL query to report how many units in each category have been ordered on each day of the week.
Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| order_date    | date    |
| item_id       | varchar |
| quantity      | int     |
+---------------+---------+
(ordered_id, item_id) is the primary key for this table.
This table contains information of the orders placed.
order_date is the date when item_id was ordered by the customer with id customer_id.
Table: Items
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| item_id             | varchar |
| item_name           | varchar |
| item_category       | varchar |
+---------------------+---------+
item_id is the primary key for this table.
item_name is the name of the item.
item_category is the category of the item.
`
WITH processed_orders AS (
    SELECT
        i.item_category Category,
        DAYOFWEEK(o.order_date) AS day_of_week,
        o.quantity quantity
    FROM
        Items i
        LEFT JOIN
        Orders o
        ON (i.item_id = o.item_id)
)
SELECT
    Category,
    SUM(IF(day_of_week=2, quantity, 0)) AS Monday,
    SUM(IF(day_of_week=3, quantity, 0)) AS Tuesday,
    SUM(IF(day_of_week=4, quantity, 0)) AS Wednesday,
    SUM(IF(day_of_week=5, quantity, 0)) AS Thursday,
    SUM(IF(day_of_week=6, quantity, 0)) AS Friday,
    SUM(IF(day_of_week=7, quantity, 0)) AS Saturday,
    SUM(IF(day_of_week=1, quantity, 0)) AS Sunday
FROM
    processed_orders
GROUP BY
    Category
ORDER BY
    Category;


`Problem: Find the Quiet Students in All Exams
Task: A "quite" student is the one who took at least one exam and didn't score neither the high score nor the low score. Write an SQL query to report the students (student_id, student_name) being "quiet" in ALL exams. Don't return the student who has never taken any exam. Return the result table ordered by student_id.
Student table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
+-------------+---------------+
Exam table:
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
+------------+--------------+-----------+
Result table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+
`

with exam_processed AS (
    SELECT
        s.student_id student_id,
        s.student_name student_name,
        e.score score,
        RANK() OVER(PARTITION BY exam_id ORDER BY score) min_rank,
        RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) max_rank
    FROM
        Exam e LEFT JOIN Student s
        ON (e.student_id = s.student_id)
)
SELECT DISTINCT
    student_id,
    student_name
FROM
    exam_processed
WHERE
    student_id NOT IN (select distinct student_id FROM exam_processed WHERE min_rank = 1 OR max_rank = 1)
ORDER BY
    student_id;

`Problem: Median Employee Salary
Task: Write a SQL query to find the median salary of each company. Bonus points if you can solve it without using any built-in SQL functions.
The Employee table holds all employees. The employee table has three columns: Employee Id, Company Name, and Salary.
+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+
`
WITH median_salaries AS (
    SELECT
        Id, Company, Salary,
        ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary) AS salary_ranked,
        COUNT(Id) OVER(PARTITION BY Company) AS total
    FROM
        Employee
)
SELECT
    Id, Company, Salary
FROM
    median_salaries
WHERE
    salary_ranked BETWEEN total/2 AND total/2 + 1;

`Problem: Find Cumulative Salary of an Employee
Task: The Employee table holds the salary information in a year. Write a SQL to get the cumulative sum of an employee's salary over a period of 3 months but exclude the most recent month.
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
`
with processed_employee AS (
    SELECT
        Id, Month,
        SUM(Salary) OVER(PARTITION BY Id ORDER BY MONTH ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) Salary,
        ROW_NUMBER() OVER(PARTITION BY Id ORDER BY MONTH DESC) AS row_id
    FROM
        Employee
)

SELECT
    Id, Month, Salary
FROM
   processed_employee
WHERE
    row_id != 1
ORDER BY Id, Month DESC;

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
