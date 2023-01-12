import requests
import json
import re

class EntsogAPI:
    """Entsog API Configuration"""
    def __init__(self, uri:str=None) -> None:
        self.count_req = 0
        if uri: self.set_uri(uri)
        self.payload=dict()

    def Reload(method):
        """Reload data after modification"""
        def inner(self, *args, **kwargs):
            method(self, *args, **kwargs)
            self.r = requests.get(self.uri, params=self.payload)
            self.count_req+=1
            print("data reloaded!")
        return inner

    @Reload
    def set_uri(self, uri:str) -> None:
        """Sets up a correct Entsog API Uri"""
        reg = "^https://transparency\.entsog\.eu/api/v1/(operationaldatas|cmpUnsuccessfulRequests|cmpUnavailables|cmpAuctions|interruptions|AggregatedData|tariffssimulations|tariffsfulls|urgentmarketmessages|connectionpoints|operators|balancingzones|operatorpointdirections|Interconnections|aggregateInterconnections).*limit=[^-].*"
        if re.search(reg, uri):
            self.uri = uri
            self.r = requests.get(self.uri)
        else:
            raise Exception("Entsog API Uri is not valid")

    @Reload
    def set_payload(self, property:str, value) -> None:
        self.payload[property] = str(value)

    def __str__(self) -> str:
        """Returns API result"""
        if not hasattr(self,'r'):
            return ''
        elif self.r.status_code < 300:
            return json.dumps(self.r.json(), indent=2)
        else:
            return f"Status Code: {self.r.status_code}"

if __name__=='__main__':
    d = EntsogAPI()
    print(d)
    d.set_uri("https://transparency.entsog.eu/api/v1/operationaldatas?limit=5")
    d.set_payload(property='indicator',value='Interruptible Available')
    print(d.count_req)