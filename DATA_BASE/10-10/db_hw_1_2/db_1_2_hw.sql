-- CREATE TABLE users(
--     PK      PRIMARY KEY,
--     email   TEXT NOT NULL,
--     name    TEXT NOT NULL,
--     age     INTEGER NOT NULL,
--     phoneNumber NOT NULL,
--     gender INTEGER
-- );

-- INSERT INTO users
-- VALUES ('1',"@naver", "유형민", "30","01084188820","1");

-- ALTER TABLE 
--  users
-- RENAME COLUMN
--  phoneNumber TO Number;


-- DROP TABLE zoo;

CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);



BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;
