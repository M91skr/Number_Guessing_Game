"""---------------------------------------- Number guessing game ----------------------------------------
In this code, a very simple number guessing game is written using flask.
The user guesses a number between 1 and 9 and writes very basic in the load address. If the guess is correct,
the result will be announced to the user, and if the guess is wrong, the user will be warned to delete
the previous number from the bar address and type a new number.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

from flask import Flask
from random import randint

num = randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1><h3>Please enter the number in the bar address after "/".</h3>' \
           '<img src="https://media4.giphy.com/media/aCqb9YW7QclN3rtto5/giphy.webp?cid=ecf05e47aouzvgboex91z628m6zh91' \
           'ttyce37g0h3n7uzynk&rid=giphy.webp&ct=g" width=200px>'


@app.route('/<int:guess>')
def choice(guess):
    if guess == num:
            return '<h1>You find me</h1>' \
                   '<img src="https://media4.giphy.com/media/Puc4FZWExJc0E/200.webp?cid=ecf05e471r5n7ganr1a4z4obwlbg9w3700b4z9vtlvr07u0x&rid=200.webp&ct=g" width=200px>'
    elif guess < num:
            return '<h1>Too Low, Try again!</h1><h3>Please delete the current number and register a new number.</h3>' \
                   '<img src="https://media1.giphy.com/media/10G2KL8GdtShbi/200.webp?cid=ecf05e471r5n7ganr1a4z4obwlbg9w3700b4z9vtlvr07u0x&rid=200.webp&ct=g" width=200px>'
    else:
            return '<h1>Too High, Try again!</h1><h3>Please delete the current number and register a new number.</h3>' \
                   '<img src="https://media4.giphy.com/media/1wnZSnmrnwJmnJkd1c/giphy.webp?cid=ecf05e471r5n7ganr1a4z4obwlbg9w3700b4z9vtlvr07u0x&rid=giphy.webp&ct=g" width=200px>'



if __name__ == "__main__":
    app.run(debug=True)