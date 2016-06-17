"""Contain server and client packet IDs"""
client_changeAction = 0
client_sendPublicMessage = 1
client_logout = 2
client_requestStatusUpdate = 3
client_pong = 4
server_userID = 5
server_commandError = 6
server_sendMessage = 7
server_ping = 8
server_handleIRCUsernameChange = 9
server_handleIRCQuit = 10
server_userStats = 11
server_userLogout = 12
server_spectatorJoined = 13
server_spectatorLeft = 14
server_spectateFrames = 15
client_startSpectating = 16
client_stopSpectating = 17
client_spectateFrames = 18
server_versionUpdate = 19
client_errorReport = 20
client_cantSpectate = 21
server_spectatorCantSpectate = 22
server_getAttention = 23
server_notification = 24
client_sendPrivateMessage = 25
server_updateMatch = 26
server_newMatch = 27
server_disposeMatch = 28
client_partLobby = 29
client_joinLobby = 30
client_createMatch = 31
client_joinMatch = 32
client_partMatch = 33
#server_lobbyJoin_obsolete = 34
#server_lobbyPart_obsolete = 35
server_matchJoinSuccess = 36
server_matchJoinFail = 37
client_matchChangeSlot = 38
client_matchReady = 39
client_matchLock = 40
client_matchChangeSettings = 41
server_fellowSpectatorJoined = 42
server_fellowSpectatorLeft = 43
client_matchStart = 44
AllPlayersLoaded = 45
server_matchStart = 46
client_matchScoreUpdate = 47
server_matchScoreUpdate = 48
client_matchComplete = 49
server_matchTransferHost = 50
client_matchChangeMods = 51
client_matchLoadComplete = 52
server_matchAllPlayersLoaded = 53
client_matchNoBeatmap = 54
client_matchNotReady = 55
client_matchFailed = 56
server_matchPlayerFailed = 57
server_matchComplete = 58
client_matchHasBeatmap = 59
client_matchSkipRequest = 60
server_matchSkip = 61
server_unauthorised = 62
client_channelJoin = 63
server_channelJoinSuccess = 64
server_channelInfo = 65
server_channelKicked = 66
server_channelAvailableAutojoin = 67
client_beatmapInfoRequest = 68
server_beatmapInfoReply = 69
client_matchTransferHost = 70
server_supporterGMT = 71
server_friendsList = 72
client_friendAdd = 73
client_friendRemove = 74
server_protocolVersion = 75
server_mainMenuIcon = 76
client_matchChangeTeam = 77
client_channelPart = 78
client_receiveUpdates = 79
server_topBotnet = 80
server_matchPlayerSkipped = 81
client_setAwayMessage = 82
server_userPanel = 83
IRC_only = 84
client_userStatsRequest = 85
server_restart = 86
client_invite = 87
server_invite = 88
server_channelInfoEnd = 89
client_matchChangePassword = 90
server_matchChangePassword = 91
server_silenceEnd = 92
client_specialMatchInfoRequest = 93
server_userSilenced = 94
server_userPresenceSingle = 95
server_userPresenceBundle = 96
client_userPanelRequest = 97
client_userPresenceRequestAll = 98
client_userToggleBlockNonFriendPM = 99
server_userPMBlocked = 100
server_targetIsSilenced = 101
server_versionUpdateForced = 102
server_switchServer = 103
server_accountRestricted = 104
server_jumpscare = 105
client_matchAbort = 106
server_switchTourneyServer = 107
client_specialJoinMatchChannel = 108
client_specialLeaveMatchChannel = 109
