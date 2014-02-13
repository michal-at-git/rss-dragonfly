
--insert example:
insert into feedList(name,addr,FeedTitle) values('Drugi w liście', 'http://drugi___.pl', 'Drugi Feed');  
insert into items (feed_id,title,pubDate,description) values (2,'Drugi do drugiego', 'now', 'treść 2->2');
-- update:
create table feedList(id integer primary key autoincrement, name text, addr text, FeedTitle text);
create table items(id integer primary key autoincrement, feed_id references feedList(id), title text, pubDate date, description text);
