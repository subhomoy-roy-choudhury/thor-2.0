import json
import sys
import os

thisdir = os.getcwd()
final=str(thisdir)+'\jsons\json_normal'
arr = os.listdir(final)

for i in arr:
    a = os.path.join(final, i)
    print(a)
    with open(a, 'r') as f:
        intents = json.load(f)

    dict1={}
    dict2={}
    list1 = []
    pattern_list = []
    responses_list = []
    i=0
    for key,value in intents.items():
        if key == 'conversations':
            for i in range((len(intents['conversations']))):
                pattern_list = []
                responses_list = []
                tag = str(str(intents['categories'][0])) +" "+str(i)
                patterns = (intents['conversations'][i][:1])
                responses = (intents['conversations'][i][1:])
                print(patterns,tag,responses,i)
                pattern_list.append(patterns)
                responses_list.append(responses)
                dict2 = {"tag":tag,"patterns":patterns,"responses":responses}
                list1.append(dict2)
                print(list1)
        if key == 'categories':

            key = str(intents['categories'][0])
            a='jsons/json_convert/'+str(key) + '.json'
            # dict1.__setitem__(str(key),list1)
            dict1.__setitem__("intents",list1)
    print(intents.keys())



    with open(a, 'w') as outfile:
        json.dump(dict1, outfile,ensure_ascii=False, indent=1)