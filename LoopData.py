from intoObject import passData


def loopData(cricket_data):
    print(f"Total Matches: {len(cricket_data['data'])}")
    for x in cricket_data["data"]:
        passData(x)


def quick_search(cricket_data):
    search = input("Search for a match : ")
    for x in cricket_data["data"]:
        if search.lower() in x['name'].lower():
            passData(x)
