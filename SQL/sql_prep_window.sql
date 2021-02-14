`
Source: windowfunctions.com/about
Topics: Over, Ranking, Grouping, Filter, Windowing
References:
  1. https://www.postgresql.org/docs/current/functions-window.html
  2. https://mode.com/sql-tutorial/sql-window-functions/
  3. https://tapoueh.org/blog/2013/08/understanding-window-functions/
  4. https://use-the-index-luke.com/
`
`
---------------------------------------------------
          Section Name: Intro Questions (GroupBy, Having)
---------------------------------------------------
`
`Problem: Refresher on Aggregagtes
Task: We would like to find the total weight of cats grouped by age having total weight over 12.
`
SELECT
  age,
  SUM(weight) AS total_weight
FROM cats
GROUP BY age
HAVING SUM(weight) > 12
ORDER BY age
`
---------------------------------------------------
          Section Name: Over Questions (Over, Preceding, Following, Partition BY)
Table `Cats`:
name	varchar, breed	varchar, weight	float, color	varchar, age	int
---------------------------------------------------
`
`Problem: Running Totals
Task: The cats must be ordered by name and will enter an elevator one by one. We would like to know what the running total weight is.
`
SELECT
  name,
  SUM(weight) OVER(ORDER BY name) AS total_weight
FROM cats
ORDER BY name

`Problem: Partitioned Running Totals
Task: The cats must be ordered first by breed and second by name. We would like to know what the running total weight of the cats is.
`
SELECT
  name, breed,
  SUM(weight) OVER(PARTITION BY breed ORDER BY name) AS running_total_weight
FROM cats
ORDER BY breed, name

