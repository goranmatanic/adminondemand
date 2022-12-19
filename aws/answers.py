from calendar import c
from inspect import getclosurevars
from random import choice
import subprocess
import json

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
    num_of_answers = 100

    for i in range(num_of_answers):
        name = f"automatedAnswer{i}"
        company_size = choice(company_sizes)
        accounting_size = choice(accounting_sizes)
        creative_size = choice(creative_sizes)
        it_size = choice(it_sizes)

        ans = Answer(name, company_size, accounting_size, creative_size, it_size)

        if ((CheckValidAnswers(ans))):
            valid_answers.append(ans)

def QuantifyAnswers():

    for ans in valid_answers:
        com = company_sizes.index(ans.company_size) + 1
        acc = accounting_sizes.index(ans.accounting) + 1
        cre = creative_sizes.index(ans.creative) + 1
        it = it_sizes.index(ans.it) + 1

        ans_value = (com * 90) + (acc * 20) + (cre * 20) + (it * 20)
        ans.setValue(ans_value)

def GenerateRecommendation(answer):

    services = open("services.json", "r")
    services_json = json.load(services)
    services.close()

    def GetClosestValue(ans):

        office_services_abs = []
        creative_services_abs = []

        for service in services_json['services']:
            if (service['category'] == "office"):
                 svc = {"name": service['name'], "abs": f"{abs(ans.value - int(service['value']))}"}
                 #svc = {"name": service['name'], "abs": f"{ans.value - int(service['value'])}"}
                 office_services_abs.append(svc)

            if (answer.creative != "0" and service['category'] == "creative"):
                 svc = {"name": service['name'], "abs": f"{abs(ans.value - int(service['value']))}"}
                 #svc = {"name": service['name'], "abs": f"{ans.value - int(service['value'])}"}
                 creative_services_abs.append(svc)

        sorted_office_services = sorted(office_services_abs, key=lambda d: d['abs'])
        sorted_creative_services = sorted(creative_services_abs, key=lambda d: d['abs'])

        sorted_services = sorted_office_services[:3] + sorted_creative_services[:3]

        return sorted_services

    return GetClosestValue(answer)

    if (answer.value <= 210 and answer.creative != "0"):
        #print("Mala firma sa creative odjelom\nPreporuka neka usluga za manje od 10$ po licenci + Adobe creative cloud")
        #recommended_services = GetClosestValue(answer)
        #print (recommended_services)
        return
    elif (answer.value <= 210):
        #print("Mala firma\nPreporuka neka usluga za manje od 10$ po licenci")
        #recommended_services = GetClosestValue(answer)
        #print (recommended_services)
        return

    if (answer.value <= 360 and answer.creative != "0"):
        #print("Mala - srednja firma sa creative odjelom\nPreporuka neka usluga za manje od 20$ po licenci + Adobe creative cloud")
        #recommended_services = GetClosestValue(answer)
        #print (recommended_services)
        return
    elif (answer.value <= 360):
        #print("Mala - srednja firma\nPreporuka neka usluga za manje od 20$ po licenci")
        #recommended_services = GetClosestValue(answer)
        #print (recommended_services)
        return

    if (answer.value <= 510 and answer.creative != "0"):
       # print("Srednja - velika firma sa creative odjelom\nPreporuka neka usluga za manje od 30$ po licenci + Adobe creative cloud")
        return
    elif (answer.value <= 510):
        #print("Srednja - velika firma\nPreporuka neka usluga za manje od 30$ po licenci")
        return

    if (answer.creative != "0"):
        #print("Velika firma sa creative odjelom\nPreporuka neki najskuplji Office paket + Adobe creative cloud")
        return
    else:
        #print("Velika firma\nPreporuka neki najskuplji Office paket")
        return

GenerateAnswers()
QuantifyAnswers()
for ans in valid_answers:
    rcmd = GenerateRecommendation(ans)
    print(f"For a company with {ans.company_size} employees we recommend the following: ")
    for entry in rcmd:
        print(f"---------------> {entry['name']}")