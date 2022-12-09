from lib2to3.pgen2.pgen import generate_grammar
from operator import indexOf
from random import random, choice
import subprocess
import json
from unittest import case

class Answer:
    def __init__(self, name, company_size, accounting, creative, it):
        self.name = name
        self.company_size = company_size
        self.accounting = accounting
        self.creative = creative
        self.it = it

    def __str__(self) -> str:
        return (f"Answer submitter: {self.name}\nCompany size: {self.company_size}\nAccount size: {self.accounting}\nCreative size: {self.creative}\nIT size: {self.it}\n---------------------------------------")

# Zakomentirano zbog Authorization failed errora
#res = subprocess.Popen("curl -s --header 'Authorization: Bearer tfp_H16GhjcYXUqvfcPzVwtxU2khsYp6Ar9FpKKwgTwZjZxV_3sqbFdcPSnFS5i' https://api.typeform.com/forms/e88QJ87C/responses", shell=True, stdout=subprocess.PIPE)
#answers = res.stdout.read()

# Answers.json file ima sample odgovora za obradu
answers_file = open("answers.json", "r")
answers_json = json.loads(answers_file.read())


def CheckValidAnswers(answer):

    def SumIndexes(answer):
        acc = accounting_sizes.index(answer.accounting)
        cre = creative_sizes.index(answer.creative)
        it = it_sizes.index(answer.it)

        return acc + cre + it

    def HighestIndex(answer):
        return max(accounting_sizes.index(answer.accounting), creative_sizes.index(answer.creative), it_sizes.index(answer.it))

    company_sizes = ["1-5", "6 - 50", "51 - 250", ">250"]
    accounting_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
    creative_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
    it_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]

    if (answer.company_size == "1-5"):
        if (SumIndexes(answer) > 3 or HighestIndex(answer) > 1): 
            return False
        else:
            return True
    elif (answer.company_size == "6 - 50"):
        if (SumIndexes(answer) > 5 or HighestIndex(answer) > 2): 
            return False
        else:
            return True
    elif (answer.company_size == "51 - 250"):
        if (SumIndexes(answer) > 7 or HighestIndex(answer) > 3): 
            return False
        else:
            return True
    elif (answer.company_size == ">250"):
        return True

def GenerateAnswers():
    num_of_answers = 1000

    company_sizes = ["1-5", "6 - 50", "51 - 250", ">250"]
    accounting_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
    creative_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
    it_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]

    answers_valid = 0
    answers_invalid = 0


    for i in range(num_of_answers):
        name = f"automatedAnswer{i}"
        company_size = choice(company_sizes)
        accounting_size = choice(accounting_sizes)
        creative_size = choice(creative_sizes)
        it_size = choice(it_sizes)
        if ((CheckValidAnswers(Answer(name, company_size, accounting_size, creative_size, it_size)))):
            answers_valid += 1
            #print(Answer(name, company_size, accounting_size, creative_size, it_size))
        else:
            answers_invalid += 1

    print(f"Valid answers: {answers_valid}")
    print(f"Invalid answers: {answers_invalid}")



GenerateAnswers()

#print("---------------- Submissions ----------------")
#for answer in answers_json['items']:
#    print("-------- New submission --------")
#    print(f"Name: {answer['answers'][0]['text']}")
##    try:
 #       print(f"Company size: {answer['answers'][1]['choice']['label']}")
 #   except:
 ##       print("Company size: NOT SET")

#    try:
#        print(f"Accounting Y/N: {answer['answers'][2]['choice']['label']}")
#    except:
#        print("Accounting Y/N: NOT SET")

#    try:
#        print(f"Accounting size: {answer['answers'][3]['text']}")
##    except:
#        print("Accounting size: NOT SET")

#    try:
#        print(f"Creative Y/N: {answer['answers'][4]['choice']['label']}")
#    except:
#        print("Creative Y/N: NOT SET")

#    try:
#        print(f"Creative size: {answer['answers'][5]['text']}")
#    except:
#        print("Creative size: NOT SET")

#    try:
#        print(f"IT Y/N: {answer['answers'][6]['choice']['label']}")
#    except:
#        print("IT Y/N: NOT SET")

#    try:
#        print(f"IT size: {answer['answers'][7]['text']}")
#    except:
#        print("IT size: NOT SET")

#    try:
#        print(f"Current storage solution: {answer['answers'][8]['choice']['label']}")
#    except:
#        print("Current storage solution: NOT SET")