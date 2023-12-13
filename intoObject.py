from CurrMatch import Cricket


def passData(x):
    if len(x['score']) == 2:
        if x["teamInfo"][0]['name'] in x['score'][0]['inning']:
            today_matches = Cricket(x['name'], x['status'], x['matchType'], x["teamInfo"][0]['name'],
                                    x['teamInfo'][1]['name'], x['score'][0]['r'], x['score'][0]['w'],
                                    x['score'][0]['o'],x['score'][1]['r'], x['score'][1]['w'],
                                    x['score'][1]['o'])
        else:
            today_matches = Cricket(x['name'], x['status'], x['matchType'], x["teamInfo"][1]['name'],
                                    x['teamInfo'][0]['name'], x['score'][0]['r'], x['score'][0]['w'],
                                    x['score'][0]['o'],x['score'][1]['r'], x['score'][1]['w'],
                                    x['score'][1]['o'])
    elif len(x['score']) == 1:
        if x["teamInfo"][0]['name'] in x['score'][0]['inning']:
            today_matches = Cricket(x['name'],x['status'],x['matchType'],x["teamInfo"][0]['name'],x['teamInfo'][1]['name'],x['score'][0]['r'],x['score'][0]['w'],x['score'][0]['o'])
        else:
            today_matches = Cricket(x['name'], x['status'], x['matchType'], x["teamInfo"][1]['name'],x["teamInfo"][0]['name'], x['score'][0]['r'],
                                    x['score'][0]['w'], x['score'][0]['o'])
    else:
        today_matches = Cricket(x['name'],x['status'],x['matchType'],x["teamInfo"][0]['name'],x['teamInfo'][1]['name'])

    today_matches.structuring()
    today_matches.Current_Matches()
