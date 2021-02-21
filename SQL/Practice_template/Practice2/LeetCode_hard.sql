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
