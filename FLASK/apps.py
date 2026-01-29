from flask import Flask

apps= Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"  

if __name__ == '__main__':
    app.run()
    