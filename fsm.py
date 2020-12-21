from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_carousel_template


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_initpig1(self, event):
        text = event.message.text
        return text.lower() == "pick polite pig"

    def on_enter_choose(self, event):
        print("I'm choosing a pig")
        userid = event.source.user_id

        reply_token = event.reply_token
        send_carousel_template(reply_token)
        
        self.go_back()

    def on_exit_choose(self):
        print("Leaving choose pig")

    def on_enter_initpig1(self, event):
        print("I choose polite pig")

        reply_token = event.reply_token
        send_text_message(reply_token, "I'm polite pig")
        self.go_back()
    '''
    def on_exit_state2(self):
        print("Leaving state2")
    '''
