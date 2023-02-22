from typing import Iterator
import requests
import json
import re

class BaseAPI:
    """Entsog API Configuration"""
    def __init__(self, category:str="operators", **kwargs) -> None:
        self.count_req = 0
        self.category = category
        self.__base_uri = 'https://transparency.entsog.eu/api/v1/'
        self.__categories = ('operationaldatas','cmpUnsuccessfulRequests','cmpUnavailables','cmpAuctions',
        'interruptions','AggregatedData','tariffssimulations','tariffsfulls','urgentmarketmessages',
        'connectionpoints','operators','balancingzones','operatorpointdirections','Interconnections',
        'aggregateInterconnections')
        self.__payload = {'offset':'0', 'limit':'5'}
        self.set_uri(category=category)
        if kwargs: self.set_payload(**kwargs)

    def Reload(method):
        """Reload data after modification"""
        def inner(self, *args, **kwargs):
            method(self, *args, **kwargs)
            if self.get_uri(): 
                self.__r = requests.get(self.get_uri(), params=self.__payload)
                self._fields = self.__r.json()["meta"]["fields"]
                self.count_req+=1
        return inner

    def __check_uri(self, uri:str) -> None:
        """Checks the compliance of the Entsog API Uri"""
        reg = "^https://transparency\.entsog\.eu/api/v1/(operationaldatas|cmpUnsuccessfulRequests|cmpUnavailables|cmpAuctions|interruptions|AggregatedData|tariffssimulations|tariffsfulls|urgentmarketmessages|connectionpoints|operators|balancingzones|operatorpointdirections|Interconnections|aggregateInterconnections)*"
        if re.search(reg, uri):
            self.__uri = uri
            self.__r = requests.get(self.__uri)
        else:
            raise Exception("Entsog API Uri is not valid")

    def __str__(self) -> str:
        """Returns API result"""
        if self.__r.status_code < 300:
            return json.dumps(self.__r.json(), indent=2)
        else:
            return f"Status Code: {self.__r.status_code}"

    def read_json(self, offset:int=0, destination:int=1000, pace:int=1000) -> Iterator[dict]:
        """Generator of Operational Data API Content"""
        def load_batch(offset):
            self.set_payload(offset=offset, limit=pace)
            return self._get_request().json()[self.category]
        Iter = 0
        while Iter < destination:
            for record in load_batch(offset=Iter):
                yield record
                Iter += 1
                if Iter == destination: break

    #Setters
    @Reload
    def set_payload(self, **kwargs) -> None:
        """Apply filters"""
        
        if hasattr(self, '_fields'):
            if kwargs.keys() in self._fields: raise Exception(f"""The following keys: {', '.join([key for key in kwargs.keys() if key not in self._fields])} do not exist.
            Please use the available keys for the current API: {', '.join([iter for iter in self._fields])}""") 

        for property, value in kwargs.items():
            if property=='limit' and value<0:
                continue    
            self.__payload[property] = str(value)

    def set_uri(self, category:str) -> None:
        """Set up URI for the selected category"""
        if category in self.__categories:
            b_uri = self.__base_uri + category
            self.__check_uri(uri=b_uri)
        else:
            raise Exception(f"API category '{category}' does not exist.\nPlease select one of the following:\n{','.join(self.__categories)}")
    
    #Getters
    def get_uri(self) -> str:
        """Get Curent API URI"""
        try:
            return self.__uri
        except AttributeError:
            raise Exception("Url is not configured yet.")

    def _get_request(self) -> object:
        """Get Current request object"""
        try:
            return self.__r
        except AttributeError:
            raise Exception("No request have been issued yet.")
    
    