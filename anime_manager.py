"""
Anime Manager Business Logic Module

This module handles file input/output for anime records, string validation,
duplicate prevention, title search, and list management.
"""

import os
from typing import List


def load_anime_list(filename: str = "anime.txt") -> List[str]:
    """
    Load anime title records from a text file.

    Parameters:
        filename (str): Target text file path. Defaults to 'anime.txt'.

    Returns:
        List[str]: List of non-empty anime titles. Returns an empty list if file doesn't exist.
    """
    # Check if target storage file exists on disk
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Clean trailing whitespace and ignore blank lines
            return [line.strip() for line in lines if line.strip()]
    return []


def save_anime_list(anime_list: List[str], filename: str = "anime.txt") -> None:
    """
    Save anime title records to a text file on disk.

    Parameters:
        anime_list (List[str]): List of anime titles to save.
        filename (str): Target text file path. Defaults to 'anime.txt'.
    """
    # Open target file in write mode and write each title on a new line
    with open(filename, "w", encoding="utf-8") as file:
        for name in anime_list:
            file.write(f"{name}\n")


def add_anime(anime_list: List[str], name: str) -> bool:
    """
    Add a new anime title to the list if not already present.

    Parameters:
        anime_list (List[str]): Active list of anime titles.
        name (str): Title of anime to add.

    Returns:
        bool: True if anime was successfully added; False if duplicate title already exists.
    """
    # Normalize input string for duplicate comparison
    cleaned = name.strip().lower()
    existing_lower = [item.lower() for item in anime_list]

    # Reject addition if title already exists in list
    if cleaned in existing_lower:
        return False

    # Format title nicely and append to list
    anime_list.append(name.strip().title())
    return True


def remove_anime(anime_list: List[str], name: str) -> bool:
    """
    Remove an existing anime title from the list.

    Parameters:
        anime_list (List[str]): Active list of anime titles.
        name (str): Title of anime to remove.

    Returns:
        bool: True if anime was found and removed; False otherwise.
    """
    # Normalize search target string
    cleaned = name.strip().lower()

    # Iterate through current list to locate matching entry
    for item in list(anime_list):
        if item.lower() == cleaned:
            anime_list.remove(item)
            return True

    return False


def search_anime(anime_list: List[str], query: str) -> List[str]:
    """
    Search for anime titles containing the specified search string.

    Parameters:
        anime_list (List[str]): Active list of anime titles.
        query (str): Search substring.

    Returns:
        List[str]: List of matching anime titles.
    """
    # Normalize search query
    q = query.strip().lower()

    # Filter and return all entries containing search substring
    return [item for item in anime_list if q in item.lower()]
