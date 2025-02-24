from bardapi import Bard

token = ""
bard = Bard(token=token)
response = bard.get_answer("What is Machine Learning?")['content']
print(response)
