from slixmpp import ClientXMPP
from llama_cpp import Llama
from translate import Translator
from langdetect import detect

login = "login@host.com"
passw = "password"

model = "tinyllama.gguf"
tokens = 256
descrption = "Информация о боте:\nЭтот чат бот сделан на основе TinyLLaMA с 1.1 триллионом параметров. Но он с обычным общением почему то плох, ему лучше задавать только вопросы, и то, он с вами может только по английскому разговаривать.\nСам сервер ограничел TinyLLaMA на 256 токенов и квантовым размером в Q4, из-за того что сама нейросеть хостится на телефоне, поэтому придётся ждать где-то 1 – 2 минуты чтобы нейросеть отправила результат.\n\nУдачного вам использования бота!"

class LLaMABot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)
        self.llm = Llama(
            model_path=model
        )

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            if msg['body'] == '//info':
                msg.reply(descrption).send()
            else:
                qlang = detect(msg['body'])
                questt = Translator(from_lang=qlang, to_lang="en").translate(msg['body'])
                questi = "Q: " + questt + " A: "

                output = self.llm(
                    questi,
                    max_tokens=tokens,
                    stop=["Q:"],
                    echo=True
                )
            
                questo = output['choices'][0]['text']
                msg.reply(questo[len(questi):]).send()

if __name__ == '__main__':
    xmpp = LLaMABot(login, passw)
    xmpp.connect()
    xmpp.process()
