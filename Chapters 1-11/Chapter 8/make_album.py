def make_album(artist,album,tracks=''):
	"""Return a dictionary containing details about an album"""
	album_dict = {'artist': artist.title(), 'album': album.title()}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict

while True:
	print('Please tell me an album: ')
	print('(enter "q" to quit at any time')

	artist_name = input('Album name: ')
	if artist_name == 'q':
		break

	album_name = input('Artist name: ')
	if album_name == 'q':
		break

	album_info = make_album(artist_name, album_name)
	print(album_info)

#old code
# album = make_album('tool','lateralus')
# print(album)	

# album = make_album('a perfect circle','mer de noms')
# print(album)	

# album = make_album('james blake','james blake','11')
# print(album)	

