from chatterbot import ChatBot,response_selection
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import logging,datetime
from chatterbot.comparisons import levenshtein_distance
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.comparisons import sentiment_comparison
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import logging
import DepositWithdrawAdapter
import RatcliffObershelp as ratcliffobershelp


logging.basicConfig(filename='sora_bot.log',level=logging.INFO)

d_response=["i am in beta version, i don't know a lot.",
"Maybe you can ask something else.",
"i am sorry but i didn't really get your point."]


chat_bot = ChatBot(
	'Angelium',
	read_only=True,
	preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        'chatterbot.preprocessors.unescape_html'
    ],
 logic_adapters=[
       {
           'import_path':'DepositWithdrawAdapter.DepositWithdrawAdapter',},
            {
                'import_path' : 'chatterbot.logic.BestMatch',
                'statement_comparison_function' : ratcliffobershelp.Ratcliff_Obershelp,
                "response_selection_method": response_selection.get_random_response,
                "default_response":d_response,
                "maximum_similarity_threshold":0.80
            },
            
    ]

)



def train_data():
    trainer = ChatterBotCorpusTrainer(chat_bot)
    #trainer=ListTrainer(chat_bot)
    trainer.train("./Data_1.4.yml")
    print("training completed, use bot.py to talk to bot.")




def exporting_data():
	trainer.export_for_training('./{}export.json'.format(datetime.datetime.now()))

train_data()

