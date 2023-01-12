import requests
import json
import re

class EntsogAPI:
    def __init__(self, uri:str=None) -> None:
        self.set_uri(uri)

    def set_uri(self, uri:str) -> None:
        """Set up a correct Entsog API Uri"""
        reg = "^https://transparency\.entsog\.eu/api/v1/(operationaldatas|cmpUnsuccessfulRequests|cmpUnavailables|cmpAuctions|interruptions|AggregatedData|tariffssimulations|tariffsfulls|urgentmarketmessages|connectionpoints|operators|balancingzones|operatorpointdirections|Interconnections|aggregateInterconnections).*limit=[^-].*"
        if re.search(reg, uri):
            self.uri = uri
        else:
            raise Exception("Entsog API Uri is not valid")

    def display_data(self) -> str:
        r = requests.get(self.uri)
        return json.dumps(r.json(), indent=2)

if __name__=='__main__':
    r = EntsogAPI(uri="https://transparency.entsog.eu/api/v1/operationaldatas?indicator=Interruptible%20Available&limit=5")
    print(r.display_data())