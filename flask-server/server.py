# WINDOWS:
# python -m venv venv (create virtual environment)
# venv\Scripts\activate (activate virtual environment)
# if flask has not been installed, run: pip install flask

# MAC:
# python3 -m venv venv (create virtual environment)
# source venv/bin/activate (activate virtual environment)
# if flask has not been installed, run: pip3 install flask

from flask import Flask 

app = Flask(__name__)

# memebers api route
@app.route('/members')
def members():
    return {"members" : ["member1", "member2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)
    
# WINDOWS: run the server: python server.py
# MAC: run the server: python3 server.py