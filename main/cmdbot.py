import random
import json

import torch

from supporting_files.chatbot.model import NeuralNet
from supporting_files.chatbot.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('supporting_files/command.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "pretrained_models/data1_cmd.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Thor"
# print("Let's chat! (type 'quit' to exit)")

def command_dl(sentence1):
    sentence = sentence1
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                # print(f"{bot_name}: {random.choice(intent['responses'])}")
                response = intent['tag']
                return response

    else:
        # print(f"{bot_name}: I do not understand...")
        response = sentence1
        return response

if __name__ == '__main__':
    while True:
        command =str(input(f'{bot_name}: '))
        result=str(command_dl(command))
        print(f'you : {result}')