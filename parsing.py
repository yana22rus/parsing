import requests
import re
from time import sleep


token = "token"
version = 5.103

with open("ID_GIRLS.txt", "w") as f:

    pass

def get_offset(group_id):

    r = requests.get(f"https://m.vk.com/club{group_id}").text

    found = re.findall('<em class="pm_counter">(\d+)<span class="num_delim"> </span>(\d+)</em>', r)

    all = int("".join(found[0]))

    offest = 0

    lst = []

    while all > offest:
        try:
            count = requests.get('https://api.vk.com/method/groups.getMembers', params={
                    'access_token':token,
                    'v':version,
                    'group_id': group_id,
                    'offset':offest,
                }).json()['response']['items']
            sleep(1)
            print(offest)
            offest += 1000
            lst.append("\n".join(list(map(str,count))))
        except Exception:
            sleep(5)

    return lst

d = {"https://m.vk.com/public192797754":192797754,
     "https://m.vk.com/scared_of_girlss":176898719,
     "https://m.vk.com/public190339907":190339907,
     "https://m.vk.com/beautynaxod":187289777,
     "https://m.vk.com/public196731013":196731013,
     "https://m.vk.com/biutimeik":184536564,
     "https://m.vk.com/public202680812":202680812,
     "https://m.vk.com/chepomanicu":160050094,
     }

for x in d.values():

    data = list(set(map(str,get_offset(x))))

    with open("ID_GIRLS.txt", "a") as outfile:
        outfile.write("\n".join(data))


