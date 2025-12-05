from integration.espnApiConnector import EspnApi
from service.LeagueHistoryService import LeagueHistoryService

from espn_api.football import League


# espnApi = EspnApi()

# response = espnApi.getLeagueHistory(1375368, 2022)

# print(response)

service = LeagueHistoryService(1375368, 2024)
service.getYearScores()
