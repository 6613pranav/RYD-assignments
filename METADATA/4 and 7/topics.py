import re
import json
print('Topics covered in the book are:')
filename="General_Science_Multiple_Choice_Question_Bank_for_General_CompeSSC"
f = open('C:/Users/DELL/Downloads/'+filename+'.txt', "r", encoding='utf-8')
data = f.read()
text = data.split('\n')
temp=[]
list=['Contents','Content','CONTENT','Index','index','Table of Contents']

for i in list:
        if i in text:
            st = text.index(i) + 2
            g = text[st:]
            break



c=0
try:
    for i in g:
         if i.startswith('\x0c'):
             break
         for j in range(len(temp)):
             if (i != '' and i!=' ') and re.search(i, temp[j]):
                if re.match(r'\d', i):
                    continue
                else:
                    #print(i)
                    c = 1
                    break
         if(c==0):
             temp.append(i)
         else:
             break
except:
    print('Questions regarding ', filename)
t=('\n').join(temp)
print(t)
