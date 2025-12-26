'''
You need to display an important error message: "System failure imminent". You must first check that the message is less than 50 characters, and then display it in all caps.

b. Replace the word 'failure' in the above sentence to "success"

c.Check whether the character(entered by the user) in present in the above sentence or not.

'''
msg = "System failure imminent"
print (msg.count(msg))
print (len(msg) < 50)
print (msg.upper())
new_msg = msg.replace("failure", "success")
print (new_msg)
print (msg.find(input("Type something: ")))
