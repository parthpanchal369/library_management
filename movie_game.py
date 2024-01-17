import random


class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre


class User:
    def __init__(self, username):
        self.username = username
        self.rated_movies = {}


def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    movie = Movie(title, genre)
    movies.append(movie)
    print(f"Movie '{title}' added successfully!")


def rate_movie(user):
    print("Available movies:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie.title} ({movie.genre})")

    choice = int(input("Enter the number of the movie you want to rate: "))
    rating = int(input("Enter your rating (1-5): "))

    movie = movies[choice - 1]
    user.rated_movies[movie.title] = rating

    print(f"Thank you for rating '{movie.title}'!")


def recommend_movie(user):
    unrated_movies = [movie for movie in movies if movie.title not in user.rated_movies]
    if not unrated_movies:
        print("You have rated all available movies. No more recommendations.")
        return

    random_movie = random.choice(unrated_movies)
    print(f"We recommend you watch: '{random_movie.title}' ({random_movie.genre})")


if __name__ == "__main__":
    users = {}
    movies = []

    while True:
        print("\n===== Movie Recommendation System =====")
        print("1. Register User")
        print("2. Add Movie")
        print("3. Rate Movie")
        print("4. Get Movie Recommendation")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            username = input("Enter your username: ")
            users[username] = User(username)
            print(f"User '{username}' registered successfully!")

        elif choice == '2':
            add_movie()

        elif choice == '3':
            username = input("Enter your username: ")
            if username in users:
                rate_movie(users[username])
            else:
                print("User not found. Please register first.")

        elif choice == '4':
            username = input("Enter your username: ")
            if username in users:
                recommend_movie(users[username])
            else:
                print("User not found. Please register first.")

        elif choice == '5':
            print("Exiting Movie Recommendation System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
