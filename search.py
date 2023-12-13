from LoopData import quick_search
import threading


def fav_match_search(cri):
    fav_match = True
    while fav_match:
        match_search = input("Do you want search for match, enter yes/no :")
        if match_search.lower() != "yes" and match_search.lower() != "no":
            print("Please enter a valid input")
        elif match_search.lower() == "yes":
            quick_search(cri)
        elif match_search.lower() == "no":
            break
