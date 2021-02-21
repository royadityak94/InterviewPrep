'''
Higher Link: https://www.linkedin.com/posts/eric-weber-060397b7_data-datascience-sql-activity-6765982620477128704-7h2x
Actual Link: https://lnkd.in/g3c5JGC
SQL (Medium-level) Questions from Leetcode
'''

`Problem: Nth Highest Salary
Task: Write a SQL query to get the nth highest salary from the Employee table.
      +----+--------+
      | Id | Salary |
      +----+--------+
      | 1  | 100    |
      | 2  | 200    |
      | 3  | 300    |
      +----+--------+
      +------------------------+
      | getNthHighestSalary(2) |
      +------------------------+
      | 200                    |
      +------------------------+
`




`Problem:  Rank Scores
Task: Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. (Basically, DENSE_RANK() and not RANK())
          +----+-------+
          | Id | Score |
          +----+-------+
          | 1  | 3.50  |
          | 2  | 3.65  |
          | 3  | 4.00  |
          | 4  | 3.85  |
          | 5  | 4.00  |
          | 6  | 3.65  |
          +----+-------+
          +-------+---------+
          | score | Rank    |
          +-------+---------+
          | 4.00  | 1       |
          | 4.00  | 1       |
          | 3.85  | 2       |
          | 3.65  | 3       |
          | 3.65  | 3       |
          | 3.50  | 4       |
          +-------+---------+
`




`Problem: Consecutive Numbers
Task: Write an SQL query to find all numbers that appear at least three times consecutively.
        Logs table:
        +----+-----+
        | Id | Num |
        +----+-----+
        | 1  | 1   |
        | 2  | 1   |
        | 3  | 1   |
        | 4  | 2   |
        | 5  | 1   |
        | 6  | 2   |
        | 7  | 2   |
        +----+-----+

        Result table:
        +-----------------+
        | ConsecutiveNums |
        +-----------------+
        | 1               |
        +-----------------+
        1 is the only number that appears consecutively for at least three times.
`




`Problem: Department Highest Salary
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Task: Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
`
Solution: 1 (600+ ms)
---------


Solution: 2 (400 ns)
---------

`Problem: Exchange Seats
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.The column id is continuous increment.Mary wants to change seats for the adjacent students.
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the above sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
`
Solution-1:
-------



Solution-2:
-------


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
