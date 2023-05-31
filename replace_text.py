import re
f=open('hello.txt','r')
file_text=f.read()

print(file_text)
replacedBy="I am the new replaced text"

new_text=file_text.replace('model_lib',replacedBy)
new_text_re=re.sub('model_main_lib',replacedBy,new_text)

print(new_text_re)
print(new_text)
