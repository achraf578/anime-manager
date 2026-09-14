"""
Anime Manager Console Application Main Entry Point

This module manages user menu prompts, interactive CLI inputs,
and calls functions provided by the anime manager business logic module.
"""

from anime_manager import (
    load_anime_list,
    save_anime_list,
    add_anime,
    remove_anime,
    search_anime,
)


def main():
    """
    Main interactive console loop for the Anime Manager application.
    """
    print("========================================")
    print("           ANIME MANAGER                ")
    print("========================================")

    # Load initial list of anime titles from text file storage
    anime_list = load_anime_list()

    # Main user interaction menu loop
    while True:
        # Print menu choices
        print("\nActions:")
        print("1. Add Anime")
        print("2. Remove Anime")
        print("3. Search Anime")
        print("4. Show Anime List")
        print("5. Save & Exit")

        # Capture user selection
        choice = input("\nPlease select an option (1-5): ").strip()

        # Action 1: Add new anime titles
        if choice == "1":
            try:
                count = int(input("How many anime do you want to add? "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Loop to add specified number of anime entries
            for _ in range(count):
                title = input("Enter anime title: ").strip()
                if title:
                    if add_anime(anime_list, title):
                        print(f"Added: {title.title()}")
                    else:
                        print(f"Notice: '{title}' already exists in your list.")

        # Action 2: Remove existing anime titles
        elif choice == "2":
            try:
                count = int(input("How many anime do you want to remove? "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Loop to remove specified number of anime entries
            for _ in range(count):
                title = input("Enter anime title to remove: ").strip()
                if remove_anime(anime_list, title):
                    print(f"Removed: {title}")
                else:
                    print(f"Notice: Anime '{title}' was not found in your list.")

        # Action 3: Search for anime titles matching query
        elif choice == "3":
            query = input("Enter search keyword: ").strip()
            matches = search_anime(anime_list, query)
            if matches:
                print(f"Found {len(matches)} matching title(s):")
                for m in matches:
                    print(f" - {m}")
            else:
                print("No anime found matching your search query.")

        # Action 4: Display complete anime roster list
        elif choice == "4":
            if not anime_list:
                print("Your anime list is currently empty.")
            else:
                print("\n--- Current Anime List ---")
                for idx, name in enumerate(anime_list, start=1):
                    print(f"{idx}. {name}")

        # Action 5: Save current entries to disk and terminate session
        elif choice == "5":
            save_anime_list(anime_list)
            print("Anime list saved successfully. Goodbye.")
            break

        # Handle invalid options
        else:
            print("Invalid selection. Please choose an option between 1 and 5.")


if __name__ == "__main__":
    main()
