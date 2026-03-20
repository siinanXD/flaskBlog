from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Beispiel-Daten
blog_posts = [
    {"id": 1, "title": "Erster Post", "content": "Hallo Welt"}
]

@app.route('/')
def index():
    return render_template("index.html", posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")

        new_id = len(blog_posts) + 1

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

if __name__ == "__main__":
    app.run(debug=True)