from flask import Flask
from flask import render_template
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("index.html", post=all_post)


@app.route('/blog/<int:num>')
def get_post(num):
    response = requests.get(blog_url)
    all_post = response.json()
    post_num = num
    return render_template('post.html', number=post_num, posts=all_post)




if __name__ == "__main__":
    app.run(debug=True)
