import json

with open('wocka.json', 'r') as f: # Why is it called that?
    jokes = json.load(f)

with open('stupidstuff.json', 'r') as f:
    stupid_jokes = json.load(f)

with open('reddit_jokes.json', 'r') as f:
    reddit_jokes = json.load(f)

categorys = []

reddit_jokes = [{**d, 'category': 'reddit'} for d in reddit_jokes] # add reddit category

jokes = [d for dict_list in [reddit_jokes, stupid_jokes, jokes] for d in dict_list] # Add togehter

with open('jokes.json', 'w') as f: # save it...
    json.dump(jokes, f, indent = 2)

# Stats stuff

print('I have {} Jokes.'.format(len(jokes)))

def getCountOfCategory(category):
    return len([joke for joke in jokes if joke['category'] == category])

categorys = []
for joke in jokes:
    if joke['category'] not in categorys:
        categorys.append(joke['category'])

print('I have these categorys: '+', '.join(categorys))
for category in categorys:
    print('Category {} has {} jokes.'.format(category, getCountOfCategory(category)))
