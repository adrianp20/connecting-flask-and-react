# Connecting-flask-and-react

**Make sure to have react and flask installed on your system**
Front-end:
(Assuming that you are starting from scratch) In your react terminal input npx create-react-app <your choice of name>


**For creating the virtual environment**
WINDOWS:
python -m venv venv (create virtual environment)
venv\Scripts\activate (activate virtual environment)
if flask has not been installed, run: pip install flask

MAC:
python3 -m venv venv (create virtual environment)
source venv/bin/activate (activate virtual environment)
if flask has not been installed, run: pip3 install flask

**package.json changes**
in between the lines "private" and "dependencies" add the following line: "proxy": "http://localhost:5000",
this will connect flask to our react app

once server.py is built, cd to backend directory and do the following:
WINDOWS: run the server: python server.py
MAC: run the server: python3 server.py

After everything is setup, you can run npm start in your frontend directory and access your website

(credit to this video: https://www.youtube.com/watch?v=7LNl2JlZKHA)
