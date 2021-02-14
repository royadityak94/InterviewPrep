'''
Practice Source: https://quip.com/2gwZArKuWk7W
'''
------------------------
Problem #1 (MoM Percent Change)
Task: Find the month-over-month percentage change for monthly active users (MAU)
Table Name: logins (userID, date)
| user_id | date       |
|---------|------------|
| 1       | 2018-07-01 |
| 234     | 2018-07-02 |
| 3       | 2018-07-02 |
| 1       | 2018-07-02 |
| ...     | ...        |
| 234     | 2018-10-04 |
------------------------

WITH monthly_active_users AS (
  SELECT
    DATE_TRUNCATE('month', date) AS month_ts,
    COUNT(DISTINCT userID) AS active_users
  FROM
    logins
  GROUP BY
    DATE_TRUNC('month', date)
)
SELECT
  current.month_ts current_month,
  current.active_users current_active_users,
  previous.month_ts previous_month,
  previous.active_users previous_active_users,
  ROUND(((current.active_users - previous.active_users)/current.active_users)*100.0, 2) AS percentage_change
FROM
  monthly_active_users current
  JOIN
  monthly_active_users previous
WHERE
  current.month_ts = previous.month_ts + INTERVAL '1 months'

------------------------
Problem #2 (Tree Structure Labeling )
  Task: Write SQL such that we label each node as a “leaf”, “inner” or “Root” node, such that for the nodes above we get
  Table: tree
        node   parent
          1       2
          2       5
          3       5
          4       3
          5       NULL
  Output:
          node    label
          1       Leaf
          2       Inner
          3       Inner
          4       Leaf
          5       Root
------------------------

Solution: 1
------
WITH tree_labels AS (
  SELECT
    current.node AS node,
    current.parent AS parent,
    COUNT(next.node) AS children
  FROM
    tree current
  JOIN
    tree next
  ON
    current.node = next.parent
  GROUP BY (
    current.node,
    current.parent
    )
  )
SELECT
  node,
  CASE
    WHEN parent IS NULL THEN 'Root'
    WHEN children = 0 THEN 'Leaf'
    ELSE 'Inner'
  END AS label
FROM
  tree_labels

Solution: 2
------

SELECT
  node,
  CASE
    WHEN parent IS NULL THEN 'Root'
    WHEN node NOT IN
      (SELECT parent FROM tree WHERE parent IS NOT NULL) THEN 'Leaf'
    WHEN node IN (SELECT parent FROM tree) THEN 'Inner'
  END AS lable
FROM
  tree

------------------------
Problem #3 (Retained Users Per Month) -> logins
      | user_id | date       |
      |---------|------------|
      | 1       | 2018-07-01 |
      | 234     | 2018-07-02 |
      | 3       | 2018-07-02 |
      | 1       | 2018-07-02 |
      | ...     | ...        |
      | 234     | 2018-10-04 |

  Task 1: Write a query that gets the number of retained users per month. In this case, retention for a given month is defined as the number of users who logged in that month who also logged in the immediately previous month.

  Task 2: Now we’ll take retention and turn it on its head: Write a query to find many users last month did not come back this month. i.e. the number of churned users.

  Task 3: Create a table that contains the number of reactivated users per month. (Active -> InActive -> Active for Month-over-month)
------------------------

Solution: Task 1
-------

WITH DistinctMonthlyUsers AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', a.date) AS month_ts
  FROM
    logins
)

SELECT
  current.month_ts AS month_timestamp,
  COUNT(previous.user_id) AS retained_user_count
FROM
  DistinctMonthlyUsers current
  LEFT JOIN
  DistinctMonthlyUsers previous
  ON
    current.month_ts = previous.month_ts + INTERVAL '1 month'
    AND
    current.user_id = previous.user_id
GROUP BY
  current.month_ts

Solution: Task 2
-------
SELECT
  DATE_TRUNC('month', current.date) AS month_ts,
  COUNT(DISTINCT previous.user_id) churned_users
FROM
  logins current
FULL OUTER JOIN
  logins previous
