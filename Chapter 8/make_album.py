def make_album(artist,album,tracks=''):
	"""Return a dictionary containing an album and it's associated artist"""
	album_dict = {'artist': artist.title(), 'album': album.title()}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

album = make_album('tool','lateralus')
print(album)	

album = make_album('a perfect circle','mer de noms')
print(album)	

album = make_album('james blake','james blake','11')
print(album)	

