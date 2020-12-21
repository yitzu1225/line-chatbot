import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_carousel_template(id):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='http://www.520touxiang.com/uploads/allimg/2018121313/v33lv4g3ix2.jpg',                   
                    title='this is menu1',
                    text='description1',
                    actions=[            
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://www.520touxiang.com/uploads/allimg/2018121313/v33lv4g3ix2.jpg',
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
    line_bot_api.push_message(id,Carousel_template)
    return "OK"

def push_message(userid, msg):
    line_bot_api = LineBotApi(access_token)
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
