"""
Here are a few ways to create/add to a dictionary.
"""
# create the dictionary object with either of these
current_movies = dict()
current_movies = {"The Grinch": "11:00am", "Rudolph": "1:00pm"}

# add to the dictionary object with either of these
current_movies["Frosty the Snowman"] = "3:00pm"
current_movies.update({"Christmas Vacation": "5:00pm"})

print("We're currently showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, "is playing at", showtime)
