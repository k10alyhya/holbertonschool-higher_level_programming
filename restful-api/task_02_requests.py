#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder and prints or saves them."""
import csv
import requests


def fetch_and_print_posts():
    """Fetches all posts and prints the status code and each post title."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetches all posts and saves their id, title and body to posts.csv."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        # Keep only id, title and body from each post
        data = [
            {"id": p["id"], "title": p["title"], "body": p["body"]}
            for p in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
