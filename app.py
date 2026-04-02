import json
import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "posts.json")


def load_posts():
    """
    Load all blog posts from the JSON file.

    Returns:
        list: A list of blog post dictionaries.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts if isinstance(posts, list) else []
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error loading posts: {e}")
        return []


def save_posts(posts):
    """
    Save all blog posts to the JSON file.

    Args:
        posts (list): A list of blog post dictionaries to save.

    Returns:
        bool: True if saving was successful, otherwise False.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)
        return True
    except OSError as e:
        print(f"File error while saving: {e}")
        return False
    except TypeError as e:
        print(f"Serialization error: {e}")
        return False


def fetch_post_by_id(posts, post_id):
    """
    Find a blog post by its ID.

    Args:
        posts (list): A list of blog post dictionaries.
        post_id (int): The ID of the post to search for.

    Returns:
        dict | None: The matching post dictionary, or None if not found.
    """
    for post in posts:
        if post["id"] == post_id:
            return post
    return None


@app.route("/")
def index():
    """
    Display all blog posts with optional search and category filtering.
    """
    posts = load_posts()
    search_query = request.args.get("q", "").strip().lower()
    category_filter = request.args.get("category", "").strip()

    filtered_posts = posts

    if search_query:
        filtered_posts = [
            post for post in filtered_posts
            if search_query in post["title"].lower()
            or search_query in post["content"].lower()
        ]

    if category_filter:
        filtered_posts = [
            post for post in filtered_posts
            if post["category"].lower() == category_filter.lower()
        ]

    categories = sorted(set(post["category"] for post in posts))

    return render_template(
        "index.html",
        posts=filtered_posts,
        categories=categories,
        current_search=search_query,
        current_category=category_filter
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Add a new blog post.
    """
    if request.method == "POST":
        posts = load_posts()

        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        category = request.form.get("category", "").strip()

        if not title or not content or not category:
            return "Titel, Inhalt und Kategorie sind erforderlich.", 400

        new_id = max((post["id"] for post in posts), default=0) + 1

        new_post = {
            "id": new_id,
            "title": title,
            "content": content,
            "category": category,
            "likes": 0,
            "comments": []
        }

        posts.append(new_post)

        if not save_posts(posts):
            return "Fehler beim Speichern der Posts.", 500

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """
    Update an existing blog post.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        category = request.form.get("category", "").strip()

        if not title or not content or not category:
            return "Titel, Inhalt und Kategorie sind erforderlich.", 400

        post["title"] = title
        post["content"] = content
        post["category"] = category

        if not save_posts(posts):
            return "Fehler beim Speichern der Posts.", 500

        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """
    Delete a blog post by its ID.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        return "Post not found", 404

    posts.remove(post)

    if not save_posts(posts):
        return "Fehler beim Speichern der Posts.", 500

    return redirect(url_for("index"))


@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    """
    Increase the like count for a blog post.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        return "Post not found", 404

    post["likes"] += 1

    if not save_posts(posts):
        return "Fehler beim Speichern der Posts.", 500

    return redirect(url_for("index"))


@app.route("/comment/<int:post_id>", methods=["POST"])
def comment(post_id):
    """
    Add a comment to a blog post.
    """
    posts = load_posts()
    post = fetch_post_by_id(posts, post_id)

    if post is None:
        return "Post not found", 404

    author = request.form.get("author", "").strip()
    text = request.form.get("text", "").strip()

    if author and text:
        post["comments"].append({
            "author": author,
            "text": text
        })

        if not save_posts(posts):
            return "Fehler beim Speichern der Posts.", 500

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)