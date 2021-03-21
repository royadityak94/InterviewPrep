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

`Problem: Hopper Company Queries I
Task: Write an SQL query to report the following statistics for each month of 2020:
The number of drivers currently with the Hopper company by the end of the month (active_drivers). The number of accepted rides in that month (accepted_rides). Return the result table ordered by month in ascending order, where month is the month's number (January is 1, February is 2, etc.).
Drivers table:
+-----------+------------+
| driver_id | join_date  |
+-----------+------------+
| 10        | 2019-12-10 |
| 8         | 2020-1-13  |
| 5         | 2020-2-16  |
| 7         | 2020-3-8   |
| 4         | 2020-5-17  |
| 1         | 2020-10-24 |
| 6         | 2021-1-5   |
+-----------+------------+

Rides table:
+---------+---------+--------------+
| ride_id | user_id | requested_at |
+---------+---------+--------------+
| 6       | 75      | 2019-12-9    |
| 1       | 54      | 2020-2-9     |
| 10      | 63      | 2020-3-4     |
| 19      | 39      | 2020-4-6     |
| 3       | 41      | 2020-6-3     |
| 13      | 52      | 2020-6-22    |
| 7       | 69      | 2020-7-16    |
| 17      | 70      | 2020-8-25    |
| 20      | 81      | 2020-11-2    |
| 5       | 57      | 2020-11-9    |
| 2       | 42      | 2020-12-9    |
| 11      | 68      | 2021-1-11    |
| 15      | 32      | 2021-1-17    |
| 12      | 11      | 2021-1-19    |
| 14      | 18      | 2021-1-27    |
+---------+---------+--------------+

AcceptedRides table:
+---------+-----------+---------------+---------------+
| ride_id | driver_id | ride_distance | ride_duration |
+---------+-----------+---------------+---------------+
| 10      | 10        | 63            | 38            |
| 13      | 10        | 73            | 96            |
| 7       | 8         | 100           | 28            |
| 17      | 7         | 119           | 68            |
| 20      | 1         | 121           | 92            |
| 5       | 7         | 42            | 101           |
| 2       | 4         | 6             | 38            |
| 11      | 8         | 37            | 43            |
| 15      | 8         | 108           | 82            |
| 12      | 8         | 38            | 34            |
| 14      | 1         | 90            | 74            |
+---------+-----------+---------------+---------------+

Result table:
+-------+----------------+----------------+
| month | active_drivers | accepted_rides |
+-------+----------------+----------------+
| 1     | 2              | 0              |
| 2     | 3              | 0              |
| 3     | 4              | 1              |
| 4     | 4              | 0              |
| 5     | 5              | 0              |
| 6     | 5              | 1              |
| 7     | 5              | 1              |
| 8     | 5              | 1              |
| 9     | 5              | 0              |
| 10    | 6              | 0              |
| 11    | 6              | 2              |
| 12    | 6              | 1              |
+-------+----------------+----------------+
`

WITH RECURSIVE months(month) AS (
    SELECT 1 month
    UNION ALL
    SELECT month+1 FROM months WHERE month < 12
),
driver_stats AS (
    SELECT
        month(join_date) month,
        COUNT(driver_id) OVER(ORDER BY join_date) active_drivers
    FROM
        drivers
    WHERE
        year(join_date) <= 2020
),
rider_stats AS (
    SELECT
        month(requested_at) month,
        COUNT(ride_id) accepted_rides
    FROM
        Rides
    WHERE
        ride_id IN (SELECT DISTINCT ride_id FROM AcceptedRides)
        AND
        year(requested_at) = 2020
    GROUP BY
        month
)
SELECT DISTINCT
    m.month,
    IFNULL(MAX(ds.active_drivers) OVER(ORDER BY m.month), 0) active_drivers,
    IFNULL(rs.accepted_rides, 0) accepted_rides
FROM
    months m
    LEFT JOIN driver_stats ds ON (m.month = ds.month)
    LEFT JOIN rider_stats rs ON (m.month = rs.month)
