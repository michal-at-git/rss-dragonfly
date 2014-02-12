
--insert example:
insert into feedList(name, addr) values ('michalt blog', 'http://blog.michalt.pl/rss.php', '+title+');

-- update:
create table feedList(id integer primary key autoincrement, name text, addr text, FeedTitle text);
create table items(id integer primary key autoincrement, feed_id references feedList(id), title text, pubDate date, description text);
