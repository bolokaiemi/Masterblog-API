from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 2, "title": "Second Post", "content": "This is the second post.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 3, "title": "Learning Python", "content": "Python is easy to learn with consistent practice.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 4, "title": "Flask Basics", "content": "Flask helps you build web apps quickly and easily.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 5, "title": "Debugging Code", "content": "Debugging teaches patience and improves problem-solving skills.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 6, "title": "Web Development", "content": "Combining HTML, CSS, and Flask creates powerful web apps.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 7, "title": "Consistency Matters", "content": "Practicing daily is key to mastering programming.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 8, "title": "Small Projects", "content": "Building small projects helps reinforce what you learn.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 9, "title": "Stay Motivated", "content": "Seeing your code work keeps you motivated to continue.", "author": "Ebi", "date": "2023-06-07"},
    {"id": 10, "title": "Never Give Up", "content": "Every expert was once a beginner—keep going!", "author": "Ebi", "date": "2023-06-07"}
]

# ✅ Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Model (table)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "date": self.date
        }

# 👉 Create DB (run once)
with app.app_context():
    db.create_all()

# :::::::::::::::::::::::::
# GET ALL POSTS
# :::::::::::::::::::::::::
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

# :::::::::::::::::::::::::
# ADD POST
# :::::::::::::::::::::::::
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    new_post = Post(
        title=data.get("title"),
        content=data.get("content"),
        author=data.get("author"),
        date=data.get("date")
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.to_dict()), 201

# :::::::::::::::::::::::::
# UPDATE POST
# :::::::::::::::::::::::::
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()

    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)
    post.author = data.get("author", post.author)
    post.date = data.get("date", post.date)

    db.session.commit()

    return jsonify(post.to_dict())

# :::::::::::::::::::::::::
# DELETE POST
# :::::::::::::::::::::::::
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
