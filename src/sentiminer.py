#!/usr/bin/env python3


import csv, sys, re, random

DATE = "16 March 2022"
VERSION = "ii"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")

WHATISTHIS_p1 = f"""
\t {THISPROG}
\t Program to study sentiment in text and output a score
"""
WHATISTHIS_p2 = "\t Use option '-h' for more glorification about this amazing project!\n"


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIYellow = '\033[1;93m'     # Yellow
BIGreen='\033[1;92m'      # Green
BIBlue='\033[1;94m'       # Blue
BICyan='\033[1;96m'       # Cyan
BIRed='\033[1;91m'        # Red
BIWhite='\033[1;97m'      # White
White='\033[0;37m'        # White



banner1_str = """

  ███████╗███████╗███╗   ██╗████████╗██╗███╗   ███╗██╗███╗   ██╗███████╗██████╗
  ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
  ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
  ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
  ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/



def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


def bannerScreen(myCount_int):
	"""prints a charming and colourful little message for the user"""
	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		for i in range(myCount_int):
			randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
			print(randomColour_str + banner1_str + BIWhite)
	else:
		print(banner1_str)
#end of bannerScreen()




def helper():
	"""Cheap online help; how to use the program"""
	bannerScreen(1) # print up one banner screen
	print(WHATISTHIS_p1)
	h_str1 = "\t"+DATE+" | version: "+VERSION
	h_str2 = "\t"+AUTHOR +"\n\tmail: "+AUTHORMAIL
	print("\t"+len(h_str2) * "-")
	print(printWithColour(BIYellow,h_str1))
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")
	print("\tOptions:")
	print("\t[-H]: This page.")
	print("\t[-S]: Ask me to enter a sentence to test.\n")
	print("\t[<textFile>]: Enter a text file to test.\n")
	print(printWithColour(BIGreen,f"\t[+] \U0001f600 USAGE: python3 {THISPROG} textFile.txt"))
	print(printWithColour(BIGreen,f"\t[+] \U0001f600 USAGE: python3 {THISPROG} -S "))

#end of helper()



def getArguments(argv_list):
	""" A function to determine what parameters have been entered. There are two main options to check for at execution time: the name of the TXT file, a manually entered sentence to test, or whether the user wants some help."""

	# print(argv_list)

	param_1 = "TXT" # call for cvsReader()
	param_2 = "-H" # call for helper()
	param_3 = "-S" # call for helper()

	if len(argv_list) == 0:
		# Output welcome message
		# print(printWithColour(BICyan,WHATISTHIS_p1))
		print(printWithColour(BICyan,WHATISTHIS_p2))

	# helperFlag_Bool = False
	text_list = None # file to open
	for i in argv_list:
		# print(BIRed + f"Checking <<{i}>>" + White)

		if param_1 in i.upper(): #entered filename
			# print(i)
			myFile_str = i
			print(printWithColour(BIGreen,"\t [+]"),printWithColour(BICyan, f"Entered text file: {i}"))
			text_list = getFile(i)

		if param_2 == i.upper(): # get some help
			# print(f"\t Call to help found: {i}")
			# helperFlag_Bool = True
			helper()
			exit()

		if param_3 == i.upper(): # Prompt to enter a sentence
			# print(f"\t Call to help found: {i}")
			# helperFlag_Bool = True
			# print("enter sentence")
			text_list = getSentence()

		# if param_1 not in i.upper() and param_2 not in i.upper():
		# 	print(printWithColour(BICyan,WHATISTHIS_p2))

		if text_list != None:
			begin(text_list)

			# end of getArguments()

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
		'darwin' : 'OSX',
		'win32'  : 'Windows',
		'linux1' : 'Linux',
		'linux2' : 'Linux'
	}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()


def getSentiments(csvfile):
	"""opens the file csv file containing finn sentiment words"""
	word_dict = {}
	with open(csvfile, newline='') as csvfile:
		datareader = csv.reader(csvfile, delimiter=',')
		for row in datareader:
			word_dict[row[0]] = row[1]
	return word_dict
#end of getSentiments()



def getSentence():
	"""ask the user to enter something to evaluate"""
	data_str = input("\tEnter a sentence to scan for sentiment : ")
	print(printWithColour(BIGreen,"\t [+]"),printWithColour(BIYellow, f"Your input is:"),printWithColour(BIBlue,f"{data_str}"))

	return data_str.split() #return a list
#end of getSentence()



def getFile(fname):
	"""open textfile name to load and extract text"""
	#fname = input("  Enter the name of the file :")
	data_str = ""
	try:
		with open(fname) as file:
			for line in file:
				data_str = data_str + line
				data_str = data_str.replace("\n"," ")
		#print("contents: ",data_str, type(data_str))
	except FileNotFoundError:
		print(printWithColour(BIRed,"\t [+]"), printWithColour(BIYellow,"Error finding the file... exiting"))
		exit()
	data_str = data_str.lower()
	#remove basic punctuation
	punctuation = "!`':,?.()/\\"
	for p in punctuation:
		data_str = data_str.replace(p," ")
	return data_str.split() # return a list
#end of getFile()



def studySentiment(text_list, sentiments_dict):
	"""function to to determine the sentiment score from the text."""
	score = 0 # current score of the sentimental words
	hits = 0 # the number of words which have a sentiment value
	for i in text_list:
		#print("   Current word: ",i)
		try:
			wordScore_int = int(sentiments_dict[i])
			print(printWithColour(BICyan,f"\t    ~ {i}, score:"),printWithColour(BIBlue,f"{wordScore_int}"))
			score =  score + wordScore_int
			hits = hits + 1
		except KeyError:
			#print("  <<",i,">> Word not found in sentiments_dict...")
			pass
	print("\t\t" + "- -" * 20)
	try:
		print(printWithColour(BIGreen,"\t [+]"), printWithColour(BIYellow,f"Hits (number of sentiment words) : {hits}"))
		print(printWithColour(BIGreen,"\t [+]"), printWithColour(BIYellow,f"Score : {score}"))
		print(printWithColour(BIGreen,"\t [+]"), printWithColour(BIYellow,f"Score/hits : {score/hits}"))
	except ZeroDivisionError:
		print(printWithColour(BIRed,"\t [+]"), printWithColour(BIYellow,f"Not enough input to function ... :-("))
		exit()
#end of studySentiment()



def begin(text_list):
	"""Begin the program."""
	print(printWithColour(BIGreen,"\t [+]"), printWithColour(BIYellow, f"Contents : {text_list}, {type(text_list)}"))
	csvfile = "finn.csv"
	sentiments_dict = getSentiments(csvfile)
	print(printWithColour(BIGreen,"\t [+]"),printWithColour(BIYellow, f"Analyzing the sentiment score of text..."))
	studySentiment(text_list, sentiments_dict)

#end of begin()




if __name__ == '__main__':
	getArguments(sys.argv[1:])




# command line paramters code
###################################
#import itertools, sys
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator
#from collections import namedtuple


#
# if __name__ == '__main__':
#
#     if len(sys.argv)  == 2: #user enters a sentence
#         begin(sys.argv[1])
#         exit()
#
#     if len(sys.argv) == 3: #two options ["f", "filename"] added to command line
#        begin(sys.argv[1],sys.argv[2])
#     else:
#     #if len(sys.argv) == 2: #one option added to command line
#     #   begin(sys.argv[1])
#     #else:
#        help()
#        sys.exit(0)
#






# plotting notes...

#n_groups = 5

#means_men = (20, 35, 30, 35, 27)
#std_men = (2, 3, 4, 1, 2)

#means_women = (25, 32, 34, 20, 25)
#std_women = (3, 5, 2, 3, 3)

#fig, ax = plt.subplots()

#index = np.arange(n_groups)
#bar_width = 0.35

#opacity = 0.4
#error_config = {'ecolor': '0.3'}

#rects1 = ax.bar(index, means_men, bar_width,
#                alpha=opacity, color='b',
#                yerr=std_men, error_kw=error_config,
#                label='Men')

#rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                alpha=opacity, color='r',
#                yerr=std_women, error_kw=error_config,
#                label='Women')

#ax.set_xlabel('Group')
#ax.set_ylabel('Scores')
#ax.set_title('Scores by group and gender')
#ax.set_xticks(index + bar_width / 2)
#ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
#ax.legend()

#fig.tight_layout()
#plt.show()
