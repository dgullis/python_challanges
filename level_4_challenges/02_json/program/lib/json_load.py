# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object

import urllib.request
import json
import operator

def load_data_from_url(url):
    with urllib.request.urlopen(url) as response:
        json_data = json.load(response)
        return json_data
    
# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):

    return load_json_data(filename)

def load_json_data(filename):
    # Load JSON data from a file
    with open(filename, 'r') as file:
        return json.load(file)
    

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    
    with open(filename, 'r') as file:
        json_data = json.load(file)
    
    return [item['name'] for item in json_data if item['director'] == director]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    
    with open(filename, 'r') as file:
        json_data = json.load(file)

    return [item['name'] for item in json_data if desired_actor in item['stars'] ]
    

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    with open(filename, 'r') as file:
        json_data = json.load(file)

    return [item['name'] for item in json_data if item['imdb_rating'] >= rating]


# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    with open(filename, 'r') as file:
        json_data = json.load(file)
    
    return [item['name'] for item in json_data if start_year <= item['year'] <= end_year]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    # Load JSON data from file
    json_data = load_json_data(filename)
    # Sort films by year and get their name
    sorted_films = sort_films_by_year(json_data)
    name_of_films = get_name_of_films(sorted_films)
    
    return name_of_films

def load_json_data(filename):
    # Load JSON data from a file
    with open(filename, 'r') as file:
        return json.load(file)

def sort_films_by_year(data):
    # Sort a list of films by year
    return sorted(data, key= operator.itemgetter('year'))
    
def get_name_of_films(data):
    # Get names of films from a list of dictionaries
    return [item['name'] for item in data]

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    with open(filename, 'r') as file:
        json_data = json.load(file)

    sorted_by_year_newest_first = sorted(json_data, key= operator.itemgetter('year'), reverse=True)
    return [item['name'] for item in sorted_by_year_newest_first]


# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    json_data = load_json_data(filename)
    actors = get_actors_starting_with_letter(json_data, letter)
    return(actors)

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
def get_actors_starting_with_letter(data, letter):
    stars = set()
    for item in data:
        for star in item['stars']:
            if star.startswith(letter.upper()):
                stars.add(star)
    return sorted(stars)
    

    
    

