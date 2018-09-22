# imelda = "More Mayhem", "Emilda May", 2011, \
#          ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# title, artist, year, tracks = imelda
#
# print("Name of the artist: \t" + artist)
# print("Title of the Album: \t" + title)
# print("Year of production: \t" + str(year)+ "\n")
# for song in tracks:
#     print("\t", song)

# Example of a tuple with a mutable object such as a list:

imelda = "More Mayhem", "Imelda May", 2011, \
         ([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number: {0}, Title: {1}".format(track, title))

