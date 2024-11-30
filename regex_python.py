#created by manu nair
import re

message_string = "ememnair.  gma il"
regex_string = "[^a-zA-Z0-9]+"
regex_pattern = re.compile(regex_string)
if (re.search(regex_pattern, message_string)):
    print("Yes")
else:
    print("No")

print(re.search(regex_pattern, message_string))
print(re.match(regex_pattern, message_string))

print(re.sub('nair','',message_string))
print(re.sub('emem','mm',message_string))
print(re.sub(r'\s+','',message_string))
print(re.sub('ememn(air)air', r'\1' ,message_string))