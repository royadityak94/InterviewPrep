`Practice SQL Recursion questions - Hierarchical or Tree Structured data`

`Problem: Basic Syntax Usage
Task: Sum of all values uptil 50 or parameterized
`
-- Non-parameterized 
WITH RECURSIVE number_yield AS (
    SELECT 1 as digit
    UNION 
    SELECT (digit + 1) AS digit FROM number_yield 
        WHERE digit < 50 -- Last value taken is digit=49 and then 1 is added
)
SELECT 
    SUM(digit)
FROM 
    number_yield
;

-- Parameterized 
WITH RECURSIVE number_yield (digit) AS (
    SELECT 1 AS digit
    UNION 
    SELECT (digit + 1) AS digit FROM number_yield
        WHERE digit < 50
)
SELECT 
    SUM(digit)
FROM 
    number_yield
;

`Problem: Basic Syntax Usage - 2 (Multiple parameters)
Task: Print (i, i*2, i^2) using recursive cte
Parts
`
WITH RECURSIVE tabulated (number, double, square) AS (
    SELECT 1, 2.0, 3.0 
    UNION ALL 
    SELECT 
        t.number + 1, 
        t.double * 2,
        t.square ^ 2
    FROM tabulated t
    WHERE number < 10
)
SELECT * FROM tabulated;