;

`Problem: Hopper Company Queries III
Task: Write an SQL query to compute the average_ride_distance and average_ride_duration of every 3-month window starting from January - March 2020 to October - December 2020. Round average_ride_distance and average_ride_duration to the nearest two decimal places.
Result table:
+-------+-----------------------+-----------------------+
| month | average_ride_distance | average_ride_duration |
+-------+-----------------------+-----------------------+
| 1     | 21.00                 | 12.67                 |
| 2     | 21.00                 | 12.67                 |
| 3     | 21.00                 | 12.67                 |
| 4     | 24.33                 | 32.00                 |
| 5     | 57.67                 | 41.33                 |
| 6     | 97.33                 | 64.00                 |
| 7     | 73.00                 | 32.00                 |
| 8     | 39.67                 | 22.67                 |
| 9     | 54.33                 | 64.33                 |
| 10    | 56.33                 | 77.00                 |
+-------+-----------------------+-----------------------+
`
WITH RECURSIVE months(month) AS (
  SELECT 1
  UNION ALL
  SELECT month + 1 FROM months WHERE month < 12
),

ride_summary AS (
  SELECT
    month(r.requested_at) month,
    SUM(ar.ride_distance) month_ride_distance,
    SUM(ar.ride_duration) monthly_ride_duration
  FROM
    Rides r
    JOIN AcceptedRides ar
    ON (r.ride_id = ar.ride_id)
    WHERE year(r.requested_at) = '2020'
    GROUP BY month
)

SELECT
  m.month month,
  ROUND(AVG(CAST(IFNULL(rs.month_ride_distance, 0) AS FLOAT)) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) average_ride_distance,
  ROUND(AVG(CAST(IFNULL(rs.monthly_ride_duration, 0) AS FLOAT)) OVER(ORDER BY month ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING), 2) average_ride_duration
FROM
  months m
  LEFT JOIN
  ride_summary rs
    ON (m.month = rs.month)
ORDER BY
  month
LIMIT 10;

`Problem: Hopper Company Queries II
Task: Write an SQL query to report the percentage of working drivers (working_percentage) for each month of 2020
Result table:
+-------+--------------------+
| month | working_percentage |
+-------+--------------------+
| 1     | 0.00               |
| 2     | 0.00               |
| 3     | 25.00              |
| 4     | 0.00               |
| 5     | 0.00               |
| 6     | 20.00              |
| 7     | 20.00              |
| 8     | 20.00              |
| 9     | 0.00               |
| 10    | 0.00               |
| 11    | 33.33              |
| 12    | 16.67              |
+-------+--------------------+
`

WITH RECURSIVE months(month) AS (
  SELECT 1 month
  UNION ALL
  SELECT month+1 FROM months WHERE month < 12
),

driver_infomation AS (
  SELECT
    month(join_date) month,
    count(driver_id) OVER(ORDER BY join_date ROWS UNBOUNDED PRECEDING) active_drivers
  FROM
    drivers
  WHERE
    year(join_date) <= 2020
),

available_drivers AS (
  SELECT
    m.month,
    IFNULL(MAX(di.active_drivers) OVER(ORDER BY month), 0) active_drivers
  FROM
    months m
    LEFT JOIN
    driver_infomation di
    ON (m.month = di.month)
),

working_drivers AS (
  SELECT
    month(r.requested_at) month,
    COUNT(DISTINCT driver_id) working_drivers
  FROM
    Rides r
    JOIN AcceptedRides ar
    ON (r.ride_id = ar.ride_id)
    WHERE year(r.requested_at) = 2020
    GROUP BY month
)

SELECT
  m.month month,
  IFNULL(ROUND(working_drivers/active_drivers*100, 2), 0) working_percentage
FROM
  months m
  LEFT JOIN available_drivers ad ON (ad.month = m.month)
  LEFT JOIN working_drivers wd ON (wd.month = m.month)
