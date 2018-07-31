from flask import Flask, render_template
import socket
import pyautogui

app = Flask(__name__)


@app.route('/')
def index():
    pyautogui.screenshot().save('static/img/screenshot.png')
    return render_template('index.html')


@app.after_request
def header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    """
    Creates an accessible page with a desktop screenshot every few minutes.
    """
    host = socket.gethostbyname(socket.gethostname())   # Manually set host if this fails.
    app.run(host=host, port=5050)
