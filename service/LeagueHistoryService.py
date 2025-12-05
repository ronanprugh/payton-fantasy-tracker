from  espn_api.football import League

class LeagueHistoryService:
    # leagueId = 1375368
    def __init__(self, leagueId, year):
        self.leagueId = leagueId
        self.year = year
        espn_s2 = "AEACjGBB2dAKK5N4qnObSndUqKPWQ9vSwbRMWwgu3rVul9KPA%2BPnzUMF%2BF0lEuNgo8gbGeP8zkKdZSi%2FacekIFe8uIVmW6g0XdmNiSmovw%2BJLGIGAJh5Ud5G2%2FldV%2BW%2FfRqovBaw5%2Fn09aJUiSJ8Mnp2tZHF8CO9q2YzHBGpTy3BRCrmIhjmlMbcr09O3FJvkerSDhJAjEz2QlZxDmXzl6Acea7kZlHovmsh6lPs7aRBsxfmFQq4I1plK2fZO2bixugDXwpsclsJW%2FzfTRuj3cJd"
        swid = "{963AA205-2ED4-4B3B-BAA2-052ED4BB3B7B}"
        self.league = League(league_id=leagueId, year=year, espn_s2=espn_s2, swid=swid)
    
    def getYearScores(self):
        ret = {}
        for team in self.league.teams:
            teamInfo = {}
            teamInfo["teamId"] = team.team_id
            teamInfo["teamName"] = team.team_name
            teamInfo["teamOwner"] = team.owners[0]['firstName'] + " " + team.owners[0]['lastName']
            teamInfo["scores"] = team.scores
            teamInfo["pointsFor"] = team.points_for
            ret[team.team_id] = teamInfo     
        return ret   
        
        