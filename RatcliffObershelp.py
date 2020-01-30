from textdistance import ratcliff_obershelp

class Comparator:

    def __call__(self, statement_a, statement_b):
        return self.compare(statement_a, statement_b)

    def compare(self, statement_a, statement_b):
        return 0
        
class Ratcliff_Obershelp(Comparator):


    def compare(self, statement, other_statement):
        # Get the lowercase version of both strings
        statement_text = str(statement.text.lower())
        other_statement_text = str(other_statement.text.lower())

        result = ratcliff_obershelp(statement_text, other_statement_text)
        # Return your calculated value here
        return result

# ---------------------------------------- #

ratcliffobershelp = Ratcliff_Obershelp()