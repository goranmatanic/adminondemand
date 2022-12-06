import subprocess
import json

res = subprocess.Popen("curl -s --header 'Authorization: Bearer tfp_H16GhjcYXUqvfcPzVwtxU2khsYp6Ar9FpKKwgTwZjZxV_3sqbFdcPSnFS5i' https://api.typeform.com/forms/e88QJ87C/responses", shell=True, stdout=subprocess.PIPE)
answers = res.stdout.read()

answers_json = json.loads(answers)

#print(answers_json['items'][0]['answers'][0]['text'])

print("---------------- Submissions ----------------")
for answer in answers_json['items']:
    print("-------- New submission --------")
    print(f"Name: {answer['answers'][0]['text']}")
    try:
        print(f"Company size: {answer['answers'][1]['choice']['label']}")
    except:
        print("Company size: NOT SET")

    try:
        print(f"Accounting Y/N: {answer['answers'][2]['choice']['label']}")
    except:
        print("Accounting Y/N: NOT SET")

    try:
        print(f"Accounting size: {answer['answers'][3]['text']}")
    except:
        print("Accounting size: NOT SET")

    try:
        print(f"Creative Y/N: {answer['answers'][4]['choice']['label']}")
    except:
        print("Creative Y/N: NOT SET")

    try:
        print(f"Creative size: {answer['answers'][5]['text']}")
    except:
        print("Creative size: NOT SET")

    try:
        print(f"IT Y/N: {answer['answers'][6]['choice']['label']}")
    except:
        print("IT Y/N: NOT SET")

    try:
        print(f"IT size: {answer['answers'][7]['text']}")
    except:
        print("IT size: NOT SET")

    try:
        print(f"Current storage solution: {answer['answers'][8]['choice']['label']}")
    except:
        print("Current storage solution: NOT SET")

    #try:
    #    print(f"Marketing size: {answer['answers'][9]['text']}")
    #except:
    #    print("Marketing size: NOT SET")