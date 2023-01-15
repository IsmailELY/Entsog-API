from typing import Iterator
import BaseAPI

class OperationalAPI(BaseAPI):
    def __init__(self, url:str=None, **kwargs) -> None:
        super().__init__(url=url, **kwargs)

    def read_json(self, offset:int=0, destination:int=1000, pace:int=1000) -> Iterator[dict]:
        """Generator of Operational Data API Content"""
        def load_batch(offset):
            self.set_payload(offset=offset, limit=pace)
            return self.__r.json()["operationaldatas"]
        Iter = 0
        while Iter < destination:
            for record in load_batch(offset=Iter):
                yield record
                Iter += 1
                if Iter == destination: break

    def set_payload(self, **kwargs) -> None:
        """Redefine"""
        super().set_payload(self, **kwargs)