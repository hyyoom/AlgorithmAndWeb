-- id, title, content

CREATE TABLE article(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
-- 데이터를 넣는 방법: INSERT
-- 짝꿍은 INTO

-- 삭제 : DROP
-- DROP TABLE article;



INSERT INTO article
    VALUES (1,'안녕?','나는컨텐트');



INSERT INTO article (id,title,content)
    VALUES (2,'title','나는컨텐트');
    VALUES (3,'title','나는컨텐트');

INSERT INTO article (title,content) --id없어도 autoincrement있어서 알아서 들어감
    VALUES ('title','나는컨텐트');

ALTER TABLE 
 article 
ADD COLUMN
 create_at DATE NOT NULL DEFAULT '';

INSERT INTO article (title,content,create_at)
    VALUES ('title','나는컨텐트',DATE());


ALTER TABLE
 article
RENAME COLUMN
 content TO contents;


-- ALTER TABLE
--  article
-- DROP COLUMN
--  create_at;


--기존의 레코드 수정하기 UPDATE

UPDATE article
 set create_at = DATE();

UPDATE article
 set create_at = '1900-01-01'
WHERE
 id = 3;


UPDATE article
   SET title    = 'updated title',
       contents = 'updated content'
WHERE  id       = 1;


DELETE FROM article
WHERE id = 2;


SELECT *
 FROM article
WHERE id = (
    SELECT id
    FROM article
    ORDER BY id DESC
    LIMIT 1
);

