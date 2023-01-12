import requests
import json
import re

class EntsogAPI:
    """Entsog API Configuration"""
    def __init__(self, category:str="operators", **kwargs) -> None:
        self.count_req = 0
        self.__base_uri = 'https://transparency.entsog.eu/api/v1/'
        self.__categories = ('operationaldatas','cmpUnsuccessfulRequests','cmpUnavailables','cmpAuctions',
        'interruptions','AggregatedData','tariffssimulations','tariffsfulls','urgentmarketmessages',
        'connectionpoints','operators','balancingzones','operatorpointdirections','Interconnections',
        'aggregateInterconnections')
        self.__payload = {'limit':'5'}
        self.build_uri(category=category)
        self.set_payload(**kwargs)

    def Reload(method):
        """Reload data after modification"""
        def inner(self, *args, **kwargs):
            method(self, *args, **kwargs)
            if self.count_req!=0: self.__r = requests.get(self.get_uri(), params=self.__payload)
            self.count_req+=1
        return inner

    @Reload
    def __set_uri(self, uri:str) -> None:
        """Checks the compliance of the Entsog API Uri"""
        reg = "^https://transparency\.entsog\.eu/api/v1/(operationaldatas|cmpUnsuccessfulRequests|cmpUnavailables|cmpAuctions|interruptions|AggregatedData|tariffssimulations|tariffsfulls|urgentmarketmessages|connectionpoints|operators|balancingzones|operatorpointdirections|Interconnections|aggregateInterconnections)*"
        if re.search(reg, uri):
            self.__uri = uri
            self.__r = requests.get(self.__uri)
        else:
            raise Exception("Entsog API Uri is not valid")

    @Reload
    def set_payload(self, **kwargs) -> None:
        for property, value in kwargs.items():
            if property=='limit' and value<0:
                continue    
            self.__payload[property] = str(value)

    def build_uri(self, category:str) -> None:
        """Set up the """
        if category in self.__categories:
            b_uri = self.__base_uri + category
            self.__set_uri(uri=b_uri)
        else:
            raise Exception(f"API category '{category}' does not exist.\nPlease select one of the following:\n{','.join(self.__categories)}")
        pass
    
    def get_uri(self) -> str:
        """Get Curent API URI"""
        return self.__uri

    def __str__(self) -> str:
        """Returns API result"""
        if self.__r.status_code < 300:
            return json.dumps(self.__r.json(), indent=2)
        else:
            return f"Status Code: {self.__r.status_code}"


if __name__=='__main__':
    #d = EntsogAPI('operationaldatas', indicator='Interruptible Available', directionKey='exit', tsoItemIdentifier='21Z000000OGE0154', limit=-1)
    d = EntsogAPI()
    d.set_payload(indicator='Interruptible Available', directionKey='exit')
    print(d)