ON
  current.user_id = previous.user_id
  AND
  DATE_TRUNC('month', current.data) = DATE_TRUNC('month', previous.data) + INTERVAL '1 month'
WHERE
  current.user_id IS NULL
GROUP BY
  DATE_TRUNC('month', current.date)

Solution: Task 3
-------

SELECT
  DATE_TRUNC('month', current.date) AS month_ts,
  COUNT(DISTINCT current.user_id) reactivated_users,
  MAX(DATE_TRUNC('month', previous.date)) AS most_recent_active_previously
FROM
  logins current
FULL OUTER JOIN
  logins previous
ON
  current.user_id = previous.user_id
  AND
  DATE_TRUNC('month', current.data) > DATE_TRUNC('month', previous.data)
GROUP BY
  DATE_TRUNC('month', current.date)
HAVING
  month_ts > most_recent_active_previously + INTERVAL '1 month'


------------------------
Problem #4 (Cumulative Sums)
  Say we have a table `transactions` in the form
    | date       | cash_flow |
    |------------|-----------|
    | 2018-01-01 | -1000     |
    | 2018-01-02 | -100      |
    | 2018-01-03 | 50        |
    | ...        | ...       |
  Task: Write a query to get cumulative cash flow for each day such that we end up with a table in the form below:
      | date       | cumulative_cf |
      |------------|---------------|
      | 2018-01-01 | -1000         |
      | 2018-01-02 | -1100         |
      | 2018-01-03 | -1050         |
      | ...        | ...           |
------------------------

SELECT
  date,
  SUM(cash_flow) OVER(Order by date ASC) AS cumulative_cf
FROM
  transactions
ORDER BY
  date ASC

------------------------
Problem #5 (Rolling Averages )
    Say we have table `signups` in the form:
        | date       | sign_ups |
        |------------|----------|
        | 2018-01-01 | 10       |
        | 2018-01-02 | 20       |
        | 2018-01-03 | 50       |
        | ...        | ...      |
        | 2018-10-01 | 35       |

  Task: Write a query to get 7-day rolling (preceding) average of daily sign up
------------------------

SELECT
  date,
  AVG(sign_ups) OVER(ORDER BY date ROWS BETWEEN 6 PRECEEDING AND 0 PRECEEDING) AS avg_7_days_signups
FROM
  signups

------------------------
Problem #6 (Multiple Join Conditions )
    Say we have a table `emails` that includes emails sent to and from zach@g.com
          | id | subject  | from         | to           | timestamp           |
          |----|----------|--------------|--------------|---------------------|
          | 1  | Yosemite | zach@g.com   | thomas@g.com | 2018-01-02 12:45:03 |
          | 2  | Big Sur  | sarah@g.com  | thomas@g.com | 2018-01-02 16:30:01 |
          | 3  | Yosemite | thomas@g.com | zach@g.com   | 2018-01-02 16:35:04 |
          | 4  | Running  | jill@g.com   | zach@g.com   | 2018-01-03 08:12:45 |
          | 5  | Yosemite | zach@g.com   | thomas@g.com | 2018-01-03 14:02:01 |
          | 6  | Yosemite | thomas@g.com | zach@g.com   | 2018-01-03 15:01:05 |
          | .. | ..       | ..           | ..           | ..                  |

  Task: Write a query to get the response time per email (id) sent to zach@g.com .
  Do not include ids that did not receive a response from zach@g.com.
  Assume each email thread has a unique subject.
  Keep in mind a thread may have multiple responses back-and-forth between zach@g.com and another email address.
------------------------

SELECT
  sender.id,
  MIN(recipient.timestamp) - sender.timestamp AS time_to_respond\
FROM
  emails sender
  JOIN
  emails recipient
  ON
    sender.subject = recipient.subject
    AND
    sender.to = recipient.from
    AND
    sender.from = recipient.to
    AND
    sender.timestamp < recipient.timestamp
WHERE
  sender.to = 'zach@g.com'
GROUP BY
  sender.id
