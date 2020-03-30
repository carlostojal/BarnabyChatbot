
#
# Copyright (c) Carlos Tojal
# BarnabyChatbot
# barnaby_consultant.py
#

import json
import requests

class BarnabyConsultant:

    def get_config(self):
        f = open("config.json", "r")
        config = json.loads(f.read())
        f.close()
        return config
    
    def consult_barnaby(self, q):
        print("Requesting API ({})...".format(q))
        url = "http://{}:{}/assistant".format(self.get_config()['api_url'], self.get_config()['api_port'])
        params = {
            "q": q
        }
        r = requests.get(url = url, params = params)
        response = r.json()
        print("Got response.")
        return response