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
        reply_token = event.reply_token
        send_carousel_template(reply_token)
    
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
        send_button_template(reply_token, 'https://i.imgur.com/0D0VChb.jpg', "小豬好餓", "愛吃小豬完全不意外的肚子餓了，此時你會......", "餵他低級飼料","cheap food","餵他高級飼料","expensive food")
    
    def is_going_to_initpig3(self, event):
        text = event.message.text
        return text.lower() == "pick crying pig"

    def on_enter_initpig3(self, event):
        print("I choose crying pig")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/5lrXUQm.jpg', "小豬哭個不停", "面對嚎啕大哭的小豬你會怎麼做......","給他吃高級飼料","expensive food","給他吃冰淇淋","icecream")

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
        send_1button_template(reply_token, 'https://i.imgur.com/a/hrZKlmR.jpg', "大富大貴", "你的小豬為了報答你的養育之恩，給了你一大筆錢！", "收下並謝謝小豬", "thanks")
        self.go_back();

    def is_going_to_cheapfood(self, event):
        text = event.message.text
        return text.lower() == "cheap food"

    def on_enter_cheapfood(self, event):
        print("give my pig cheap food")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/cSt1oDw.jpg', "不好了！", "你的小豬嬌生慣養，不肯吃便宜的飼料，此時你會......", "好吧，就買高級飼料給他吃", "expensive food","不理他，強迫他吃", "force")

    def is_going_to_expensivefood(self, event):
        text = event.message.text
        return text.lower() == "expensive food"

    def on_enter_expensivefood(self, event):
        print("give my pig expensive food")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/UKQqmFH.jpg', "吃飽了！", "你的小豬吃飽了之後心滿意足的睡著了，此時你會......", "把他叫起來工作！", "go to work", "讓他睡", "sleep")

    def is_going_to_sleep(self, event):
        text = event.message.text
        return text.lower() == "sleep"

    def on_enter_sleep(self, event):
        print("give my pig expensive food")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "吃飽睡飽", "你的小豬吃飽睡飽後變得超級可愛！", "好開心❤️", "happy")

    def is_going_to_leave(self, event):
        text = event.message.text
        return text.lower() == "force"

    def on_enter_leave(self, event):
        print("my pig is leaving")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "離家出走", "你的小豬受夠你了！", "噢不", "oh no")

    def is_going_to_work(self, event):
        text = event.message.text
        return text.lower() == "go to work"

    def on_enter_work(self, event):
        print("My pig is going to work")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "討厭工作", "顯然你的小豬並不喜歡工作，此時你會......", "讓他回去舒服的睡覺", "sleep", "逼迫他繼續工作", "force")

    def is_going_to_cutest(self, event):
        text = event.message.text
        return text.lower() == "happy"

    def on_enter_cutest(self, event):
        print("My pig is the cutest")
        reply_token = event.reply_token
        send_1button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "最可愛的豬", "開開心心的小豬超級可愛，榮獲最可愛小豬獎🥰\n並得到一筆獎金", "真的假的！", "really")

    def is_going_to_cold(self, event):
        text = event.message.text
        return text.lower() == "good"

    def on_enter_cold(self, event):
        print("My pig is getting cold")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "糟糕了！", "小豬不小心著涼了，此時你會......", "餵他吃藥", "medicine", "讓他先睡一覺", "take a break")

    def is_going_to_medicine(self, event):
        text = event.message.text
        return text.lower() == "medicine"

    def on_enter_medicine(self, event):
        print("My pig is taking medicine")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "看到藥就想吐", "你的小豬恨透吃藥了，此時你會......", "逼他吃下去", "force", "算了，先讓他睡一覺再說", "take a break")

    def is_going_to_break(self, event):
        text = event.message.text
        return text.lower() == "take a break"

    def on_enter_break(self, event):
        print("My pig is taking a break")
        reply_token = event.reply_token
        send_button_template(reply_token, 'https://i.imgur.com/a/Nb4dS5Y.jpg', "需要補充能量", "你的小豬經過休息後飢腸轆轆，此時你會......", "給他吃高級飼料", "expensive food", "給他吃冰淇淋", "icecream")


    '''
    def on_exit_state2(self):
        print("Leaving state2")
    '''
