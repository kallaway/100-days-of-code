-- // SQL Member Count
-- // HIDE QUESTION
-- // In this MySQL challenge, your query should return the names of the people who are reported to (excluding null values), the number of members that report to them, and the average age of those members as an integer. The rows should be ordered by the names in alphabetical order. Your output should look like the
-- // It should have a ReportsTo col, Members Count col and an Avg Age col

-- // My Solution:

SELECT ReportsTo, COUNT(FirstName) AS Members, ROUND(AVG(Age)) AS "Average Age" FROM maintable_Z9PRU WHERE ReportsTo!= "null" GROUP BY ReportsTo;