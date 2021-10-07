from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterbotCorpusTrainer
my_bot = CharBot(name = 'PyBot', read_only = True,login_adapters=['chatBot.login.MathematicalEvaluation','chatterbot.login.Besrmatch'])
small_talk = ['hi there!',
                'Namaste!','how do you do?','how are you?','i\'m cool','i\'m ok','glad to hear that.','i\'m fine','sorry to hear that.','i\'pybot. ask me a math question, please.']
talk_1 = ['Best Instagram page','Everyone know its codeslearning']
list_trainer = ListTrainer(my_bot)

for item in (small_talk, talk_1):
    list_trainer.train(item)
corpus_trainer = ChatterbotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("Namaste"))
print(my_bot.get_response("I feel Awesome Today"))
print(my_bot.get_response("What your name"))