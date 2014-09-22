#! /usr/bin/env python
# Ryan Born
# A00976358
# ChatBot


import chatbot


chatbot = chatbot.Chatbot()

i = 0

while True:
	question = chatbot.getQuestion()
	userResponse = raw_input(question+"\n")
	cont = chatbot.userResponse(userResponse)
	if(cont == False):
		break

