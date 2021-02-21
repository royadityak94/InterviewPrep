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

Solution: 2
------


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



Solution: Task 2
-------


Solution: Task 3
-------


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
  O/p: date | avg_7_days_signups
------------------------



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


------------------------
Problem # (Get the ID with the highest value in `salaries `)
      depname  | empno | salary |
      -----------+-------+--------+
      develop   |    11 |   5200 |
      develop   |     7 |   4200 |
      develop   |     9 |   4500 |
  Task: Write a query to get the empno with the highest salary. Make sure your solution can handle ties!
------------------------



------------------------
Problem # (Average and rank with a window function)
  Task: Write a query that returns the same table, but with a new column that has average salary per depname. We would expect a table in the form:
------------------------


------------------------
Problem # ()
  Task: Write a query that adds a column with the rank of each employee based on their salary within their department, where the employee with the highest salary gets the rank of 1. We would expect a table in the form:
------------------------



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



  Solution: Task 2
  -------



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
