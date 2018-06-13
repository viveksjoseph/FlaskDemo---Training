from flask import Flask, render_template, url_for

app = Flask(__name__)

class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def initials(self):
        return self.firstName + " " +self.lastName

    def __str__(self):
        return self.firstName + " " +self.lastName

# Basic View
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titles = ["Some passed", "Title passed", "Another passed"], 
                                        user = User("SomeName1", "SomeName2"), 
                                        alt_user = User("Name1", "Name2"),
                                        third_user = User("AnotherName1", "AnotherName2"))

# Bookmarks View
@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)