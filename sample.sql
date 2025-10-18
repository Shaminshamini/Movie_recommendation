INSERT INTO users VALUES (1,'Amit'), (2,'Sneha'), (3,'Rahul');
INSERT INTO movies VALUES
(1,'Inception','Sci-Fi',2010),
(2,'Titanic','Romance',1997),
(3,'The Dark Knight','Action',2008),
(4,'Interstellar','Sci-Fi',2014),
(5,'The Notebook','Romance',2004);

INSERT INTO ratings (user_id,movie_id,rating) VALUES
(1,1,5),(1,3,4),(1,4,5),
(2,2,5),(2,5,4),
(3,1,4),(3,3,5),(3,4,4);
