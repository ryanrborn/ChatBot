import nltk
import random

class Chatbot:
	"The Chatbot"
	numRounds = 0
	rounds = []
	sentenceTokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
	user = ""
	topics = ['pizza', 'hamburgers', 'mexican', 'mediterranean', 'italian', 'sandwiches']
	places = {
		"pizza" : [
			"Little Caesars by the north Walmart",
			"Papa Johns on Main",
			"Papa Murphy's on Main",
			"Fox's Den Pizza by the Hospital",
			"Factory Pizzeria on Main",
			"Pier 49 by the south Walmart",
			"Fredrico's Pizza by the canyon",
			"Firehouse Pizzeria on Main"
		],
		"hamburgers" : [
			"Wendy's on Main and 1400 N",
			"The Beehive Grill on Main",
			"Burger King on Main and 200 S",
			"Carl's Junior on Main and 1400 N",
			"A&W on Main and 700 N",
			"Chili's on Main and 1400 N",
			"Center Street Grill on Main and Center"
		],
		"mexican" : [
			"Cafe Rio on Main and 1400 N",
			"Costa Vida by Shopco",
			"Cafe Sabor on 600 W and Center",
			"El Sol on Main and 900 N",
			"Taco Time by Hastings",
			"La Tormenta by the north Walmart",
			"Beto's on Main and 1100 N"
		],
		"mediterranean" : [
			"Romo's on Main and 700 N"
		],
		"italian" : [
			"Le Nonne by the tabernacle",
			"Gia's on Main and 100 S",
			"Olive Garden on Main and 1200 N"
		],
		"sandwiches" : [
			"Subway on Main and 400 N",
			"Firehouse Subs on Main and 1250 N"
		]
	}

	def __init__(self):
		start = {"user":"","bot":"Hi, I'm a Chatbot that's knowledgable in places to eat in Logan, what's your name?."}
		self.rounds.append(start)

	def getQuestion(self):
		return self.rounds[len(self.rounds)-1]["bot"]

	def userResponse(self, response):
		response = response.strip()
		roundObj = {"user":response,"bot":"I'm not sure what you're talking about"}

		# determine bot's response here, add it to "bot" member of roundObj
		sentences = self.sentenceTokenizer.tokenize(response)
		for sent in sentences:
			if(sent == "quit"):
				print "See ya " + self.user
				return False
			tagged = nltk.tag.pos_tag(sent.split())
			user = self.findName(tagged)
			if(user != False):
				self.user = user
				roundObj["bot"] = "Hi " + user + ", what do you like to eat?"
				break;
			roundObj["bot"] = self.findRecognizedTopics(tagged)

		self.rounds.append(roundObj)

		self.numRounds += 1
		return True

	def findName(self, tagged):
		for part in tagged:
			if(part[1] == "NNP"):
				return part[0]
		return False

	def findRecognizedTopics(self, tagged):
		for part in tagged:
			if(part[1] == "NN" or part[1] == "NNS" or part[1] == "JJ"):
				if(part[0] in self.topics):
					return "Have you tried " + random.choice(self.places[part[0]])
				return "I don't know what " + part[0] + " means"
		return "I'm not sure what you're talking about"