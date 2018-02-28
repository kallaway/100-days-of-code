/*
Hackerrank challenge problem
https://www.hackerrank.com/contests/simply-sql/challenges/placements
mysql
*/

SELECT s.Name as name
FROM Students as s
INNER JOIN Packages as p on s.id = p.id
INNER JOIN (SELECT f.ID as id , p.Salary as salary, f.Friend_ID as friend_id
FROM Friends as f
INNER JOIN Packages as p on f.Friend_ID = p.id) as f on f.id=s.id
where f.salary > p.Salary
order by f.salary;