------------------------
Problem # (Get the ID with the highest value in `salaries `)
      depname  | empno | salary |
      -----------+-------+--------+
      develop   |    11 |   5200 |
      develop   |     7 |   4200 |
      develop   |     9 |   4500 |
  Task: Write a query to get the empno with the highest salary. Make sure your solution can handle ties!
------------------------

WITH salary_rank AS (
  SELECT
    empno,
    RANK() OVER(ORDER BY salary DESC) rnk
  FROM
    salaries
)
SELECT
  empno
FROM
  salary_rank
WHERE
  rnk = 1;

------------------------
Problem # (Average and rank with a window function)
  Task: Write a query that returns the same table, but with a new column that has average salary per depname. We would expect a table in the form:
------------------------

SELECT
  *,
  ROUND(AVG(salary), 0) OVER (Partition BY depName) AS avg_salary
FROM
  salaries

------------------------
Problem # ()
  Task: Write a query that adds a column with the rank of each employee based on their salary within their department, where the employee with the highest salary gets the rank of 1. We would expect a table in the form:
------------------------

SELECT
  *,
  RANK() OVER(PARTITION BY depname ORDER BY salary DESC) AS salary_rank
FROM
  salaries

------------------------
Problem # (Histograms )
  we have a table `sessions` where each row is a video streaming session with length in seconds:
        | session_id | length_seconds |
        |------------|----------------|
        | 1          | 23             |
        | 2          | 453            |
        | 3          | 27             |
        | ..         | ..             |
  Task: Write a query to count the number of sessions that fall into bands of size 5, i.e. for the above snippet, produce something akin to:
          | bucket  | count |
          |---------|-------|
          | 20-25   | 2     |
          | 450-455 | 1     |
------------------------

WITH historgram AS (
  SELECT
    session_id,
    FLOOR(length_seconds/5) AS bin_start
  FROM
    sessions
)

SELECT
  CONCATENATE(str(bin_start)*5, '-', str(bin_start*5+5)) AS bucket,
  COUNT(DISTINCT session_id) AS count
FROM
  historgram
ORDER BY
  bucket ASC

------------------------
Problem # (CROSS JOIN (multi-part))
  We have a table `state_streams` where each row is a state and the total number of hours of streaming
      | state | total_streams |
      |-------|---------------|
      | NC    | 34569         |
      | SC    | 33999         |
      | CA    | 98324         |
      | MA    | 19345         |
      | ..    | ..            |
  Task 1: Write a query to get the pairs of states with total streaming amounts within 1000 of each other. We would want to see something like
      | state_a | state_b |
      |---------|---------|
      | NC      | SC      |
      | SC      | NC      |
  Task 2:  How could you modify the SQL from the solution to Part 1 of this question so that duplicates are removed?
      | state_a | state_b |
      |---------|---------|
      | NC      | SC      |
------------------------

Solution: Task 1
-------

SELECT
  current.state AS state_a,
  previous.state AS state_b
FROM
  state_streams current
  CROSS JOIN
  state_streams previous
WHERE
  ABS(current.total_streams - previous.total_streams) < 1000
  AND
  current.state <> previous.state

  Solution: Task 2
  -------

  SELECT
    current.state AS state_a,
    previous.state AS state_b
  FROM
    state_streams current
    CROSS JOIN
    state_streams previous
  WHERE
    ABS(current.total_streams - previous.total_streams) < 1000
    AND
    current.state > previous.state

------------------------
Problem # (Advancing Counting )
   I have a table `table` in the following form, where a user can be mapped to multiple values of class:
        | user | class |
        |------|-------|
        | 1    | a     |
        | 1    | b     |
        | 1    | b     |
        | 2    | b     |
        | 3    | a     |
  Task: Write a query to count the number of users in each class such that any user who has label a and b gets sorted into b, any user with just a gets sorted into a and any user with just b gets into b.
          | class | count |
          |-------|-------|
          | a     | 1     |
          | b     | 2     |
------------------------

WITH formatting AS (
  SELECT
    user,
    MAX(class) AS class
  FROM
    table
)

SELECT
  class,
  COUNT(user)
FROM
  formatting
ORDER BY
  class
