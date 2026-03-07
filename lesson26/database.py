def update_movie(movie_id: int, movie: MovieCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('Update movies set title = ?, director = ? where id = ?', (movie.title, movie.director,movie_id))
    connection.commit()
    update = cursor.rowcount
    connection.close()
    return update > 0

def delete_movie(movie_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('delete from movies where id = ?')