GROUP BY
  month
;

`Problem: Find the Subtasks That Did Not Execute
Task: Write an SQL query to report the IDs of the missing subtasks for each task_id.
Tasks table:
+---------+----------------+
| task_id | subtasks_count |
+---------+----------------+
| 1       | 3              |
| 2       | 2              |
| 3       | 4              |
+---------+----------------+
Executed table:
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 2          |
| 3       | 1          |
| 3       | 2          |
| 3       | 3          |
| 3       | 4          |
+---------+------------+
Result table:
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 1          |
| 1       | 3          |
| 2       | 1          |
| 2       | 2          |
+---------+------------+
`
WITH RECURSIVE task_listing AS (
  SELECT task_id, 1 subtask_id, subtasks_count FROM Tasks
  UNION ALL
  SELECT task_id, subtask_id + 1 AS subtask_id, subtasks_count FROM task_listing
    WHERE subtask_id < (SELECT MAX(subtasks_count) FROM Tasks)
)

SELECT
  tl.task_id task_id,
  tl.subtask_id subtask_id
FROM
  task_listing tl
  LEFT JOIN Executed e
  ON (tl.task_id = e.task_id AND tl.subtask_id = e.subtask_id)
  WHERE
    e.subtask_id IS NULL
    AND
    tl.subtasks_count >= tl.subtask_id
;
`
N.B: We have to do tl.subtasks_count >= tl.subtask_id because earlier we had generated as much
subtask_id as MAX(subtasks_count). WE could have done: WHERE subtask_id < subtasks_count. However, that would have been
much more expensive and imfeasible (almost 2x speedup). But, if we did, we do not have to include:
tl.subtasks_count >= tl.subtask_id in our where clause!!!
`

`Problem: Transactions across Visits (Confusing Requirement)
Task: Transaction count aggregation across user visits
Source: https://leetcode.com/problems/number-of-transactions-per-visit/
Visits table:
+---------+------------+
| user_id | visit_date |
+---------+------------+
| 1       | 2020-01-01 |
| 2       | 2020-01-02 |
| 12      | 2020-01-01 |
| 19      | 2020-01-03 |
| 1       | 2020-01-02 |
| 2       | 2020-01-03 |
| 1       | 2020-01-04 |
| 7       | 2020-01-11 |
| 9       | 2020-01-25 |
| 8       | 2020-01-28 |
+---------+------------+
Transactions table:
+---------+------------------+--------+
| user_id | transaction_date | amount |
+---------+------------------+--------+
| 1       | 2020-01-02       | 120    |
| 2       | 2020-01-03       | 22     |
| 7       | 2020-01-11       | 232    |
| 1       | 2020-01-04       | 7      |
| 9       | 2020-01-25       | 33     |
| 9       | 2020-01-25       | 66     |
| 8       | 2020-01-28       | 1      |
| 9       | 2020-01-25       | 99     |
+---------+------------------+--------+
Result table:
+--------------------+--------------+
| transactions_count | visits_count |
+--------------------+--------------+
| 0                  | 4            |
| 1                  | 5            |
| 2                  | 0            |
| 3                  | 1            |
+--------------------+--------------+
`
WITH user_visits AS (
    SELECT
        v.user_id user_id,
        visit_date,
        COUNT(t.transaction_date) transaction_count
    FROM
        Visits v
    LEFT JOIN
        Transactions t
    ON
        v.user_id = t.user_id
        AND
        v.visit_date = t.transaction_date
    GROUP BY
        1, 2
),
row_nums AS (
    SELECT
        ROW_NUMBER() OVER() rn
    FROM
        Transactions
    UNION
        SELECT 0
)

SELECT
    row_nums.rn transactions_count,
    COUNT(user_visits.transaction_count) visits_count
FROM
    row_nums
    LEFT JOIN
    user_visits
    ON
        transaction_count = rn
WHERE
    rn <= (SELECT max(transaction_count) FROM user_visits)
