from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    return "Hello Python!"

def main():
    # Run the app server on localhost:4449
    app.run('localhost', 4449)

main()