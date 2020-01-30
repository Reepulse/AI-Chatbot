from chatterbot import ChatBot,response_selection
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.comparisons import sentiment_comparison
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import logging,datetime
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


def is_balance(text):
	words = ['my', 'balance']
	if all(x in text.split() for x in words):
		return True
	else:
		return False


def final_response(text):
	if is_balance(text):
		return "Your total balance is $##TOTAL_BALANCE##"
	else:
		response = chat_bot.get_response(text)
		return response


print("\n\n\n\n you can talk to sora and type exit to quit.\n\n")
while True:
    input_text = input("you : ")
    if(input_text == "exit"):
        print("sora : Nice to meet you")
        break
    print("sora :", final_response(input_text),"\n")
