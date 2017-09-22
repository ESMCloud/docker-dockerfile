#! /usr/bin/python3

import sqlite3

db = sqlite3.connect('/home/nounours/Downloads/Chinook_Sqlite.sqlite')

db.row_factory = sqlite3.Row
curs = db.cursor()
curs.execute('''SELECT  album.title, group_concat(DISTINCT genre.name) 
                FROM album 
                LEFT JOIN track 
                ON album.albumId = track.albumId 
                LEFT JOIN genre ON  track.genreId = genre.genreId 
                GROUP BY album.title 
                HAVING COUNT(DISTINCT genre.name) > 1''')

for row in curs:
    print('{0}\t:\t{1}'.format(row[0], row[1]))
