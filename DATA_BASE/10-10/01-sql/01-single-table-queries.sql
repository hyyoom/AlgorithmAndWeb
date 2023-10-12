-- 01. Querying data
SELECT 
    LastName
FROM
    employees;

SELECT 
    LastName,FirstName
FROM
    employees;

SELECT * FROM employees;


SELECT 
    FirstName AS '이름'
FROM
    employees;


SELECT
    Name AS '이름', Milliseconds/60000 AS '재생 시간(분)'
FROM
    tracks;

-- 02. Sorting data

SELECT 
    FirstName
FROM
    employees
ORDER BY
    FirstName ASC; --오름차순

SELECT 
    FirstName
FROM
    employees
ORDER BY
    FirstName DESC; --내림차순


SELECT
 Country,City
FROM
 customers
ORDER BY
 Country DESC,
 City ASC;


SELECT Name, Milliseconds/60000
FROM tracks
ORDER BY Milliseconds DESC;




-- NULL 정렬 예시

SELECT
 ReportsTo
FROM 
 employees
ORDER BY
 ReportsTo;

-- 03. Filtering data

SELECT DISTINCT
 Country
FROM 
 customers
ORDER BY
 Country ASC;

SELECT
 City,LastName,FirstName
FROM 
 customers
WHERE
 City = 'Prague';


SELECT
 LastName,FirstName,Company,Country
FROM
 customers
WHERE
 Company IS NULL AND Country = 'USA';


SELECT
 Name, Bytes
FROM
 tracks
WHERE
 100000<=Bytes AND Bytes<= 500000;

SELECT
 Name, Bytes
FROM
 tracks
WHERE
 Bytes BETWEEN 100000 AND 500000;


SELECT
 Name, Bytes
FROM
 tracks
WHERE
 Bytes BETWEEN 100000 AND 500000
ORDER BY
 Bytes;


SELECT
 LastName,FirstName,Country
FROM
 customers
WHERE
 Country IN ('Canada','Germany', 'France');
--  Country NOT IN ('Canada','Germany', 'France');


SELECT
 LastName,FirstName
FROM
 customers
WHERE
 LastName LIKE '%son';


SELECT
 LastName,FirstName
FROM
 customers
WHERE
 FirstName LIKE '___a';


SELECT
 TrackId,Name,Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 7;

SELECT
 TrackId,Name,Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
LIMIT 3,4;



-- 04. Grouping data
-- 값에 대한 계산을 수행하고 단일한 값을 반환하는 집계 함수를 씀

SELECT
 Country, COUNT(*)
FROM
 customers
GROUP BY 
 Country;

SELECT
 Composer, AVG(Bytes)
FROM
 tracks
GROUP BY
 Composer
ORDER BY
 AVG(Bytes) DESC;

SELECT
 Composer, AVG(Bytes) as avgOFbytes
FROM
 tracks
GROUP BY
 Composer
ORDER BY
 avgOFbytes DESC;



SELECT
 Composer, AVG(Milliseconds/60000) AS avgMinute
FROM
 tracks
GROUP BY
 Composer
HAVING --집계함수관련은 where가 아닌 having절을 사용해야함
 avgMinute < 10;

-- 에러


-- 에러 해결
