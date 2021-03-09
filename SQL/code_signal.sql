''' Code Signal
Goal: Keep a tab on interesting problems from code signal
'''

`Problem: RANKED SELECTION IN RANGE
Task: The contest leaderboard is stored in a table leaderboard with the following columns:
      - id: unique id of the participant;
      - name: the name of the participant;
      - score: the score the participant achieved in the competition.
The resulting table should contain the names of the participants who took the 4th to 8th places inclusive, sorted in descending order of their places. If there are fewer than 8 participants, the results should contain those who ranked lower than 3rd place.
`
CREATE PROCEDURE contestLeaderboard()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    with ranked AS (
        SELECT
            name,
            RANK() OVER (ORDER BY score DESC) ranking
        FROM
            leaderboard
    )
    SELECT
        name
    FROM
        ranked
    WHERE ranking BETWEEN 4 AND 8
    ;
END

`Problem: Introduction to 'Greatest' (Greatest operates across column, unlike MAX)
Task: you need to query the name and id of all the students whose best grade comes from Option 3, sorted based on the first 3 characters of their name. If the first 3 characters of two names are the same, then the student with the lower ID value comes first.
According to school policy, there are three possible ways to evaluate a grade:

Option 1:
    Midterm 1: 25% of the grade
    Midterm 2: 25% of the grade
    Final exam: 50% of the grade
Option 2:
    Midterm 1: 50% of the grade
    Midterm 2: 50% of the grade
Option 3:
    Final exam: 100% of the grade.
    Each student's final grade com
`

WITH grades_summary AS (
    SELECT
        Name, ID,
        (midterm1 + midterm2 + (2* final)) / 4 option_1,
        (midterm1 + midterm2) / 2 option_2,
        final option_3
    FROM
        Grades
)
SELECT
    Name, ID
FROM
    grades_summary
WHERE
        GREATEST(option_1, option_2, option_3) = option_3
        AND
        option_3 NOT BETWEEN option_1 AND option_2
ORDER BY
    SUBSTRING(name, 1, 3);

`Problem: Introduction to FIELD
Task: It looks like each of your nephews is active on a specific day of the week. You decide to check your theory by creating another table as follows: The resulting table should contain four columns, weekday, mischief_date, author, and title, where weekday is the weekday of mischief_date (0 for Monday, 1 for Tuesday, and so on, with 6 for Sunday). The table should be sorted by the weekday column, and for each weekday >>> Huey's mischief should go first, Dewey's should go next, and Louie's should go last. <<<< In case of a tie, mischief_date should be a tie-breaker. If there's still a tie, the record with the lexicographically smallest title should go first.
The table has the following columns:

      - mischief_date: the date of the mischief (of the date type);
      - author: the nephew who caused the mischief ("Huey", "Dewey" or "Louie");
      - title: the title of the mischief.
`
SELECT
  WEEKDAY(mischief_date) weekday,
  mischief_date, author, title
FROM
  mischief
ORDER BY
  weekday,
  FIELD(author, 'Huey', 'Dewey', 'Louie'),
  mischief_date,
  title;

`Problem: REGEX quick Walkthrough
Task:
`
SELECT
    id, name, surname
FROM
    Suspect
WHERE
    height <= 170
    AND
    name LIKE 'B%' -- name starts with B
    AND
    surname LIKE 'Gre_n'; - surname has {Gre} {a-z} {n}

`Problem: REGEX quick Walkthrough
Task:
`
SELECT
  first_name, second_name, attribute
FROM
  users
WHERE
  attribute LIKE BINARY CONCAT('_%\%', first_name, '\_', second_name, '\%%')
                              -- {0+ chars} {firstName_secondName} {1+ chars}

`Problem: REGEX quick Walkthrough
Task: Count all NULLs including misquoted ones
MATCH following strings -> '   NULL  ', 'ndjcn NIL jnjn', '-' or actual NULL
`
SELECT
  count(*) all_null_count
FROM
  departments
WHERE
  description REGEXP '^ *(NULL|NIL|-) *$' OR description IS NULL;

