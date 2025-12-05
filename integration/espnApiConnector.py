import requests
from exception.Exception import *

class EspnApi:
    
    def __init__(self):
        self.baseUrl = "https://fantasy.espn.com/apis/v3/games/ffl"
    
    def getLeagueHistory(self, leagueId, seasonId):
        endpoint = "/leagueHistory"
        
        fullUrl = self.baseUrl + endpoint + f"?leagueId={leagueId}&seasonId={seasonId}"
        self.__getResponse__(fullUrl)
        
        
            
    def __getResponse__(self, url):
        try:
            response = requests.get(url)
            return response
        except:
            raise ServiceException(f"Could not connect to {self.baseUrl}")