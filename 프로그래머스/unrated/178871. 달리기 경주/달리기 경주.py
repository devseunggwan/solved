def solution(players, callings):
    dict_players = {player: score for score, player in enumerate(players)}
    
    for called in callings:
        score1, score2 = dict_players[called], dict_players[called] - 1
        players[score1], players[score2] = players[score2], players[score1]
        dict_players[players[score1]], dict_players[players[score2]] = dict_players[players[score2]], dict_players[players[score1]]
        
    return players