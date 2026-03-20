from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

blog_posts = [
    {"id": 1, "title": "Erster Post", "content": "Hallo Welt"},
    {"id": 2, "title": "Zweiter Post", "content": "Mein zweiter Eintrag"}
]


def fetch_post_by_id(post_id):
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


@app.route('/')
def index():
    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")

        new_id = max([post["id"] for post in blog_posts], default=0) + 1

        new_post = {
            "id": new_id,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post["id"] != post_id]
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post["title"] = request.form.get("title")
        post["content"] = request.form.get("content")

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)