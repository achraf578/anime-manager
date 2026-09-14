import os
from typing import List


def load_anime_list(filename: str = "anime.txt") -> List[str]:
    """Load anime names from text file."""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
    return []


def save_anime_list(anime_list: List[str], filename: str = "anime.txt") -> None:
    """Save anime names to text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for name in anime_list:
            file.write(f"{name}\n")


def add_anime(anime_list: List[str], name: str) -> bool:
    """Add a new anime to the list if not already present. Returns True if added."""
    cleaned = name.strip().lower()
    if cleaned in [item.lower() for item in anime_list]:
        return False
    anime_list.append(name.strip().title())
    return True


def remove_anime(anime_list: List[str], name: str) -> bool:
    """Remove an anime from the list. Returns True if found and removed."""
    cleaned = name.strip().lower()
    for item in list(anime_list):
        if item.lower() == cleaned:
            anime_list.remove(item)
            return True
    return False


def search_anime(anime_list: List[str], query: str) -> List[str]:
    """Search anime titles matching query."""
    q = query.strip().lower()
    return [item for item in anime_list if q in item.lower()]
