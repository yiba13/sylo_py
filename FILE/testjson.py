#!/usr/bin/env python3

import json 
courses = {1:'Linux',2:'Git',3:'Vim'}

js = json.dumps(courses)
print(js,'\n',type(js))

with open('courses.json','w') as f:
    nu = f.write(json.dumps(courses))
    print(nu)

with open('course1.json','w') as f:
    json.dump(courses,f)

data1= json.loads(js)
print(data1)

with open('courses.json','r') as f:
    data2 = json.load(f)

print(data2)
