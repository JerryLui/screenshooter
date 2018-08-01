from flask import Flask, render_template
import threading
import pyautogui
import time

app = Flask(__name__)
app.config['THREAD'] = None


@app.route('/')
def index():
    return render_template('index.html')


@app.after_request
def header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


def worker(sleep_time=30, keep_screen_alive=False):
    while 1:
        # To keep the screen alive
        if keep_screen_alive:
            x, y = pyautogui.position()
            pyautogui.moveTo(0, 0)
            pyautogui.moveTo(x, y)

        pyautogui.screenshot().save('static/img/screenshot.png')
        time.sleep(sleep_time)


if __name__ == '__main__':
    """
    Creates an accessible page with a desktop screenshot every few minutes.
    """
    app.config['THREAD'] = threading.Thread(target=worker)
    app.config['THREAD'].start()

    app.run(port=5050)
