-- lists all shows contained in the hbtn_0d_tvshows database
SELECT tv_genres.name, COUNT(tv_shows.title) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