`Problem: Basic Syntax Usage - 3
Task: Sum quantity group by sub-parts, filtered on a given part
Parts
+---------------+----------+----------+
| part          | sub_part | quantity |
+---------------+----------+----------+
| our_product   | sb2      | 100      |
| our_product2  | sb1      | 100      |
| our_product   | sb1      | 200      |
`
WITH RECURSIVE included_parts (sub_part, part, quantity) AS (
    SELECT sub_part, part, quantity FROM parts WHERE part = 'our_product'
    UNION ALL 
    (SELECT 
        p.sub_part, p.part, (p.quantity * ip.quantity)
    FROM 
        parts p, 
        included_parts ip WHERE (p.part = ip.part)
)
SELECT 
    sub_part, 
    SUM(quantity) total_quantity
FROM 
    included_parts
GROUP BY 
    sub_part
;
`Problem: Depth-First Search 
Task: Searching a tree using link field
tree
+---------------+----------+----------+----------+----------+
| id            | link     | data     |    f1    |     f2   |
+---------------+----------+----------+----------+----------+
| zzx1          | zzx2     | 100      | Boston   | Chicago  |
| zzx2          | zzx5     | 200      | Chicago  |  Houston |
`
WITH RECURSIVE search_tree (id, link, data, path) AS (
    (   SELECT 
            t.id, t.link, t.data, ARRAY[ROW(t.f1, t.f2)] path -- last val is like: {"(f1,f2)"}
        FROM tree
    )
    UNION ALL 
    (   SELECT 
            t.id, t.link, t.data, path || ROW(t.f1, t.f2)
        FROM 
            tree t, search_tree st
        WHERE 
            t.id = st.link
    )
)
SELECT 
    *
FROM 
    search_tree
ORDER BY 
    path;

`Problem: Breadth-First Search 
Task: Searching a tree using link field
tree (same as above)
`
WITH RECURSIVE search_tree (id, link, data, depth) AS (
    (   
        SELECT t.id, t.link, t.data, 0 AS depth
        FROM tree t
    ) UNION ALL (
        SELECT 
            t.id, t.link, t.data, (depth + 1) depth
        FROM tree t, search_tree st 
        WHERE t.id = st.link
    )
)
SELECT 
    * 
FROM 
    search_tree 
ORDER BY 
    depth;

`Problem: Cycle Detectioon
Task: Avoid cycle in recursive queries
`
WITH RECURSIVE search_graph(id, link, data, depth, is_cycle, path) AS (
    (
        SELECT 
            g.id, g.link, g.data, 0 AS depth, false AS is_cycle, ARRAY[ROW(g.f1, g.f2)] path
        FROM graph g
    ) UNION ALL (
        SELECT 
            g.id, g.link, g.data, (sg.depth + 1) depth, 
            (ROW(g.f1, g.f2) = ANY (path)) is_cycle,
            (path || ROW(g.f1, g.f2)) path 
        FROM 
            graph g, search_graph sg 
        WHERE 
            g.id = sg.link AND NOT is_cycle
    )
)
SELECT * FROM search_graph;

--- Note from Postgres (Built in (!!) syntax for dfs/bfs/cycle detection)
-- DFS / BFS
WITH RECURSIVE search_tree (id, link, data, path) AS (
    (   SELECT 
            t.id, t.link, t.data,
        FROM tree
    )
    UNION ALL 
    (   SELECT 
            t.id, t.link, t.data
        FROM 
            tree t, search_tree st
        WHERE 
            t.id = st.link
    )
) SEARCH DEPTH FIRST BY id SET ordercol -- SEARCH BREADTH FIRST BY id SET ordercol (for bfs)
SELECT 
    *
FROM 
    search_tree
ORDER BY 
    ordercol;

-- Cycle Detection (built in)
WITH RECURSIVE search_graph(id, link, data, depth) AS (
    (
        SELECT 
            g.id, g.link, g.data, 0 AS depth
        FROM graph g
    ) UNION ALL (
        SELECT 
            g.id, g.link, g.data, (sg.depth + 1) depth, 
        FROM 
            graph g, search_graph sg 
        WHERE 
            g.id = sg.link AND NOT is_cycle
    ) CYCLE id SET is_cycle USING path -- new path  variable created
)
SELECT * FROM search_graph;


`Problem: Traveling Salesman Problem: Shortest round-trip route through US
Task: recursive CTE will enumerate all possible routes and their total distances. We’ll then sort to find the shortest.
Source: https://www.sisense.com/blog/postgres-recursive-cte/
create table places as (
  select
    'Seattle' as name, 47.6097 as lat, 122.3331 as lon
    union all select 'San Francisco', 37.7833, 122.4167
    union all select 'Austin', 30.2500, 97.7500
    union all select 'New York', 40.7127, 74.0059
    union all select 'Boston', 42.3601, 71.0589
    union all select 'Chicago', 41.8369, 87.6847
    union all select 'Los Angeles', 34.0500, 118.2500
    union all select 'Denver', 39.7392, 104.9903
)

name         |lat    |lon     |
-------------+-------+--------+
Seattle      |47.6097|122.3331|
San Francisco|37.7833|122.4167|
Austin       |30.2500| 97.7500|
New York     |40.7127| 74.0059|
Boston       |42.3601| 71.0589|
Chicago      |41.8369| 87.6847|
Los Angeles  |34.0500|118.2500|
Denver       |39.7392|104.9903|

find minimum round trip that can be made starting at San Francisco and ending at same. 
distance_calculator(lat1, lon1, lat2, lon2): x = 69.1 * difference(lat2, lat1), y = 69.1 * difference(lon2, lon1) * cos(lat1/57.3) output = sqrt(x^2+y^2)
`
-- tested code (schema used is poc)
DROP FUNCTION IF EXISTS poc.distance_calculator;
CREATE OR REPLACE FUNCTION poc.distance_calculator(lat1 float, long1 float, lat2 float, long2 float)
	RETURNS float AS $$ 
	DECLARE 
		x float = (69.1) * (lat2 - lat1);
		y float = (69.1) * (long2 - long1) * cos(lat1/57.3);
	BEGIN
		RETURN SQRT(POWER(x, 2) + POWER(y, 2));
	END
$$ LANGUAGE plpgsql

-- Using Recursive function calculator
WITH RECURSIVE distance_tabulator (visited_path, lat, lon, visited_count, total_distance) AS (
	(	SELECT 
			name AS visited_path, 
			lat, lon, 
			1::int AS visited_count,
			0::float AS total_distance
		FROM 
			poc.places
	) UNION ALL (
		SELECT 
			(dt.visited_path || '->' || p.name), 
			p.lat, p.lon, 
			(dt.visited_count + 1)::int visited_count,
			(dt.total_distance + poc.distance_calculator(dt.lat, dt.lon, p.lat, p.lon)) total_distance
		FROM 
			distance_tabulator dt, poc.places p
		WHERE 
			POSITION(p.name IN dt.visited_path) = 0
	)	
) 
SELECT 
	(dt.visited_path || '->' || p.name) visited_path, 
	(dt.total_distance + poc.distance_calculator(dt.lat, dt.lon, p.lat, p.lon)) total_distance, 
	visited_count
FROM 
	distance_tabulator dt, poc.places p
WHERE 
	POSITION('San Francisco' IN dt.visited_path) = 1 -- Starting point AS San Francisco
	AND p.name = 'San Francisco' -- Ending point AS San Francisco
	AND dt.visited_count = 8 -- Minimum # Cities TO visit
ORDER BY 
	total_distance
LIMIT 1
;

`Problem: Upward Recommendation chain for any member (https://pgexercises.com/questions/recursive/getupwardall.html)
Task: CTE should support:  select recommender from recommenders where member=x
members
+---------+----------+---------- +-------- +---------+----------+---------------+-----------+
| memid   | surname  | firstname | address | zipcode | telephone | recommendedby | joindate |
+---------+----------+---------- +-------- +---------+----------+---------------+-----------+
bookings
+---------+--------+---------- +-------+
| facid   | memid  | starttime | slots | 
+---------+--------+---------- +-------+
facilities
+---------+-------+------------+-----------+---------------+--------------------+---------------+----------+
| facid   | name  | membercost | guestcost | initialoutlay | monthlymaintenance | recommendedby | joindate |
+---------+-------+------------+-----------+---------------+--------------------+---------------+----------+
Output (ORDER: member ASC, recommnder DESC): 
+---------+-------------+-----------+---------+
| member  | recommender | firstname | surname | 
+---------+-------------+-----------+---------+
`
WITH RECURSIVE recommenders(member, recommendedby) AS (
    (   SELECT 
            memid, --member
            recommendedby -- who recommended them
        FROM 
            members
    ) UNION ALL (
        SELECT 
            r.member
            m.recommendedby
        FROM 
            members m, recommenders r ON (r.recommendedby = m.memid)
    )
)
SELECT 
    r.member, 
    r.recommendedby recommender, 
    m.firstname, 
    m.surname
FROM 
    recommenders r 
    JOIN members m 
        ON (r.recommender = m.memid)
WHERE 
    r.member IN (2, 12) -- Give the values you are seeking to find upward recommendation 
ORDER BY 
    member, recommender DESC 
;

`Problem: Downward Recommendation chain for any member (https://pgexercises.com/questions/recursive/getdownward.html)
Task: CTE should support:  select recommender from recommenders where member=x
Find the downward recommendation chain for member ID 1: that is, the members they recommended, the members those members recommended, 
and so on. Return member ID and name, and order by ascending member id.
members
+---------+----------+---------- +-------- +---------+----------+---------------+-----------+
| memid   | surname  | firstname | address | zipcode | telephone | recommendedby | joindate |
+---------+----------+---------- +-------- +---------+----------+---------------+-----------+
bookings
+---------+--------+---------- +-------+
| facid   | memid  | starttime | slots | 
+---------+--------+---------- +-------+
facilities
+---------+-------+------------+-----------+---------------+--------------------+---------------+----------+
| facid   | name  | membercost | guestcost | initialoutlay | monthlymaintenance | recommendedby | joindate |
+---------+-------+------------+-----------+---------------+--------------------+---------------+----------+
Output (ORDER: member ASC, recommnder DESC): 
+-------+-----------+---------+
| memid | firstname | surname | 
+-------+-----------+---------+
`

WITH RECURSION downward_recommender (memid, recommendedby) AS (
    (   SELECT 
            memid, 
            recommendedby 
        FROM 
            members m
        WHERE 
            recommendedBy = 1 -- the member from which we want to see the downward recommendations
    ) UNION ALL (
        SELECT 
            dr.memid memid, 
            dr.recommendedby
        FROM 
            downward_recommender dr, members m 
            ON (dr.memid = m.recommendedby)
    )
)
SELECT
    dr.memid, 
    dr.firstname, 
    dr.lastname
FROM 
    downward_recommender dr, members m ON (dr.memid = m.recommendedby)
ORDER BY 
    memid 
;
