-- id, title, content
CREATE TABLE article(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  userid INTEGER NOT NULL,
  FOREIGN KEY(userid) REFERENCES user(id)
);

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username varchar(30) NOT NULL UNIQUE,
  email varchar(30) UNIQUE
);

INSERT INTO user (username,email)
     VALUES 
     ('홍길동','hong@email.com'),
     ('이순신','lee@email.com'),
     ('유관순','ryu@email.com');
      






-- 삭제 : DROP
DROP TABLE article;




-- 데이터를 넣는 방법 : INSERT
-- SELECT
--   FROM

INSERT INTO article (title,content,created_at)
     VALUES ('제목3','이거 들어가나요?',DATE());


-- ALTER TABLE
-- 테이블 및 컬럼 수정
-- 칼럼 추가 
ALTER TABLE article 
 ADD COLUMN created_at DATE NOT NULL DEFAULT '';

-- ALTER TABLE article 
--  RENAME COLUMN contents TO content;


ALTER TABLE article
  DROP COLUMN created_at;



-- 기존의 레코드를 수정하기
-- UPDATE
UPDATE article
   SET created_at = '1900-01-01'
 WHERE id = 3;

UPDATE article 
   SET title      = 'updated title',
       content    = 'new content',
       created_at = '2023-10-09'
 WHERE id = 4 ;


DELETE 
  FROM article
 WHERE title = '제목2';


SELECT * 
  FROM article
 WHERE id IN (
  SELECT id
    FROM article
   ORDER BY id
   LIMIT 1
 );


INSERT INTO article (title,content,userid)
     VALUES ('제목2','user1이 쓴글',1);


-- article 테이블에 userid가 user 테이블에
-- 존재하지 않는 경우 데이터 삭제
-- DELETE 
--   FROM article
--  WHERE userid not in (
--   SELECT id from user
--  );
























