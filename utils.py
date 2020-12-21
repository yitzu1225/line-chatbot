import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn, PostbackEvent

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_carousel_template(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    url = 'https://i.imgur.com/Pi6xR7v.jpg'
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/Pi6xR7v.jpg',                   
                    title='禮貌小豬',
                    text='禮貌小豬很有禮貌,看到每個人都會打招呼！',
                    actions=[            
                        MessageTemplateAction(
                            label='把禮貌小豬帶回家養',
                            text='pick polite pig'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=url, 
                    title='this is menu2',
                    text='description2',
                    actions=[
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        )
                    ]
                )      
            ]
        )
    )
    line_bot_api.reply_message(reply_token,Carousel_template)
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