GROUP BY
    rn
ORDER BY
    1
;

`Problem: Total Sales Amount by Year
Task: Write an SQL query to report the Total sales amount of each item for each year, with corresponding product name, product_id, product_name and report_year. Dates of the sales years are between 2018 to 2020. Return the result table ordered by product_id and report_year.
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | LC Phone     |
| 2          | LC T-Shirt   |
| 3          | LC Keychain  |
+------------+--------------+
Sales table:
+------------+--------------+-------------+---------------------+
| product_id | period_start | period_end  | average_daily_sales |
+------------+--------------+-------------+---------------------+
| 1          | 2019-01-25   | 2019-02-28  | 100                 |
| 2          | 2018-12-01   | 2020-01-01  | 10                  |
| 3          | 2019-12-01   | 2020-01-31  | 1                   |
+------------+--------------+-------------+---------------------+
Result table:
+------------+--------------+-------------+--------------+
| product_id | product_name | report_year | total_amount |
+------------+--------------+-------------+--------------+
| 1          | LC Phone     |    2019     | 3500         |
| 2          | LC T-Shirt   |    2018     | 310          |
| 2          | LC T-Shirt   |    2019     | 3650         |
| 2          | LC T-Shirt   |    2020     | 10           |
| 3          | LC Keychain  |    2019     | 31           |
| 3          | LC Keychain  |    2020     | 31           |
+------------+--------------+-------------+--------------+
`
-- Master Calendar - across min start date, max end date
WITH RECURSIVE daily_sales AS (
  SELECT MIN(period_start) report_date FROM Sales
  UNION
  SELECT DATE_ADD(report_date, INTERVAL 1 DAY) report_date FROM daily_sales
  WHERE report_date <= ALL (SELECT MAX(period_end) FROM Sales)
)

SELECT
  s.product_id,
  p.product_name,
  CAST(year(ds.report_date) AS NCHAR) report_year,
  SUM(s.average_daily_sales) total_amount
FROM
  Sales s
JOIN
  Product p
  ON (s.product_id = p.product_id)
JOIN
  daily_sales ds
  ON (ds.report_date BETWEEN s.period_start AND s.period_end)
GROUP BY
  1, 2, 3
ORDER BY
  1, 2, 3
;

`Problem: Market Analysis II
Task: Report if the second item sold by a seller, is his favorite item.
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2019-01-01 | Lenovo         |
| 2       | 2019-02-09 | Samsung        |
| 3       | 2019-01-19 | LG             |
| 4       | 2019-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2019-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2019-08-04 | 1       | 4        | 2         |
| 5        | 2019-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
Result table:
+-----------+--------------------+
| seller_id | 2nd_item_fav_brand |
+-----------+--------------------+
| 1         | no                 |
| 2         | yes                |
| 3         | yes                |
| 4         | no                 |
+-----------+--------------------+
`
WITH ranked_orders AS (
  SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY seller_id ORDER BY order_date) transaction_rank
  FROM
    Orders
),
transaction_details AS (
  SELECT
    ro.seller_id,
    i.item_brand
  FROM
    ranked_orders ro
    LEFT JOIN
    Items i
    ON (ro.item_id = i.item_id)
  WHERE
    ro.transaction_rank = 2
)
SELECT
  u.user_id seller_id,
  COALESCE(IF(td.item_brand = u.favorite_brand, 'yes', NULL), 'no') 2nd_item_fav_brand
FROM
  Users u
  LEFT JOIN
  transaction_details td
  ON (u.user_id = td.seller_id)
ORDER BY
  1
;

