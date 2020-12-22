import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "choose", "initpig1", "initpig2", "initpig3", "rap", "deer", "princess", "rich"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "choose",
            "conditions": "is_going_to_choose",
        },
        {
            "trigger": "advance",
            "source": "choose",
            "dest": "initpig1",
            "conditions": "is_going_to_initpig1",
        },
        {
            "trigger": "advance",
            "source": "choose",
            "dest": "initpig2",
            "conditions": "is_going_to_initpig2",
        },
        {
            "trigger": "advance",
            "source": "choose",
            "dest": "initpig3",
            "conditions": "is_going_to_initpig3",
        },
        {
            "trigger": "advance",
            "source": "initpig1",
            "dest": "rap",
            "conditions": "is_going_to_rap",
        },
        {
            "trigger": "advance",
            "source": "initpig1",
            "dest": "deer",
            "conditions": "is_going_to_deer",
        },
        {
            "trigger": "advance",
            "source": "deer",
            "dest": "princess",
            "conditions": "is_going_to_princess",
        },
        {
            "trigger": "advance",
            "source": "princess",
            "dest": "rich",
            "conditions": "is_going_to_rich",
        },
        {"trigger": "go_back", "source": ["choose", "initpig1", "initpig2", "initpig3", "rap", "deer", "princess"], "dest": "rich"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "嗨！這是一個好玩的養豬計劃！\n請輸入'start'以領養你的專屬小豬🐽")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
