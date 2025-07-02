from flask import Flask
import random
rand_numm=random.randint(0,9)
app=Flask(__name__)

high_url="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
low_url="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
correct_url="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

@app.route("/")
def guess_num():
    return f"<h1>Guess the random number between 0 and 9</h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:num>")
def check_num(num):
    if num<rand_numm:
        return "<h1 style='color:red'>Too low.Try Again</h1>"\
                f"<img src='https://media.tenor.com/wfRFTgb7TG4AAAAM/chiraaku-king-movie.gif'/>"
    elif num>rand_numm:
        return "<h1 style='color:blue'>Too high.Try Again</h1>"\
                f"<img src='https://i.makeagif.com/media/4-04-2015/MK5-uW.gif'/>"
    else:
        return "<h1 style='color:green'>Correct.Well Done</h1>"\
            f"<img src='https://media.tenor.com/846h3lLpu94AAAAM/jklsouth-jkltelugu.gif'/>"














if __name__=="__main__":
    app.run()