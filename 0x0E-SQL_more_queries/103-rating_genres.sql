-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
INNER JOIN tv_show_ratings AS tsr ON tsr.show_id = tsg.show_id
GROUP BY tg.id ORDER BY rating DESC;
