
CREATE TABLE posts ( content TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL );


/* sample data */
INSERT INTO posts(id,content,time)
VALUES(1,'amazing post','2016-06-22'),
(2,'ballons are so beautiful','2017-12-04'),
(3,'cats are so cute.','2018-04-08'),
(4,'dogs are just my favourite loyal friend.','2019-01-19'),
(5,'eehhh.. eggs are so delicious','2020-03-15');