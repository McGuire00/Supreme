
import requests
from datetime import datetime
import json


def clock():
    current = datetime.now()
    print(str(current) + " EST")

keyword = input("Product name you want inventory for? ").title()       # hardwire here by declaring keyword as a string

ID = 0
def main():
    global ID
    global variant
    global cw
    global styles_id
    req = requests.get('http://www.supremenewyork.com/mobile_stock.json')
    data = req.json()
    for prod_cat_list in data["products_and_categories"].values():
        for item in prod_cat_list:
            item = item
            name = str(item['name'].replace('b', ''))
            # SEARCH WORDS HERE
            # if string1 in name:
            if keyword in name:
                # match/(es) detected!
                # can return multiple matches but you're
                # probably buying for resell so it doesn't matter
                myproduct = name
                ID = str(item['id'])
                clock()
                print('::', name, 'found ( MATCHING ITEM DETECTED )')
    if (ID == 0):
        # variant flag unchanged - nothing found - rerun
        clock()
        print(':: Reloading and reparsing page...')
        main()
    else:
        clock()
        print(':: Showing inventory for', str(myproduct))
        jsonurl = 'http://www.supremenewyork.com/shop/' + str(ID) + '.json'
        req = requests.get(jsonurl)
        data = req.json()
        i = json.dumps(data)
        found = 0
        for numCW in data['styles']:
            names = numCW['name']
            print(names)
            for sizes in numCW['sizes']:
                print(sizes)

main()
