-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT 'tv_shows.title', 'tv_show_genres.genre_id'
           FROM 'tv_shows'
       	   INNER JOIN 'tv_shows.genres' ON 'tv_shows.id' = 'tv_show_genres.show_id'
           WHERE 'tv_shows.id' IN (SELECT show_id FROM 'tv_show_genres')
           ORDER BY 'tv_shows.title', 'tv_show_genres.genre_id';

