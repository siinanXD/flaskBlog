from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")

        # neue ID erzeugen
        new_id = len(blog_posts) + 1

        new_post = {
            "id": new_id,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)