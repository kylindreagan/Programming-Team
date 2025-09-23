teams, games = map(int, input().split())

total_teams = {"T" + str(i):i for i in range(1,teams+1)}

for i in range(games):
    winner, loser = input().split()
    win_rank, lose_rank = total_teams[winner], total_teams[loser]
    if win_rank > lose_rank:
        total_teams[loser] = win_rank
        t = dict((team, rank-1) if win_rank > rank > lose_rank else (team, rank) for team, rank in total_teams.items())
        total_teams = t
        total_teams[winner] = win_rank - 1

teamSort = sorted(total_teams.items(), key=lambda x:x[1], reverse=False)

for team in teamSort:
    print(team[0], end=" ")