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

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC
      LIMIT M, 1
  );
END

`Key Learnings:
  LIMIT M, 1 has significant speedup (3x) over LIMIT 1 OFFSET M
  DISTINCT Keyword has its own advantage.
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
SELECT
    Score AS Score,
    DENSE_RANK() OVER(ORDER BY score DESC) AS `Rank`
FROM Scores

`Key Learnings:
  DENSE_RANK() doesn't skips a rank in case of tie that Rank() would
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
SELECT DISTINCT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs l1, Logs l2, Logs l3
WHERE
    l1.Id + 1 = l2.Id AND l2.Id + 1 = l3.Id
    AND
    l1.num = l2.num AND l2.num = l3.num

`Key Learnings:
1. Using "l1.id + 1 = l2.id instead of l1.id = l2.id - 1" and "DISTINCT" almost 3x the query speed!! -> Go Forward logic
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
SELECT
    Department, Employee, Salary
FROM(
    SELECT d.Name AS Department, e.Name AS Employee, Salary,
        DENSE_RANK() OVER(PARTITION BY d.Name ORDER BY Salary DESC) AS salary_rnk
    FROM Employee e JOIN Department d
    ON e.DepartmentId = d.Id) AS Salaries_Ranked
WHERE salary_rnk = 1;


Solution: 2 (400 ns)
---------
SELECT
    d.Name Department, e.Name Employee, e.Salary Salary
FROM Employee e JOIN Department d
  ON e.DepartmentId = d.Id
JOIN
  (SELECT DepartmentId, MAX(Salary) Salary FROM Employee GROUP BY DepartmentId) m
ON (m.Salary = e.Salary AND m.DepartmentId = e.DepartmentId)

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

SELECT
    (CASE
        WHEN MOD(id, 2) != 0 and id != counts THEN id + 1
        WHEN MOD(id, 2) != 0 and id = counts THEN id -- Last Row
        ELSE id-1
    END) AS id,
    student
FROM
    seat,
    (SELECT COUNT(*) AS counts FROM seat) total
ORDER BY id ASC;

Solution-2:
-------

SELECT
    ROW_NUMBER() OVER(ORDER BY (IF(id%2=1, id+1, id-1))) AS id,
    student
FROM seat;

`Problem: Apples & Oranges
Task: Write an SQL query to report the difference between number of apples and oranges sold each day. Return the result table ordered by sale_date in format ('YYYY-MM-DD').
Sales table:
+------------+------------+-------------+
| sale_date  | fruit      | sold_num    |
+------------+------------+-------------+
| 2020-05-01 | apples     | 10          |
| 2020-05-01 | oranges    | 8           |
| 2020-05-02 | apples     | 15          |
| 2020-05-02 | oranges    | 15          |
| 2020-05-03 | apples     | 20          |
| 2020-05-03 | oranges    | 0           |
| 2020-05-04 | apples     | 15          |
| 2020-05-04 | oranges    | 16          |
+------------+------------+-------------+
Result table:
+------------+--------------+
| sale_date  | diff         |
+------------+--------------+
| 2020-05-01 | 2            |
| 2020-05-02 | 0            |
| 2020-05-03 | 20           |
| 2020-05-04 | -1           |
+------------+--------------+
`
-- Option - 1
SELECT
  sale_date,
  SUM(CASE WHEN fruit='apples' THEN sold_num ELSE -sold_num END) diff
FROM
  Sales
GROUP BY sale_date
ORDER BY sale_date;

-- Option - 2 {Slow: 2x}
with apple_sale AS (
  SELECT sale_date, sold_num
  FROM Sales
  WHERE fruit = 'apples'
),
orange_sale AS (
  SELECT sale_date, sold_num
  FROM Sales
  WHERE fruit = 'oranges'
)
SELECT
  a.sale_date,
  (a.sold_num - o.sold_num) diff
FROM
  apple_sale a
  INNER JOIN
  orange_sale o
  USING (sale_date)
ORDER BY
  sale_date
;

`Problem: Grand Slam Titles
Task: Write an SQL query to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament. Return the result table in any order.
Players table:
+-----------+-------------+
| player_id | player_name |
+-----------+-------------+
| 1         | Nadal       |
| 2         | Federer     |
| 3         | Novak       |
+-----------+-------------+
Championships table:
+------+-----------+---------+---------+---------+
| year | Wimbledon | Fr_open | US_open | Au_open |
+------+-----------+---------+---------+---------+
| 2018 | 1         | 1       | 1       | 1       |
| 2019 | 1         | 1       | 2       | 2       |
| 2020 | 2         | 1       | 2       | 2       |
+------+-----------+---------+---------+---------+
Result table:
+-----------+-------------+-------------------+
| player_id | player_name | grand_slams_count |
+-----------+-------------+-------------------+
| 2         | Federer     | 5                 |
| 1         | Nadal       | 7                 |
+-----------+-------------+-------------------+
`
-- Approach 1 (Faster - Using Cross Join)
WITH cross_joined AS (
  SELECT
    player_id,
    player_name,
    SUM(
      IF(Wimbledon = player_id, 1, 0)
      + IF(Fr_open = player_id, 1, 0)
      + IF(US_open = player_id, 1, 0)
      + IF(Au_open = player_id, 1, 0)
    ) grand_slams_count
  FROM
    Players p
  CROSS JOIN
    Championships c
  GROUP BY
    player_id
)
SELECT
  *
FROM
  cross_joined
WHERE
  grand_slams_count > 0 -- Filtering out those who haven't won any contest
;

-- Approach 2 (Slower - Using Flattening)
WITH flattened_scores AS (
  SELECT Wimbledon player_id FROM Championships
  UNION ALL
  SELECT Fr_open player_id FROM Championships
  UNION ALL
  SELECT US_open player_id FROM Championships
  UNION ALL
  SELECT Au_open player_id FROM Championships
)
SELECT
  p.player_id,
  p.player_name,
  COUNT(*) grand_slams_count
FROM
  Players p
  INNER JOIN
  flattened_scores fs
  USING (player_id)
GROUP BY
  player_id
;

`Problem: Capital Gain/Loss
Task: Write an SQL query to report the Capital gain/loss for each stock.
Stocks table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+
Result table:
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
`
SELECT
  stock_name,
  SUM(IF(operation='Buy', -price, price)) capital_gain_loss
FROM
  Stocks
GROUP BY
  stock_name
;
`Problem:  All People Report to the Given Manager
Task: Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company. The indirect relation between managers will not exceed 3 managers as the company is small.
Employees table:
+-------------+---------------+------------+
| employee_id | employee_name | manager_id |
+-------------+---------------+------------+
| 1           | Boss          | 1          |
| 3           | Alice         | 3          |
| 2           | Bob           | 1          |
| 4           | Daniel        | 2          |
| 7           | Luis          | 4          |
| 8           | Jhon          | 3          |
| 9           | Angela        | 8          |
| 77          | Robert        | 1          |
+-------------+---------------+------------+
Result table:
+-------------+
| employee_id |
+-------------+
| 2           |
| 77          |
| 4           |
| 7           |
+-------------+
`
-- Join Approach (Faster) - Customized to 3 recursion depth
SELECT
  e1.employee_id
FROM
  Employees e1,
  Employees e2,
  Employees e3
WHERE
  e1.manager_id = e2.employee_id
  and
  e2.manager_id = e3.employee_id
  AND
  e3.manager_id = 3
  AND
  e1.employee_id != 1 -- Filtering out the boss himself!

-- Recursive Approach (Any recursion depth )
WITH RECURSIVE hierarchy AS (
  SELECT employee_id FROM Employees WHERE manager_id = 1 AND employee_id != 1
  UNION ALL
  SELECT ee.employee_id FROM Employees ee JOIN hierarchy ht ON (ee.manager_id = ht.employee_id)
)
SELECT
  *
FROM
  hierarchy;

  -- Recursive Approach (Any recursion depth - but limiting to 3)
  WITH RECURSIVE hierarchy AS (
    SELECT employee_id, 1 recursion_depth FROM Employees WHERE manager_id = 1 AND employee_id != 1
    UNION ALL
    SELECT ee.employee_id, recursion_depth + 1 FROM Employees ee JOIN hierarchy ht ON (ee.manager_id = ht.employee_id)
    WHERE recursion_depth < 3
  )
  SELECT
    employee_id
  FROM
    hierarchy;

`Problem: The Most Frequently Ordered Products for Each Customer
Task: Write an SQL query to find the most frequently ordered product(s) for each customer. The result table should have the product_id and product_name for each customer_id who ordered at least one order. Return the result table in any order.
Customers
+-------------+-------+
| customer_id | name  |
+-------------+-------+
| 1           | Alice |
| 2           | Bob   |
| 3           | Tom   |
| 4           | Jerry |
| 5           | John  |
+-------------+-------+
Orders
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | product_id |
+----------+------------+-------------+------------+
| 1        | 2020-07-31 | 1           | 1          |
| 2        | 2020-07-30 | 2           | 2          |
| 3        | 2020-08-29 | 3           | 3          |
| 4        | 2020-07-29 | 4           | 1          |
| 5        | 2020-06-10 | 1           | 2          |
| 6        | 2020-08-01 | 2           | 1          |
| 7        | 2020-08-01 | 3           | 3          |
| 8        | 2020-08-03 | 1           | 2          |
| 9        | 2020-08-07 | 2           | 3          |
| 10       | 2020-07-15 | 1           | 2          |
+----------+------------+-------------+------------+
Products
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
| 1          | keyboard     | 120   |
| 2          | mouse        | 80    |
| 3          | screen       | 600   |
| 4          | hard disk    | 450   |
+------------+--------------+-------+
Result table:
+-------------+------------+--------------+
| customer_id | product_id | product_name |
+-------------+------------+--------------+
| 1           | 2          | mouse        |
| 2           | 1          | keyboard     |
| 2           | 2          | mouse        |
| 2           | 3          | screen       |
| 3           | 3          | screen       |
| 4           | 1          | keyboard     |
+-------------+------------+--------------+
`
WITH customer_orders AS (
    SELECT
        customer_id,
        product_id,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY purchase_cnt DESC) purchase_rnk
    FROM (
        SELECT
            customer_id,
            product_id,
            COUNT(*) purchase_cnt
        FROM
            Orders
        GROUP BY
            customer_id, product_id
    ) t
)
SELECT
    customer_id,
    product_id,
    p.product_name
FROM
    customer_orders co
    INNER JOIN
    Products p
    Using (product_id)
WHERE
    purchase_rnk = 1
ORDER BY
    customer_id, product_id
;

`Problem: Running Total for Different Genders
Task: Write an SQL query to find the total score for each gender at each day. Order the result table by gender and day
Scores table:
+-------------+--------+------------+--------------+
| player_name | gender | day        | score_points |
+-------------+--------+------------+--------------+
| Aron        | F      | 2020-01-01 | 17           |
| Alice       | F      | 2020-01-07 | 23           |
| Bajrang     | M      | 2020-01-07 | 7            |
| Khali       | M      | 2019-12-25 | 11           |
| Slaman      | M      | 2019-12-30 | 13           |
| Joe         | M      | 2019-12-31 | 3            |
| Jose        | M      | 2019-12-18 | 2            |
| Priya       | F      | 2019-12-31 | 23           |
| Priyanka    | F      | 2019-12-30 | 17           |
+-------------+--------+------------+--------------+
Result table:
+--------+------------+-------+
| gender | day        | total |
+--------+------------+-------+
| F      | 2019-12-30 | 17    |
| F      | 2019-12-31 | 40    |
| F      | 2020-01-01 | 57    |
| F      | 2020-01-07 | 80    |
| M      | 2019-12-18 | 2     |
| M      | 2019-12-25 | 13    |
| M      | 2019-12-30 | 26    |
| M      | 2019-12-31 | 29    |
| M      | 2020-01-07 | 36    |
+--------+------------+-------+
`
SELECT
    gender,
    day,
    SUM(score_points) OVER(PARTITION BY gender ORDER BY day) total
FROM
    Scores
ORDER BY
    gender, day
;

`Problem: Find the Start and End Number of Continuous Ranges
Task: Write an SQL query to find the start and end number of continuous ranges in table Logs. Order the result table by start_id.
Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+
Result table:
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
`
WITH formatted_logs AS (
  SELECT
    log_id,
    log_id - OVER(ORDER BY log_id) grouped
  FROM
    Logs
)
SELECT
  MIN(log_id) start_id,
  MAX(log_id) end_id
FROM
  formatted_logs
GROUP BY
  grouped
ORDER BY
  start_id, end_id
;

`Problem: Number of Calls Between Two Persons
Task: Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2. Return the result table in any order.
`
SELECT
  LEAST(from_id, to_id) person1,
  GREATEST(from_id, to_id) person2,
  COUNT(*) call_count,
  SUM(duration) total_duration
FROM
  Calls
GROUP BY
  person1, person2
;

`Problem: Team Scores in Football Tournament
Task: Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches. Result table should be ordered by num_points (decreasing order). In case of a tie, order the records by team_id (increasing order).
`
WITH flattened_matches AS (
    SELECT
        team_id,
        SUM(points_scored) num_points
    FROM (
        SELECT
            host_team team_id,
            SUM(IF(host_goals > guest_goals, 3, IF(host_goals = guest_goals, 1, 0))) points_scored
        FROM
            Matches
        GROUP BY
            team_id
        UNION ALL
        SELECT
            guest_team team_id,
            SUM(IF(guest_goals > host_goals, 3, IF(host_goals = guest_goals, 1, 0))) points_scored
        FROM
            Matches
        GROUP BY
            team_id
        ) t_
    GROUP BY
        team_id
)
SELECT
    t.team_id,
    t.team_name,
    COALESCE(fm.num_points, 0) num_points
FROM
    Teams t
    LEFT JOIN
    flattened_matches fm
    USING (team_id)
ORDER BY
    num_points DESC, team_id
;

`Problem: Tree Node
Task: Given a table tree, id is identifier of the tree node and p_id is its parent node's id. Write a query to print the node id and the type of the node. Sort your output by the node id.
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
`
WITH processed_tree AS (
    SELECT
        parent.id,
        parent.p_id,
        COUNT(child.id) children_count
    FROM
        tree parent
        LEFT JOIN
        tree child
        ON (
            parent.id = child.p_id
        )
    GROUP BY
        id, p_id
)
SELECT
    id,
    IF(p_id IS NULL, 'Root', IF(children_count=0, 'Leaf', 'Inner')) Type
FROM
    processed_tree
ORDER BY
    id
;

`Problem: Customers Who Bought Products A and B but Not C
Task: Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them buy this product. Return the result table ordered by customer_id.
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+
Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
Result table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
`
WITH not_brought_productC AS (
	SELECT DISTINCT
		customer_id
	FROM
		Orders
	GROUP BY
		customer_id
	HAVING
		SUM(product_name = 'A') > 0
		AND SUM(product_name = 'B') > 0
		AND NOT SUM(product_name = 'C') > 0
)
SELECT
	customer_id, customer_name
FROM
	Customers
	INNER JOIN
	not_brought_productC
	USING (customer_id)
ORDER BY
    customer_id
;

`Problem: Last Person to Fit in the Elevator
Task: Write an SQL query to find the person_name of the last person who will fit in the elevator without exceeding the weight limit. It is guaranteed that the person who is first in the queue can fit in the elevator. The maximum weight the elevator can hold is 1000.
Queue table
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+
`
with ordered_queue AS (
    SELECT
        person_name,
        turn,
        SUM(weight) OVER(ORDER BY turn) running_total
    FROM
        Queue

)
SELECT
    person_name
FROM
    ordered_queue
WHERE
    running_total <= 1000
ORDER BY
    turn DESC
LIMIT 1
;

`Problem: Managers with at Least 5 Direct Reports
Task: Given the Employee table, write a SQL query that finds out managers with at least 5 direct report.
Employee
+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
`
SELECT
  ma.Name
FROM
  Employee em
  LEFT JOIN
  Employee ma
  ON (
    em.ManagerId = ma.id
  )
GROUP BY
  ma.Id
HAVING
  ma.Name IS NOT NULL
  AND COUNT(DISTINCT em.Id) >= 5;

`Problem: Active Businesses (Good one!!!)
Task: Write an SQL query to find all active businesses. An active business is a business that has more than one event type with occurences greater than the average occurences of that event type among all businesses.
Events table:
+-------------+------------+------------+
| business_id | event_type | occurences |
+-------------+------------+------------+
| 1           | reviews    | 7          |
| 3           | reviews    | 3          |
| 1           | ads        | 11         |
| 2           | ads        | 7          |
| 3           | ads        | 6          |
| 1           | page views | 3          |
| 2           | page views | 12         |
+-------------+------------+------------+
Result table:
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+
`
WITH event_summary AS (
    SELECT
        event_type,
        AVG(occurences) average_occurences
    FROM
        Events
    GROUP BY
        event_type
)
SELECT
    ev.business_id
FROM
    Events ev
    LEFT JOIN
    event_summary es
    USING (event_type)
WHERE
    ev.occurences > es.average_occurences
GROUP BY
    ev.business_id
HAVING
    COUNT(DISTINCT ev.event_type) > 1
;

`Problem: Second Degree Follower
Task: In facebook, there is a follow table with two columns: followee, follower. Please write a sql query to get the amount of each follower’s follower if he/she has one.
+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
should output:
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
`
SELECT
  parent.follower,
  COUNT(DISTINCT child.follower) num
FROM
  follow parent,
  follow child
WHERE
  parent.follower = child.followee
GROUP BY
  parent
ORDER BY
  parent
;

`Problem: Product Price at a Given Date
Task: Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Result table:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
`
with price_current_day AS (
    SELECT
        product_id,
        new_price price,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) row_rnk
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)
SELECT
    p1.product_id,
    COALESCE(p2.price, 10) price
FROM
    (SELECT DISTINCT product_id FROM Products) p1
    LEFT JOIN
    price_current_day p2
    USING (product_id)
WHERE
    p2.row_rnk = 1
    OR p2.row_rnk IS NULL
;

`Problem: Highest Grade For Each Student
Task: Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id. The output must be sorted by increasing student_id.
Enrollments table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
Result table:
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
`
with enrollment_ranked AS (
    SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id) studentwise_rank
    FROM
        Enrollments
)
SELECT
    student_id,
    course_id,
    grade
FROM
    enrollment_ranked
WHERE
    studentwise_rank = 1
ORDER BY
    student_id
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
