from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, CarouselTemplate,
    ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction, URIAction, CarouselColumn, MessageAction
)

import os

app = Flask(__name__)

line_bot_api = LineBotApi('SO3U/GpBN0KYGAdsrT/NEGh9lQ8q7SCb1rj/ajDhWsYNyC2uHEPvRWzFaXUgeDVoj0k6tCFjFERXUUfcJozzIG88dGLmpBK8WR6PE+xSLneu+wuebE3mgQRt4WZ1LRAgr3RrGv+n3jlNPIYgeT2euQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f2810747d94b2abb7c8e13c35b8b46be')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TemplateSendMessage(
        alt_text="a"
        template=ButtonsTemplate(

        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="a"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
