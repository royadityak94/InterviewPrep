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
with processed_median AS (
  SELECT
    Number, Frequency,
    SUM(Frequency) OVER(ORDER BY Number) lFreq,
    SUM(Frequency) OVER(ORDER BY Number DESC) rFreq
  FROM
    input
)

SELECT
  AVG(Number) median
FROM
  processed_median
WHERE
  Frequency >= ABS(lFreq - rFreq)

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

with department_processed AS (
  SELECT
    LEFT(pay_date, 7) pay_month,
    e.department_id department_id,
    AVG(amount) OVER(PARTITION BY s.pay_date) company_avg,
    AVG(amount) OVER(PARTITION BY s.pay_date, d.department_id) department_avg
  FROM
    salary s JOIN employee e
    ON (s.employee_id = e.employee_id)
)

SELECT
  pay_month,
  department_id,
  CASE
    WHEN department_avg > company_avg THEN 'higher'
    WHEN department_avg < company_avg THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM
  department_processed
ORDER BY
  pay_month;


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
  current.install_dt install_dt,
  COUNT(DISTINCT current.player_id) AS installs,
  SUM(CASE WHEN next.player_id IS NOT NULL THEN 1 ELSE 0) / COUNT(DISTINCT current.player_id) Day1_retention
FROM
  (SELECT player_id, MIN(event_date) install_dt FROM Activity GROUP BY player_id) current
  LEFT JOIN Activity next
  ON (current.player_id = next.player_id AND current.install_dt = next.event_date - INTERVAL '1 DAY')
GROUP BY
  current.install_dt



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
with activity_processed AS (
  SELECT
    *,
    COUNT(DISTINCT activity) OVER(PARTITION BY username) activity_cnt,
    ROW_NUMBER() OVER(PARTITION BY username ORDER BY startDate DESC) activity_rnk
  FROM
    UserActivity
)

SELECT
  username, activity, startDate, endDate
FROM
  activity_processed
WHERE
  activity_cnt = 1 OR activity_rnk = 2



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
