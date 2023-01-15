import BaseAPI
from typing import Iterator
import time

class OperationalAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="operationaldatas", **kwargs)

    def read_json(self, offset:int=0, destination:int=1000, pace:int=1000) -> Iterator[dict]:
        """Generator of Operational Data API Content"""
        def load_batch(offset):
            self.set_payload(offset=offset, limit=pace)
            return self._get_request().json()["operationaldatas"]
        Iter = 0
        while Iter < destination:
            for record in load_batch(offset=Iter):
                yield record
                Iter += 1
                if Iter == destination: break

    def set_payload(self, **kwargs) -> None:
        if hasattr(self, '_fields'):
            if kwargs.keys() in self._fields: raise Exception(f"""The following keys: {', '.join([key for key in kwargs.keys() if key not in self._fields])} do not exist.
            Please use the available keys for the current API: {', '.join([iter for iter in self._fields])}""") 
        super().set_payload(**kwargs)



if __name__=='__main__':
    a = OperationalAPI()
    for row in a.read_json(0,50):
        print("row: ",row)
        time.sleep(0.3)
