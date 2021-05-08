letter = '''
Dear <|Name|>,
Greeting from ABC coding house. I am happy to tell you about your selection
You are selected !
Have a great day ahead !
Thanks and regards,
Bill
Date: <|Date|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)