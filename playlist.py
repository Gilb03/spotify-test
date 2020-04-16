playlist = {
"author": "patagonia bus",
"title": "turn it off",
"songs": [
     {'title': "somng1", "artist": ['blue'], 'duration': 2.5},
     {'title': "song2", "artist": ['kitty', 'djkitty'], 'duration': 5.5},
     {'title': "fuck this", "artist": ['blue'], 'duration': 2}
    ] 
 
 }

total_length = 0
for song in playlist['songs']:
     total_length += song['duration']
     print(total_length)