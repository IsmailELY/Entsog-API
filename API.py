import requests
import json
import re

class EntsogAPI:
    def __init__(self, uri:str=None) -> None:
        if uri: self.set_uri(uri)
        self.r = requests.get("https://transparency.entsog.eu/api/v1")

    def set_uri(self, uri:str) -> None:
        """Sets up a correct Entsog API Uri"""
        reg = "^https://transparency\.entsog\.eu/api/v1/(operationaldatas|cmpUnsuccessfulRequests|cmpUnavailables|cmpAuctions|interruptions|AggregatedData|tariffssimulations|tariffsfulls|urgentmarketmessages|connectionpoints|operators|balancingzones|operatorpointdirections|Interconnections|aggregateInterconnections).*limit=[^-].*"
        if re.search(reg, uri):
            self.uri = uri
            self.r = requests.get(self.uri)
        else:
            raise Exception("Entsog API Uri is not valid")

    def __str__(self) -> str:
        """Returns API result"""
        if self.r.status_code < 300:
            return json.dumps(self.r.json(), indent=2)
        else:
            return f"Status Code: {self.r.status_code}"

if __name__=='__main__':
    r = EntsogAPI()
    print(r)