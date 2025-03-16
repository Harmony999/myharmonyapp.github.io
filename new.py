# from flask import Flask
# import random
# app = Flask(__name__)
# number = random.randint(1, 10)
# @app.route('/')
# def home():
#     return "<h1>Guess a number between 1 and 10!</h1><p>Go to /guess/your_number</p>"
# @app.route('/guess/<int:guess>')
# def check_guess(guess): 
#     if guess == number:
#       return "<h1> Correct! You guessed the number!</h1>"
#     else:
#       return "<h1> Wrong! Try again.</h1>"
# if __name__ == '__main__':
#    app.run(debug=True)

##17-29 PLAIN HTML PAGE##
# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "<h1>Welcome to My Website</h1><p>This is the home page.</p>"
# @app.route('/about')
# def about():
#     return "<h1>About Me</h1><p>I love coding!</p>"
# @app.route('/contact')
# def contact():
#     return "<h1>Contact Me</h1><p>My favorite superhero is BatMan!</p>"
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('form.html')
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     return f"<h1>Hello, {name}!</h1>"
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title='Home', heading='Welcome to My Website', content='This is the home page.')
@app.route('/about')
def about():
    return render_template('index.html', title='About Me', heading='About Me', content='I love coding!')
@app.route('/contact')
def contact():
    return render_template('index.html', title='Contact Me', heading='Contact Me', content='My favorite superhero is Batman!')
if __name__ == '__main__':
    app.run(debug=True)