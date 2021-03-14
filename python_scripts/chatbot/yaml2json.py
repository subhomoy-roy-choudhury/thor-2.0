import json
import os
import sys
import yaml


thisdir = os.getcwd()
final=str(thisdir)+'\yamls'
arr = os.listdir(final)

for i in arr:
    a = os.path.join(final, i)
    print(a)
    if os.path.exists(a):
        source_file = open(a, "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    else:
        print("ERROR: " + str(i)+ " not found")
        exit(1)

    # Processing the conversion
    output = json.dumps(source_content,ensure_ascii=False, indent=2)
    b='jsons/json_normal/'+str(i) + '.json'
    target_file = open(b, "w")
    target_file.write(output)
    target_file.close()

 
