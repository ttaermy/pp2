# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#rating above 5.5
def check_rating(name):
    for movie in movies:
        if movie["name"] == name:
            return movie["imdb"] > 5.5
    return False  

# Return movies with IMDB rating > 5.5
def good_movies_list():
    return [movie["name"] for movie in movies if movie["imdb"] > 5.5]

# Return a list of movies in a given category
def movies_in_same_category(category_name):
    return [movie["name"] for movie in movies if movie["category"] == category_name]

#the average IMDB rating of all movies
def average_rating():
    total_rating = sum(movie["imdb"] for movie in movies)
    return total_rating / len(movies) if movies else 0

#the average IMDB rating of a specific category
def rating_of_category(movie_category):
    category_movies = [movie["imdb"] for movie in movies if movie["category"] == movie_category]
    return sum(category_movies) / len(category_movies) if category_movies else 0  

