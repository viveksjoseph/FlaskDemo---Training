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

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titles = ["Title passed", "Another title"], 
                                        user = User("Vivek", "Joseph"), 
                                        alt_user = User("Lakshay", "Khatter"))

if __name__ == '__main__':
    app.run(debug=True)