from pycookiecheat import chrome_cookies 
from roster_driver import RosterDriver
import yaml

"""This function opens the espn_creds.yaml file and returns its contents as privateData"""
with open('espn_cookies.yaml', 'r') as _private:
    try:
        private_data = yaml.load(_private)
    except yaml.YAMLError as exc:
        print(exc)

#your URL here
url = private_data['url']

#cookies = chrome_cookies(url)
cookies = {'espn_s2': private_data['espn_s2'],
'SWID': private_data['SWID']}


d = RosterDriver(url, cookies)

for ros in d.roster:
    print(ros)
d.tiered_update()
print()
w = d.fetch_waiver_targets()
for p in w:
    print(p)
d.quit_driver()