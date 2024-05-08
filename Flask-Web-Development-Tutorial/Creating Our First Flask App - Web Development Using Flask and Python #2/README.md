# Installing Flask:
Open command prompt or windows powershell and write

pip install flask
The most basic code in flask is:

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

In this first we are importing a class named Flask from flask module then we are making a variable named ‘app’ which takes a string argument. It is nothing but file name, as you can see in the screenshot shown below

If instead of “__name__” i write file name in string format, it works perfectly fine. So, we can write it like

app = Flask(__name__)
or

app = Flask(“filename”)

# Route:
In third line, route is a decorator. We give it a string as argument and that string is our end point. In this case URL is “www.websitename.com/”. If we had written @app.route(“blogs”) then URL would be “www.websitename.com/blogs” and whatever function is written under it will be executed when anybody goes on that end point. We will see it working in our next step.

# app.run():
Now we have written all the code for our web application but whenever we run it, nothing happens. It is because we haven’t ran the application but you will say we executed the code. See it like this, we make functions and run the code but functions don’t execute. Do functions execute by themselves? No, we have to execute them by writing like this functionname(). app.run() is like that, we are making functions but they are just there, not executed. So to execute them we need to write app.run()

If you google search "Minimal flask app", you will find some code written in the flask documentation. The code doesn't contain the app.run() line. In my opinion, it becomes very difficult for beginners to figure out why their application is not running.

# But why app.run()?
Why app.run()? Why can’t we just write like functionname()? Well we don’t want to just execute them at the same time, we want a particular function to execute when user goes to that particular URL.

I have created only one endpoint as of now, we will create more endpoints very soon. You can create more endpoints if you want now or follow the tutorial to see what's next! 

# debug=True
This is an argument which we can give in app.run(). We don't want to restart our app everytime we make changes so it is used to automatically restart the app.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/harry")
def harry():
    return "Hello harry bhai4!"
app.run(debug=True)
