# --- List of destinations --- # 
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# --- A test traveler --- #
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# --- Gets the index of the destination passed in --- # 
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# --- Test code for get_destination_index(), will raise a ValueError if argument is invalid --- #
#print(get_destination_index('Los Angeles, USA'))

# --- Gets's the traveler's location using the previous function, as an index of the list passed in --- #
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

# --- Test code for test_destination_index --- #
#print(test_destination_index)

# --- List of attractions. Empty at first, but will fill with future functions --- #
attractions = [[] for i in destinations]
# --- Test code for attractions --- #
#print(attractions)

# --- Adds an attraction for a destination passed in, and puts that attraction in the list attractions. --- #
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  try:
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
  except ValueError:
    return

# --- Adds attractions using the add_attraction function. --- #
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# --- Finds attractions for a user, according to their interests and their destination. --- #
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

# --- Test code for the above function --- #
#la_arts = find_attractions('Los Angeles, USA', ['art'])
#print(la_arts)

# --- Generates a message for the traveler and presents attractions they may be interested in. --- #
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi '
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around " + traveler_destination + ': '
  # --- Logic here checks if the string of traveler_attractions is the last string of the list; if it is, it will return a full stop, if not, it will add a comma to the end of the string. --- #
  i = 0
  while i < len(traveler_attractions):
    if i <= len(traveler_attractions) - 1:
      interests_string += 'the ' + traveler_attractions[i] + '.'
      break
    interests_string += 'the ' + traveler_attractions[i] + ', '
    i += 1
  return interests_string

# --- Calls the above function on a traveler --- #
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

print(smills_france)