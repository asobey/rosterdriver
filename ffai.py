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

print('==============INITIALIZE ROSTER DRIVER=============')
d = RosterDriver(url, cookies)
print('==============PRINT ROSTER=============')
# for ros in d.roster:
#     print(ros)
print('==============TIERED UPDATE=============')
d.tiered_update()
print()
print('==============FETCH WAIVER TARGETS=============')
w = d.fetch_waiver_targets()
print('==============PRINT WAIVER TARGETS=============')
for p in w:
    print(p)
print('==============QUIT=============')
d.quit_driver()