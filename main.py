from anime_manager import (
    load_anime_list,
    save_anime_list,
    add_anime,
    remove_anime,
    search_anime,
)


def main():
    print("========================================")
    print("           ANIME MANAGER                ")
    print("========================================")

    anime_list = load_anime_list()

    while True:
        print("\nActions:")
        print("1. Add Anime")
        print("2. Remove Anime")
        print("3. Search Anime")
        print("4. Show Anime List")
        print("5. Save & Exit")

        choice = input("\nPlease select an option (1-5): ").strip()

        if choice == "1":
            try:
                count = int(input("How many anime do you want to add? "))
            except ValueError:
                print("Invalid number.")
                continue

            for _ in range(count):
                title = input("Enter anime title: ").strip()
                if title:
                    if add_anime(anime_list, title):
                        print(f"-> Added: {title.title()}")
                    else:
                        print(f"-> '{title}' already exists in your list!")

        elif choice == "2":
            try:
                count = int(input("How many anime do you want to remove? "))
            except ValueError:
                print("Invalid number.")
                continue

            for _ in range(count):
                title = input("Enter anime title to remove: ").strip()
                if remove_anime(anime_list, title):
                    print(f"-> Removed: {title}")
                else:
                    print(f"-> Anime '{title}' not found!")

        elif choice == "3":
            query = input("Search query: ").strip()
            matches = search_anime(anime_list, query)
            if matches:
                print(f"Found {len(matches)} match(es):")
                for m in matches:
                    print(f" - {m}")
            else:
                print("No anime found matching your query!")

        elif choice == "4":
            if not anime_list:
                print("Your anime list is currently empty.")
            else:
                print("\n--- Anime List ---")
                for idx, name in enumerate(anime_list, start=1):
                    print(f"{idx}. {name}")

        elif choice == "5":
            save_anime_list(anime_list)
            print("Anime list saved successfully. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
