from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('GL6Zjxe2JAY1N4m5t/jrupLbBcp3ODgmEy68o2I/ek5+Sk49kkpUD9449SUO/KfhjPN/eu0fF4PSkE92pF5ZVTm48rduATBJl7ViE0RDyFEf4V/V33RmMVAQ/oMV65lwsgp//hBxAqbro42o8cFK2wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('bc038fd97e1a5fd24d9a8285aa341c44')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, "you are pig")

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
