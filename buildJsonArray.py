import json

# Remove the 'Comment Submitted by ' portion from Title
def cleanAuthorName(title):
	if title.startswith("Comment Submitted by "):
		return title[21:]
	elif title.startswith(": Comment Submitted by "):
		return title[23:]
	else:
		return title

# Return cleaned JsonArray and Fields
def getTextAndId(inputDict):

	# List of Texts and Ids
	myTextList   = []
	myIdList     = []
	myAuthorList = []
	
	# Incorrect Format Comments
	errorComments = 0

	# Read Dictionary
	for key, value in inputDict.iteritems():
		try:
			myText  = value["commentText"]
			myTitle = cleanAuthorName( value["title"] )
			myTextList.append(myText)
			myIdList.append(key)
			myAuthorList.append(myTitle)
		except:
			errorComments += 1
	print "Incorrect Format Comments: ", errorComments

	# Convert to JSON String
	jsonStringText = json.dumps(myTextList)
	
	return {'jsonTextList': jsonStringText, 'idList': myIdList, 'textList': myTextList, 'authorList': myAuthorList}
	
	
