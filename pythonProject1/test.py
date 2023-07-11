#XQhUzb6Ln3wczkAgwLr6NzAHkrVHl8fTsgrAOUNTSGsIRT8ythQEPMNGjjIpodybYJG5jA.
from bardapi import Bard

token = 'XQhUzb6Ln3wczkAgwLr6NzAHkrVHl8fTsgrAOUNTSGsIRT8ythQEPMNGjjIpodybYJG5jA.'
bard = Bard(token=token)
response = bard.get_answer("What is Machine Learning?")['content']
print(response)