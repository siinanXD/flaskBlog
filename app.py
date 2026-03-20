from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

blog_posts = [
    {
        "id": 1,
        "title": "Erster Post",
        "content": "Hallo Welt! Das ist mein erster Blogeintrag.",
        "category": "Allgemein",
        "likes": 0,
        "comments": [
            {"author": "Sinan", "text": "Starker Start!"}
        ]
    },
    {
        "id": 2,
        "title": "Flask lernen",
        "content": "Heute lerne ich Flask und baue meine eigene Blog-App.",
        "category": "Programmierung",
        "likes": 2,
        "comments": []
    }
]


def fetch_post_by_id(post_id):
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


@app.route('/')
def index():
    search_query = request.args.get("q", "").strip().lower()
    category_filter = request.args.get("category", "").strip()

    filtered_posts = blog_posts

    if search_query:
        filtered_posts = [
            post for post in filtered_posts
            if search_query in post["title"].lower() or search_query in post["content"].lower()
        ]

    if category_filter:
        filtered_posts = [
            post for post in filtered_posts
            if post["category"].lower() == category_filter.lower()
        ]

    categories = sorted(set(post["category"] for post in blog_posts))

    return render_template(
        "index.html",
        posts=filtered_posts,
        categories=categories,
        current_search=search_query,
        current_category=category_filter
    )


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        category = request.form.get("category", "").strip()

        if not title or not content or not category:
            return "Titel, Inhalt und Kategorie sind erforderlich.", 400

        new_id = max([post["id"] for post in blog_posts], default=0) + 1

        new_post = {
            "id": new_id,
            "title": title,
            "content": content,
            "category": category,
            "likes": 0,
            "comments": []
        }

        blog_posts.append(new_post)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        category = request.form.get("category", "").strip()

        if not title or not content or not category:
            return "Titel, Inhalt und Kategorie sind erforderlich.", 400

        post["title"] = title
        post["content"] = content
        post["category"] = category

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    return redirect(url_for('index'))


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    post["likes"] += 1
    return redirect(url_for('index'))


@app.route('/comment/<int:post_id>', methods=['POST'])
def comment(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    author = request.form.get("author", "").strip()
    text = request.form.get("text", "").strip()

    if author and text:
        post["comments"].append({
            "author": author,
            "text": text
        })

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)