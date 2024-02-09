def is_above_5_5(movie):
    return movie["imdb"] > 5.5

def get_movies_above_5_5(movies):
    return [movie for movie in movies if is_above_5_5(movie)]

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def compute_average_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

def compute_average_score_by_category(movies, category):
    category_movies = get_movies_by_category(movies, category)
    return compute_average_score(category_movies)