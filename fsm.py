from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_carousel_template, send_button_template, send_1button_template


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_choose(self, event):
        print("I'm choosing a pig")
        userid = event.source.user_id
        reply_token = event.reply_token
        send_carousel_template(reply_token)

    def on_exit_choose(self):
        print("Leaving choose pig")
    
    def is_going_to_initpig1(self, event):
        text = event.message.text
        return text.lower() == "pick polite pig"

    def on_enter_initpig1(self, event):
        print("I choose polite pig")
        reply_token = event.reply_token
        #send_text_message(reply_token, "I'm polite pig")
        send_button_template(reply_token, 'https://i.imgur.com/Pi6xR7v.jpg', "園遊會表演", "受到大家歡迎的禮貌小豬受邀參加園遊會表演，你會讓他表演什麼呢......","表演說唱","be a rap star","扮演一隻麋鹿","be a deer")

    def is_going_to_initpig2(self, event):
        text = event.message.text
        return text.lower() == "pick hungry pig"

    def on_enter_initpig2(self, event):
        print("I choose hungry pig")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/0D0VChb.jpg', "小豬好餓", "愛吃小豬完全不意外的肚子餓了，此時你會......", "餵他高級飼料","cheap food","餵他低級飼料","expensive food")
    
    def is_going_to_initpig3(self, event):
        text = event.message.text
        return text.lower() == "pick crying pig"

    def on_enter_initpig3(self, event):
        print("I choose crying pig")
        reply_token = event.reply_token
        send_text_message(reply_token, "I'm crying pig")

    def is_going_to_rap(self, event):
        text = event.message.text
        return text.lower() == "be a rap star"

    def on_enter_rap(self, event):
        print("My pig is a rap star")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/5lrXUQm.jpg', "精彩的說唱表演", "你的小豬在舞台上大放異彩！","太好了","good")

    def is_going_to_deer(self, event):
        text = event.message.text
        return text.lower() == "be a deer"

    def on_enter_deer(self, event):
        print("My pig is a deer")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/cwNLvYS.jpg', "可愛小麋鹿發糖果", "你的小豬扮成麋鹿在人群中發糖果🍬","太可愛了","so cute")

    def is_going_to_princess(self, event):
        text = event.message.text
        return text.lower() == "so cute"

    def on_enter_princess(self, event):
        print("My pig is a princess")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/cSt1oDw.jpg', "小豬其實是公主!?", "你的小豬在人群中被認出，她其實是從城堡跑出來的小公主！", "真的假的！", "really")

    def is_going_to_rich(self, event):
        text = event.message.text
        return text.lower() == "really"

    def on_enter_rich(self, event):
        print("My pig gives me money")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/cSt1oDw.jpg', "大富大貴", "你的小豬為了報答你的養育之恩，給了你一大筆錢！", "收下並謝謝小豬", "thanks")

    '''
    def on_exit_state2(self):
        print("Leaving state2")
    '''
