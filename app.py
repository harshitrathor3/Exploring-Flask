from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

dummy_data = [
    {
        "title": "Exploring the Universe",
        "author": "Astronomy Enthusiast",
        "date_posted": "2023-01-15",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "title": "Cooking Adventures",
        "author": "Chef Gourmet",
        "date_posted": "2023-02-28",
        "content": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    }
]


@app.route('/')
@app.route('/home')
def home():
    return '<h2>Hello</h2>'


@app.route('/<var>/<var1>')
def fun(var, var1):
    print(var, var1 , sep='\n')
    return f'Hello {escape(var), escape(var1)}'

@app.route('/posts')
def showPosts():
    return render_template('sample.html', posts = dummy_data, title = 'something cool one')

@app.route('/about')
def another():
    return render_template('another.html', title = 'the title is here')

if __name__ == '__main__':
    app.run(debug=True)