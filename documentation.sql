create table feedList(id integer primary key autoincrement, name text, addr text, content text);
create table feedContent();
--insert example:
insert into feedList(name, addr) values ('michalt blog', 'http://blog.michalt.pl/rss.php', '+content+');