`Problem: IF Revisited
Task: Your task is to return the table with a column id and a column checks, where for each answers id the following string should be returned:
    "no answer" if the given_answer is empty;
    "correct" if the given_answer is the same as the correct_answer;
    "incorrect" if the given_answer is not empty and is incorrect.
The program will be given a table answers with the following columns:
   - id - the unique ID of the question;
   - correct_answer - the correct answer to the question, given as a string;
   - given_answer - the answer given to the question, which can be NULL.
`
SELECT
  id,
  IF(
    given_answer IS NULL, 'no answer',
    IF(given_answer = correct_answer), 'correct', 'incorrect'
  ) checks
FROM
  answers;

`Problem: Say, hello to Pythonic 'Eval' in SQL
Task: should only contain those rows that represent correct expressions in tbe below SQL table
Table Columns (id	a	b	operation	c) => Output (id	a	b	operation	c)
`
SELECT
  id, a, b, operation, c
FROM
  expressions
WHERE
  ELT(LOCATE(operation, '+-*/'), a+b, a-b, a*b, a/b) = c;
  -- LOCATE functions as index, ELT as which argument to chose. Ex: for '*', chose 3rd argument.

`Problem: Hello to 'Substring Index'
Task:
`

SELECT
    DISTINCT subscriber
FROM (
    SELECT subscriber, newspaper FROM full_year
    UNION
    SELECT subscriber, newspaper FROM half_year
) AS t1
WHERE
    newspaper LIKE '%Daily%' -- Pick newspaper having 'Daily' in it
ORDER BY
    SUBSTRING_INDEX(subscriber, ' ', 1) -- Pick first name from {FirstName LastName} -> pick all elements to the left of delimiter;

`Problem: Hello to GROUP_CONCAT
Task: Given this diary table, create a semicolon-separated list of all the distinct countries you've visited, sorted lexicographically, and put the list in a table that has a single countries column.
id	travel_date	country
1	2008-05-12	Ireland
`
SELECT
  GROUP_CONCAT(DISTINCT country ORDER BY country SEPARATOR ';') countries_visited
FROM
  diary;

`Problem: Hello to GROUP_CONCAT #2
Task:

id	first_name	surname	player_number
1	Alexis	Sanchez	7
2	Petr	Cech	33
Output: ====>
players
Alexis Sanchez #7; Oliver Giroud #12; Theo Walcott #14; Santi Cazorla #19; Hector Bellerin #24; Petr Cech #33
`
SELECT
  GROUP_CONCAT(CONCAT(first_name, ' ', last_name, ' #', player_number) players
FROM
  soccer_team;

`Problem: Hello To 'Rollup'
Task: Given the foreignCompetitors table, compose the resulting table with two columns: country and competitors. The first column should contain the country name, and the second column should contain the number of competitors in this country. The table should be sorted by the country names in ascending order. In addition,>>  it should have an extra row at the bottom with the summary, <<
competitor	country
Acme Corp	USA
GLOBEX	USA
Openmedia	France
K-bam	USA
Hatdrill	UK
----Output----
country	competitors
France	2
Germany	1
Spain	1
UK	1
USA	3
Total:	8
`
SELECT
  IFNULL(country, 'Total:') country,  -- COALESCE(country, 'Total:')
  COUNT(country) competitors
FROM
  foreignCompetitors
GROUP BY
  country
WITH
  ROLLUP -- subclause of GROUP BY, preferred over CUBE

`Problem: Shortcut to combinatorial arithmetics
Task: COUNT all possible combinations the set of characters, colors can assume;
id	characters	color
1	code	blue
2	fights	white
--- OUTPUT ----
combinations
24
`
SELECT
  ROUND(
    EXP(
      SUM(
        LOG(
          LENGTH(characters)
        )
      )
    )
  ) combinations -- Emaluates multiplication of the len(characters)
FROM
  discs;

`
In SQL, as we cannot multiply numbers, with equivalent of MULT(), the trick is:
ROUND(EXP(SUM(Log(...)))) = x*y*z (entries in characters)
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
