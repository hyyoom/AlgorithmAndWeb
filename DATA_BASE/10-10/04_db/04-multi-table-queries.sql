-- scott.sql을 이용해서 join 연습

--article, user 같이 조회

SELECT *
  FROM article, user
 WHERE article.userid = user.id;

-- EMPLOPYEE, DEPARTMENT
SELECT e.name , e.deptno, d.name
  FROM EMPLOYEE e, DEPARTMENT d
 WHERE e.deptno = d.deptno;

-- 동등조인 == INNER JOIN
SELECT e.name , e.deptno, d.name, d.location
  FROM EMPLOYEE e
 INNER JOIN DEPARTMENT d
    ON e.deptno = d.deptno;

-- 각 직원의 상사 이름을 조회,SELF JOIN
SELECT e1.name, e1.job, e1.deptno,e1.boss, e2.name
  FROM EMPLOYEE e1, EMPLOYEE e2
 WHERE e1.boss = e2.empno;

SELECT * FROM EMPLOYEE;

-- 한쪽이라도 값을 가지고 있으면 일단 조회
-- 하고 없는 쪽은 NULL 표시하면 좋겠는데 OUTER JOIN
SELECT e1.name, e1.job, e1.deptno,e1.boss, e2.name
  FROM EMPLOYEE e1
 LEFT JOIN EMPLOYEE e2
   ON e1.boss = e2.empno;


-- 직원의 이름 상사이름 부서 이름 조회

SELECT e1.name, e2.name, d.name
  FROM EMPLOYEE e1, EMPLOYEE e2, DEPARTMENT d
 WHERE e1.boss = e2.empno
   AND e1.deptno = d.deptno;


SELECT e1.name, e2.name, d.name
  FROM EMPLOYEE e1 
  INNER JOIN EMPLOYEE e2
    ON e1.boss = e2.empno
  INNER JOIN DEPARTMENT d
    ON e1.deptno = d.deptno;

SELECT e1.name, e2.name, d.name
  FROM EMPLOYEE e1 
  LEFT JOIN EMPLOYEE e2
    ON e1.boss = e2.empno
  LEFT JOIN DEPARTMENT d
    ON e1.deptno = d.deptno;   











