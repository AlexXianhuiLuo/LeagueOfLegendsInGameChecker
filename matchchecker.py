import requests
import json

class InGameChecker:
    def __init__(self):
        #API Stuff
        self.apiEndpoint = "https://na1.api.riotgames.com"
        self.summonerExtension = "/lol/summoner/v4/summoners/by-name/"
        self.spectatorExtension = "/lol/spectator/v4/active-games/by-summoner/"

        """
        TODO: EITHER CREATE A FILE CALLED 'credentials.txt' WITH THE VALUES 'key, {API KEY HERE}' 
        OR JUST DELETE THE FOLLOWING LINES OF CODE UP TO THE LINE 'self.header = {"X-Riot-Token": key}' AND REPLACE THE KEY
        """
        f = open("LeagueDiscordBot\credentials.txt", "r")
        vals = f.read().split(", ")
        for x in range(len(vals)):
            if vals[x] == "key":
                key = vals[x + 1]

        self.header ={
            "X-Riot-Token": key # REPLACE THIS WITH YOUR API KEY
        }

    """
    @param: the name of the summoner to check
    @returns: a boolean representing whether or not they are currently in game

    A method that checks whether or not a summoner is currently in game
    """
    def check(self, summonerName : str):
        spectatorReq = requests.get(self.apiEndpoint + self.spectatorExtension + self.getId(summonerName), headers = self.header)
        if spectatorReq.ok:
            return True
        elif spectatorReq.status_code == 404:
            return False
        else:
            # Something Went Wrong
            print(spectatorReq.reason)
            return False

    """
    @param: the summoner name to get the id of
    @returns: the id of the summoner

    currently this method just serves as a helper method

    NOTE: There are 3 types of ids that riot uses, the 'id', 'accountId', and 'puuid', this returns the 'id'
    """
    def getId(self, summonerName : str):
        idReq = requests.get(self.apiEndpoint + self.summonerExtension + summonerName, headers = self.header)
        info = json.loads(idReq.text)
        print(info)
        return info["id"]