`Problem: Report Contiguous Dates
Task: Write an SQL query to generate a report of period_state for each continuous interval of days in the period from 2019-01-01 to 2019-12-31.
period_state is 'failed' if tasks in this interval failed or 'succeeded' if tasks in this interval succeeded. Interval of days are retrieved as start_date and end_date. Order result by start_date.
Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+
Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+
Result table:
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+
`
WITH aggregated_view AS (
    SELECT
        fail_date reporting_date,
        'failed' period_state,
        DAYOFYEAR(fail_date) - ROW_NUMBER() OVER(ORDER BY fail_date) AS period_group
    FROM
        Failed
    WHERE
        fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION
    SELECT
        success_date reporting_date,
        'succeeded' period_state,
        DAYOFYEAR(success_date) - ROW_NUMBER() OVER(ORDER BY success_date) AS period_group
    FROM
        Succeeded
    WHERE
        success_date BETWEEN '2019-01-01' AND '2019-12-31'
)
SELECT
    period_state,
    MIN(reporting_date) start_date,
    MAX(reporting_date) end_date
FROM
    aggregated_view
GROUP BY
    period_state, period_group
ORDER BY
    start_date
;


`Problem: Students Report By Geography (Pivot Table)
Task: Pivot the continent column in this table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia and Europe respectively. It is guaranteed that the student number from America is no less than either Asia or Europe.
student
| name   | continent |
|--------|-----------|
| Jack   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jane   | America   |
output:
| America | Asia | Europe |
|---------|------|--------|
| Jack    | Xi   | Pascal |
| Jane    |      |        |
`
WITH ranked_student AS (
  SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) ordering
  FROM
    student
)
SELECT
  MAX(CASE WHEN continent = 'America' THEN name END) America,
  MAX(CASE WHEN continent = 'Asia' THEN name END) Asia,
  MAX(CASE WHEN continent = 'Europe' THEN name END) Europe
FROM
  ranked_student
GROUP BY
  ordering


`Problem: Follow-up Question [Students Report By Geography]
Task: If it is unknown which continent has the most students, can you write a query to generate the student report?
Answer Source: https://leetcode.com/problems/students-report-by-geography/discuss/672308/(_)-MySQL-Solutions%3A-WINDOW-variables-(Follow-up-answer)
`
SELECT
        CASE WHEN continent = 'America' THEN @r1 := @r1 + 1
             WHEN continent = 'Asia'    THEN @r2 := @r2 + 1
             WHEN continent = 'Europe'  THEN @r3 := @r3 + 1 END row_id,
        CASE WHEN continent = 'America' THEN name END America,
        CASE WHEN continent = 'Asia'    THEN name END Asia,
        CASE WHEN continent = 'Europe'  THEN name END Europe
FROM student, (SELECT @r1 := 0, @r2 := 0, @r3 := 0) tmp
ORDER BY name

`Problem: User Purchase Platform
Task: Write an SQL query to find the total number of users and the total amount spent using mobile only, desktop only and both mobile and desktop together for each date.
Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+
Result table:
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+
`
WITH master_calendar AS (
  SELECT DISTINCT spend_date, 'desktop' platform FROM Spending
  UNION
  SELECT DISTINCT spend_date, 'mobile' platform FROM Spending
  UNION
  SELECT DISTINCT spend_date, 'both' platform FROM Spending
),
processed_spending AS (
  SELECT
    user_id,
    spend_date,
    IF(mobile_amount > 0, IF(desktop_amount > 0, 'both', 'mobile'), 'desktop') platform,
    (mobile_amount + desktop_amount) amount
  FROM (
    SELECT
      user_id,
      spend_date,
      SUM(CASE WHEN platform='mobile' THEN amount ELSE 0 END) mobile_amount,
      SUM(CASE WHEN platform='desktop' THEN amount ELSE 0 END) desktop_amount
    FROM
      Spending
    GROUP BY
      user_id, spend_date
  ) t
)
SELECT
  mc.spend_date,
  mc.platform,
  IFNULL(SUM(ps.amount), 0) total_amount,
  COUNT(ps.user_id) total_users
FROM
  master_calendar mc
LEFT JOIN
  processed_spending ps
  ON (
    mc.spend_date = ps.spend_date
    AND
    mc.platform = ps.platform
  )
GROUP BY
  spend_date, platform
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
