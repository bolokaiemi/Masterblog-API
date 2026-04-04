from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
    {"id": 3, "title": "Learning Python", "content": "Python is easy to learn with consistent practice."},
    {"id": 4, "title": "Flask Basics", "content": "Flask helps you build web apps quickly and easily."},
    {"id": 5, "title": "Debugging Code", "content": "Debugging teaches patience and improves problem-solving skills."},
    {"id": 6, "title": "Web Development", "content": "Combining HTML, CSS, and Flask creates powerful web apps."},
    {"id": 7, "title": "Consistency Matters", "content": "Practicing daily is key to mastering programming."},
    {"id": 8, "title": "Small Projects", "content": "Building small projects helps reinforce what you learn."},
    {"id": 9, "title": "Stay Motivated", "content": "Seeing your code work keeps you motivated to continue."},
    {"id": 10, "title": "Never Give Up", "content": "Every expert was once a beginner—keep going!"}
]

# :::::::::::::::::::::::::
# GET ALL POSTS
# :::::::::::::::::::::::::
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


# :::::::::::::::::::::::::
# ADD POST
# :::::::::::::::::::::::::
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    new_post = {
        "id": max([post["id"] for post in POSTS], default=0) + 1,
        "title": data.get("title"),
        "content": data.get("content")
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201


# ::::::::::::::::::::::::::
# UPDATE POST
# ::::::::::::::::::::::::::
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()

    for post in POSTS:
        if post["id"] == post_id:
            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])
            return jsonify(post)

    return jsonify({"error": "Post not found"}), 404


# :::::::::::::::::::::::::
# DELETE POST
# :::::::::::::::::::::::::
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global POSTS

    POSTS = [post for post in POSTS if post["id"] != post_id]

    return jsonify({"message": "Post deleted"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
