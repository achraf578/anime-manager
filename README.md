# Anime Manager

A command-line Python application for tracking, organizing, searching, and managing anime watchlists.

## Overview

The Anime Manager CLI allows users to view, add, search, and remove anime titles interactively. It ensures data persistence by automatically saving entries to a plain text file (`anime.txt`).

## Key Features

- Add and Remove: Interactive title additions and removals with case-insensitive duplicate protection.
- Keyword Search: Substring search filtering across stored anime titles.
- Clean Roster View: Numbered display of stored anime titles.
- Persistent Text File Storage: Automatic loading from and writing to `anime.txt`.

## System Requirements

- Python 3.8 or higher.

## Installation and Execution

Run `main.py` directly using Python:
```bash
python main.py
```

## Project File Structure

```
anime-manager/
│
├── main.py          # Console interactive menu interface
├── anime_manager.py # Logic for list management, validation, and file persistence
├── anime.txt        # Plain text data file
├── .gitignore      # Git exclusion rules
└── README.md        # Project documentation
```

## License

This project is licensed under the MIT License.
