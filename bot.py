import random
import re
import nltk

indents = {
    'hello' : {
        'input' : ['hello', 'hay', 'how are you?'],
        'output' : ['hey', 'hello', "what's up?"]
    },
    'weather' : {
        'input' : ['find out the weather', "what's the weather like", 'weather'],
        'output' : ['weather is good', 'optimal weather']
    }
}

def clean_up(text):
    text = text.lower()
    re_not_word = r'[^\w\s]'
    text = re.sub(re_not_word, '', text)
    return text

def text_match(user_text, input):
    user_text = clean_up(user_text)
    input = clean_up(input)

    if user_text.find(input) != -1:
        return True
    
    if input.find(user_text) != -1:
        return True

    input_len = len(input)
    difference = nltk.edit_distance(user_text, input)

    return (difference / input_len) < 0.4


INTENTS = {
    'hello': {
        'examples': ['hello', 'hey'],
        'responses': ['hello', "afternoon"]
    },
    'hay': {
        'examples': ['how are you?', 'what is your mood'],
        'responses': ['it seems nothing', 'Okay, how are you?']
    },
    'exit': {
        'examples': ['exit', ''],
        'responses': ['good bye!', 'bye']
    }
}

def get_intent(text):
    for intent in INTENTS:
        for example in INTENTS[intent]['examples']:
            if text_match(text, example):
                return intent


def get_response(intent):
    return random.choice(INTENTS[intent]['responses'])

text = input('< ')
intent = get_intent(text)
answer = get_response(intent)
print('>', answer)

while not text_match(text, 'Выход'):
    text = input('< ')
    intent = get_intent(text)
    answer = get_response(intent)
    print('>', answer)