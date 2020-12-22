from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_carousel_template, send_button_template


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
        
        self.go_back()

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
        self.go_back()

    def is_going_to_initpig2(self, event):
        text = event.message.text
        return text.lower() == "pick hungry pig"

    def on_enter_initpig2(self, event):
        print("I choose hungry pig")

        reply_token = event.reply_token
        send_text_message(reply_token, "I'm hungry pig")
        self.go_back()
    
    def is_going_to_initpig3(self, event):
        text = event.message.text
        return text.lower() == "pick crying pig"

    def on_enter_initpig3(self, event):
        print("I choose crying pig")

        reply_token = event.reply_token
        send_text_message(reply_token, "I'm crying pig")
        self.go_back()
    '''
    def on_exit_state2(self):
        print("Leaving state2")
    '''
