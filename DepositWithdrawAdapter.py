from chatterbot.logic import LogicAdapter
import random
from chatterbot.conversation import Statement
import sys,logging
logging.basicConfig(filename='sora_transaction_bot.log',level=logging.INFO)
class DepositWithdrawAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
    # Only Run when User Enter Exchange related Text

    def can_process(self, statement):
        check_list = ['deposit','transfer', 'change','withdraw']
        statement = statement.text
      
        for i in check_list:
                 if i in statement and ('how' not in statement) and ('fees' not in statement) and ('not' not in statement):
                    logging.info('%s is processabel in depossit/withdraw module',statement)
                    return True
        return False

    def check_from_list(self,selected_statement,list_values):
        for i in list_values:
            if i in selected_statement:
                return i
        return ''
    def get_cardinal(self,selected_statement):
        try:
            import re
            total_amount = re.findall(r"[-+]?\d*\.\d+|\d+", selected_statement)[0]
           
            print('Currency from RE : ',total_amount)
            return total_amount
               
        except IndexError:
            try:
                # Get Numerical Data from String
                from word2number import w2n
                total_amount = w2n.word_to_num(selected_statement)
                print('Currency from w2n : ',total_amount)
                return total_amount
            except:
                total_amount = ''
                return total_amount

    def process(self, input_statement, additional_response_selection_parameters):      

        selected_statement = input_statement.text
    
        confidence = 1

        currency_list = ['anx','bitcoin','btc','usdt','eth','etherium']
        action_list = ['to xchange','to exchange','from exchange','from xchange','to wallet','from wallet']

        action = ""
        currency_type = ""
        total_amount = ""

        action = self.check_from_list(selected_statement,action_list)

     
        currency_type = self.check_from_list(selected_statement,currency_list)

        print('Action : ',action,'\nCurrency Type : ',currency_type)

     
        total_amount = self.get_cardinal(selected_statement)
        response_statement = {
                'action' : action,
                'currency_type': currency_type,
                'currency': total_amount,
            }

        text = Statement(response_statement,confidence)
        confidence = 0
        logging.info('results : %s ',response_statement)
        return  text