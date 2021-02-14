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
        SUM(Frequency) OVER(Order by Number ASC) frq_lower,
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
