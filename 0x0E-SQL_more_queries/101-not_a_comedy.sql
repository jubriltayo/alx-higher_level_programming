-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT title FROM tv_genres AS tg
RIGHT JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
RIGHT JOIN tv_shows AS ts ON ts.id = tsg.show_id
WHERE ts.title NOT IN (
		SELECT DISTINCT title FROM tv_genres AS tg
		INNER JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
		INNER JOIN tv_shows AS ts ON ts.id = tsg.show_id
		WHERE tg.name = 'Comedy')
ORDER BY title;
