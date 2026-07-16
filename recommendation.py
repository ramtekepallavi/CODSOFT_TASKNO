import random

# Movie database with ratings
movies = {
    "action": [("Avengers", 8.5), ("Batman", 8.2), ("John Wick", 8.0), ("Mad Max", 8.1)],
    "comedy": [("Hera Pheri", 9.0), ("Golmaal", 7.8), ("Dhamaal", 7.5), ("Welcome", 7.7)],
    "romance": [("Titanic", 9.2), ("DDLJ", 9.0), ("Notebook", 8.5), ("Kabir Singh", 7.0)],
    "horror": [("Conjuring", 8.5), ("Nun", 6.5), ("It", 7.3), ("Annabelle", 6.8)]
}

print("🎬 Welcome to Movie Recommendation System")

# User name
name = input("Enter your name: ")
print(f"\nHello {name}! Let's find a movie for you 🎥")

while True:
    print("\nAvailable categories:")
    print("👉 action | comedy | romance | horror")

    choice = input("\nEnter category (or type 'exit' to quit): ").lower()

    if choice == "exit":
        print(f"\nThank you {name}! Enjoy your movies 🍿")
        break

    elif choice in movies:
        print("\n🔹 Recommended Movies:")

        # Random 2 movies select
        recommendations = random.sample(movies[choice], 2)

        for movie, rating in recommendations:
            print(f"👉 {movie} ⭐ ({rating}/10)")

        # Ask to continue
        again = input("\nDo you want more recommendations? (yes/no): ").lower()

        if again != "yes":
            print(f"\nGoodbye {name}! 👋")
            break

    else:
        print("❌ Invalid category! Please try again.")