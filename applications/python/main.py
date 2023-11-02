# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/home')
# def index():
#     return 'home page'

# #@app.route('/hi')
# #def hello():
#  #   return 'Hello, World'

# from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'Hello, {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"