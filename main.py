from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            for message in messages:
                # Replace with your logic to send a message
                print(f"Sending message: {message}")
                sleep(time_interval)

    return '''
    <form method="post" enctype="multipart/form-data">
        Access Token: <input type="text" name="accessToken"><br>
        Thread ID: <input type="text" name="threadId"><br>
        Kidx: <input type="text" name="kidx"><br>
        Time Interval: <input type="number" name="time"><br>
        Text File: <input type="file" name="txtFile"><br>
        <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run()
