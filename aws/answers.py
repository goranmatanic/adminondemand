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
        return (f"Answer submitter: {self.name}\nCompany size: {self.company_size}\nAccount size: {self.accounting}\nCreative size: {self.creative}\nIT size: {self.it}\nValue: {self.value}\n---------------------------------------")

    def setValue(self, value):
        self.value = value

# Zakomentirano zbog Authorization failed errora
#res = subprocess.Popen("curl -s --header 'Authorization: Bearer tfp_H16GhjcYXUqvfcPzVwtxU2khsYp6Ar9FpKKwgTwZjZxV_3sqbFdcPSnFS5i' https://api.typeform.com/forms/e88QJ87C/responses", shell=True, stdout=subprocess.PIPE)
#answers = res.stdout.read()

# Answers.json file ima sample odgovora za obradu
#answers_file = open("answers.json", "r")
#answers_json = json.loads(answers_file.read())

# Varijabla za spremanje validnih odgovora
valid_answers = []

company_sizes = ["1-5", "6 - 50", "51 - 250", ">250"]
accounting_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
creative_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]
it_sizes = ["0", "1-5", "6 - 50", "51 - 250", ">250"]

def CheckValidAnswers(answer):

    def SumIndexes(answer):
        acc = accounting_sizes.index(answer.accounting)
        cre = creative_sizes.index(answer.creative)
        it = it_sizes.index(answer.it)

        return acc + cre + it

    def HighestIndex(answer):
        return max(accounting_sizes.index(answer.accounting), creative_sizes.index(answer.creative), it_sizes.index(answer.it))

    if (SumIndexes(answer) == 0): 
        return False

    if (answer.company_size == "1-5"):
        if (SumIndexes(answer) > 3 or HighestIndex(answer) > 1): 
            return False
        else:
            return True
    elif (answer.company_size == "6 - 50"):
        if (SumIndexes(answer) > 6 or HighestIndex(answer) > 2): 
            return False
        else:
            return True
    elif (answer.company_size == "51 - 250"):
        if (SumIndexes(answer) > 9 or HighestIndex(answer) > 3): 
            return False
        else:
            return True
    elif (answer.company_size == ">250"):
        return True

def GenerateAnswers():
    num_of_answers = 5000

    for i in range(num_of_answers):
        name = f"automatedAnswer{i}"
        company_size = choice(company_sizes)
        accounting_size = choice(accounting_sizes)
        creative_size = choice(creative_sizes)
        it_size = choice(it_sizes)

        ans = Answer(name, company_size, accounting_size, creative_size, it_size)

        if ((CheckValidAnswers(ans))):
            valid_answers.append(ans)

    print(f"Valid answers: {len(valid_answers)}")

def QuantifyAnswers():

    for ans in valid_answers:
        com = company_sizes.index(ans.company_size) + 1
        acc = accounting_sizes.index(ans.accounting) + 1
        cre = creative_sizes.index(ans.creative) + 1
        it = it_sizes.index(ans.it) + 1

        ans_value = (com * 90) + (acc * 20) + (cre * 20) + (it * 20)
        ans.setValue(ans_value)

def PrintAnswers():
    small_companies = []
    small_mid_companies = []
    mid_big_companies = []
    big_companies = []

    for ans in valid_answers:
        if (ans.company_size == "1-5"):
            small_companies.append(ans)
            #print(ans)
        elif (ans.company_size == "6 - 50"):
            small_mid_companies.append(ans)
            #print(ans)
        elif (ans.company_size == "51 - 250"):
            mid_big_companies.append(ans)
            #print(ans)
        elif (ans.company_size == ">250"):
            big_companies.append(ans)
            #print(ans)

    sum_small = 0
    sum_small_mid = 0
    sum_mid_big = 0
    sum_big = 0

    for ans in small_companies:
        sum_small += ans.value

    for ans in small_mid_companies:
        sum_small_mid += ans.value
        
    for ans in mid_big_companies:
        sum_mid_big += ans.value
        
    for ans in big_companies:
        sum_big += ans.value

    #print(f"Average small company value: {sum_small/len(small_companies)}")
    #print(f"Average small_mid company value: {sum_small_mid/len(small_mid_companies)}")
    #print(f"Average mid_big company value: {sum_mid_big/len(mid_big_companies)}")
    #print(f"Average big company value: {sum_big/len(big_companies)}")

def GenerateRecommendation(answer):
    if (answer.value <= 210 and answer.creative != "0"):
        print("Mala firma sa creative odjelom")
        return
    elif (answer.value <= 210):
        print("Mala firma")
        return

    if (answer.value <= 360 and answer.creative != "0"):
        print("Mala - srednja firma sa creative odjelom")
        return
    elif (answer.value <= 360):
        print("Mala - srednja firma")
        return

    if (answer.value <= 510 and answer.creative != "0"):
        print("Srednja - velika firma sa creative odjelom")
        return
    elif (answer.value <= 510):
        print("Srednja - velika firma")
        return

    if (answer.creative != "0"):
        print("Velika firma sa creative odjelom")
        return
    else:
        print("Velika firma")

GenerateAnswers()
QuantifyAnswers()
PrintAnswers()
for ans in valid_answers:
    GenerateRecommendation(ans)