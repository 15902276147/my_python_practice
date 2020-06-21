import json 

try: 
    with open('./jinpeng.json','r') as f : 
        result = f.readline() 
        json_info = json.loads(result) 
        print (json_info) 

except Exception as e : 
    print (e)