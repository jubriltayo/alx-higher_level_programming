-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT title, name FROM tv_genres AS tg
RIGHT JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
RIGHT JOIN tv_shows AS ts ON ts.id = tsg.show_id
ORDER BY title, name;