`Problem: Examining nearby rows
Task: The cats would like to see the average of the weight of them, the cat just after them and the cat just before them. The first and last cats are content to have an average weight of consisting of 2 cats not 3.
`
SELECT
  name, weight,
  AVG(weight) OVER(ORDER BY weight ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS average_weight
FROM cats
ORDER BY weight

`Problem: Correct Running Total
Task: The cats must be ordered by weight descending and will enter an elevator one by one. We would like to know what the running total weight is. If two cats have the same weight they must enter separately
`
SELECT
  name,
  SUM(weight) OVER(ORDER BY weight DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_weight
FROM cats
ORDER BY weight DESC
`
---------------------------------------------------
          Section Name: Ranking Questions (Row_Number, Rank, Dense_Rank, Cume_dist & Percent_rank)
percent_rank returns a number from 1 to 0. The highest being 1 and the lowest 0.
cume_dist will return a number from 1 towards 0 but never 0.
---------------------------------------------------
`
`Problem: Unique Numbers
Task: The cats form a line grouped by color. Inside each color group the cats order themselves by name. Every cat must have a unique number for its place in the line.
`
SELECT
  ROW_NUMBER() OVER(ORDER BY color, name) AS unique_number,
  name, color
FROM cats

`Problem: Ordering
Task: We would like to find the fattest cat. Order all our cats by weight. The two heaviest cats should both be 1st. The next heaviest should be 3rd.
`
SELECT
  weight, name,
  RANK() OVER(ORDER BY weight DESC) AS ranking
FROM cats
ORDER BY ranking, name

`Problem: Further Orderring
Task: For cats age means seniority, we would like to rank the cats by age (oldest first). ranking to be sequentially increasing.
`
SELECT
  name, age,
  DENSE_RANK() OVER(ORDER BY age DESC) AS ranking,
FROM cats
ORDER BY ranking, name

`Problem: Percentages
Task: Each cat would like to know what percentage of other cats weigh less than it
`
SELECT
  name, weight,
  (Percent_rank() OVER(ORDER BY weight))*100 AS percent
FROM cats
ORDER BY weight

`Problem: Percentiles
Task: Each cat would like to know what weight percentile it is in. This requires casting to an integer
`
SELECT
  name, weight,
  CAST(CUME_DIST() OVER(ORDER BY WEIGHT)*100 AS INTEGER) AS percent
FROM cats
ORDER BY weight

`
---------------------------------------------------
          Section Name: Grouping Questions (Lag, Lead, nth_value, ntile, first_value)
---------------------------------------------------
`
`Problem: Quartiles
Task: We would like to group the cats into quartiles by their weight.
`
SELECT
  name, weight,
  ntile(4) OVER(ORDER BY weight) AS weight_quartile
FROM cats
ORDER BY weight

`Problem: Compare to Row
Task: Print a list of cats, their weights and the weight difference between them and the nearest lighter cat ordered by weight.
`
SELECT
  name, weight,
  COALESCE(weight - LAG(weight, 1) OVER (ORDER BY weight), 0.0) AS weight_to_lose
FROM cats
ORDER BY weight

`Problem: Compare to Row (Part 2)
Task: The cats now want to lose weight according to their breed. Each cat would like to lose weight to be the equivalent weight of the cat in the same breed weighing just less than it.
`
SELECT
  name, breed, weight,
  COALESCE(weight - LAG(weight, 1) OVER (PARTITION BY breed ORDER BY weight), 0.0) AS weight_to_lose
FROM cats
ORDER BY weight

`Problem: First of each Group
Task:  Each cat would like to pretend it has the lowest weight for its color. Print cat name, color and the minimum weight of cats with that color.
`
SELECT
  name, color,
  nth_value(weight, 1) OVER(PARTITION BY color ORDER BY weight) AS weight_by_color
FROM cats
ORDER BY color, name

`Problem: Row Comparison with Lead
Task: Each cat would like to see the next heaviest cat's weight when grouped by breed. If there is no heavier cat print 'fattest cat'. Print a list of cats, their weights and either the next heaviest cat's weight or 'fattest cat'
`
select
  name, weight, breed,
  COALESCE(CAST(LEAD(weight, 1) OVER(PARTITION BY breed ORDER BY weight) AS VARCHAR), 'fattest cat') AS next_heaviest
FROM cats
ORDER BY weight

`Problem: Special Case Grouping
Task: The cats have decided the correct weight is the same as the 4th lightest cat. All cats shall have this weight. Except the weight of the lightest three to 99.9.
`
select
  name, weight,
  COALESCE(nth_value(weight, 4) OVER(ORDER BY weight), 99.9) AS imagined_weight
FROM cats
ORDER BY weight

`Problem: Grouping (Adv.)
Task: The cats want to show their weight by breed. The cats agree that they should show the second lightest cat's weight. Print a list of breeds, and the second lightest weight of that breed
`
SELECT
  DISTINCT(breed),
  nth_value(weight, 2) OVER(PARTITION BY breed ORDER BY weight RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS imagined_weight
FROM cats
ORDER BY breed
`
---------------------------------------------------
          Section Name: Other Questions (Window, Array Agg, Filter)
Ex: avg(time) filter (where weight < 90) as light_runners_time
Ex: select array_agg(time) from runners -- {101,103,104,104,108}
---------------------------------------------------
`
`Problem: Window Clause
Task: Each cat would like to see what half, third and quartile they are in for their weight.
`
SELECT
  name, weight,
  ntile(2) OVER ntile_win AS half,
  ntile(3) OVER ntile_win AS thirds,
  ntile(4) OVER ntile_win AS quarts
FROM cats
WINDOW ntile_win AS (ORDER BY weight)
ORDER BY weight

`Problem: Array Aggregation
Task: Return 3 rows, each row containing a color and a list of cat names.
      Return: color, names Order by: color DESC
`
SELECT
  color,
  ARRAY_AGG(name) AS names
FROM cats
GROUP BY color
ORDER BY color DESC

`Problem: Filter Operation
Task: We would like to find the average weight of cats grouped by breed. Also, in the same query find the average weight of cats grouped by breed whose age is over 1
`
select
  breed,
  AVG(weight) AS average_weight,
  AVG(weight) FILTER(WHERE age > 1) AS average_old_weight
FROM cats
GROUP BY breed
ORDER BY breed
