
SELECT first_name, country
 FROM users
WHERE first_name='건우'
AND country = '경기도';


SELECT first_name, country
 FROM users
WHERE country != '강원도' 
AND country != '경기도'
AND age BETWEEN 20 AND 30;

