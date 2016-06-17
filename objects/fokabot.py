"""FokaBot related functions"""
from helpers import userHelper
from objects import glob
from constants import actions
from constants import serverPackets
from constants import fokabotCommands
import re
from helpers import generalFunctions

# Tillerino np regex, compiled only once to increase performance
npRegex = re.compile("^https?:\\/\\/osu\\.ppy\\.sh\\/b\\/(\\d*)")

def connect():
	"""Add FokaBot to connected users and send userpanel/stats packet to everyone"""

	token = glob.tokens.addToken(999)
	token.actionID = actions.idle
	glob.tokens.enqueueAll(serverPackets.userPanel(999))
	####glob.tokens.enqueueAll(serverPackets.userStats(999))

	# NOTE: Debug thing to set all users as connected
	#users = glob.db.fetchAll("SELECT id FROM users")
	#for i in users:
	#	t = glob.tokens.addToken(i["id"])
	#	t.actionID = actions.idle

def disconnect():
	"""Remove FokaBot from connected users"""

	glob.tokens.deleteToken(glob.tokens.getTokenFromUserID(999))

def fokabotResponse(fro, chan, message):
	"""
	Check if a message has triggered fokabot (and return its response)

	fro -- sender username (for permissions stuff with admin commands)
	chan -- channel name
	message -- message

	return -- fokabot's response string or False
	"""

	for i in fokabotCommands.commands:
		# Loop though all commands
		#if i["trigger"] in message:
		if generalFunctions.strContains(message, i["trigger"]):
			# message has triggered a command

			# Make sure the user has right permissions
			if i["rank"] != None:
				# Rank = x
				if userHelper.getRankPrivileges(userHelper.getID(fro)) != i["rank"]:
					return False
			else:
				# Rank > x
				if i["minRank"] > 1:
					# Get rank from db only if minrank > 1, so we save some CPU
					if userHelper.getRankPrivileges(userHelper.getID(fro)) < i["minRank"]:
						return False

			# Check argument number
			message = message.split(" ")
			if i["syntax"] != "" and len(message) <= len(i["syntax"].split(" ")):
				return "Wrong syntax: {} {}".format(i["trigger"], i["syntax"])

			# Return response or execute callback
			if i["callback"] == None:
				return i["response"]
			else:
				return i["callback"](fro, chan, message[1:])

	# No commands triggered
	return False
