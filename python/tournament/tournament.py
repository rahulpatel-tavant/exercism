from collections import defaultdict

def tally(rows):
    points_table = {}
    for row in rows:
        points_table = write_in_points_table(row, points_table)
    return format_points_table(sort(points_table))

def write_in_points_table(row, points_table):
    result = row.split(';')
    if result[2] in ['win', 'loss']:
        winner_team = result[0] if result[2] == 'win' else result[1]
        losser_team = result[0] if result[2] == 'loss' else result[1]
        points_table = update_point_table_on_win_loos(points_table, winner_team, losser_team)
    else:
        points_table = update_point_table_on_draw(points_table, result[0], result[1])
    return points_table

def update_point_table_on_win_loos(pt, wteam, lteam):
     pt[wteam] = pt[wteam] if wteam in pt else defaultdict(int)
     pt[wteam] = { 'MP' : pt[wteam]['MP'] + 1, 'W' : pt[wteam]['W'] + 1, 'D' : pt[wteam]['D'], 'L' : pt[wteam]['L'], 'P' : pt[wteam]['P'] + 3 }
     pt[lteam] = pt[lteam] if lteam in pt else defaultdict(int)
     pt[lteam] = { 'MP' : pt[lteam]['MP'] + 1, 'W' : pt[lteam]['W'], 'D' : pt[lteam]['D'], 'L' : pt[lteam]['L'] + 1, 'P' : pt[lteam]['P'] } 
     return pt

def update_point_table_on_draw(pt, team1, team2):
   pt[team1] = pt[team1] if team1 in pt else defaultdict(int)
   pt[team1] = { 'MP' : pt[team1]['MP'] + 1, 'W' : pt[team1]['W'], 'D' : pt[team1]['D'] + 1, 'L' : pt[team1]['L'], 'P' : pt[team1]['P'] + 1 }
   pt[team2] = pt[team2] if team2 in pt else defaultdict(int)
   pt[team2] = { 'MP' : pt[team2]['MP'] + 1, 'W' : pt[team2]['W'], 'D' : pt[team2]['D'] + 1, 'L' : pt[team2]['L'], 'P' : pt[team2]['P'] + 1 } 
   return pt

def sort(pt):
    pt = sorted(pt.items(), key = lambda kv : kv[1]['P'], reverse=True)
    for i in range(1, len(pt)):
        if pt[i - 1][1]['P'] == pt[i][1]['P'] and pt[i - 1][0] > pt[i][0]:
            temp = pt[i]
            pt[i] = pt[i - 1]
            pt[i - 1] = temp
    return pt

def format_points_table(pt):
    results = ['Team                           | MP |  W |  D |  L |  P']
    for tp in pt:
        results.append("{:31}|{:3} |{:3} |{:3} |{:3} |{:3}".format(tp[0], tp[1]['MP'], tp[1]['W'], tp[1]['D'], tp[1]['L'], tp[1]['P']))              
    return results    
