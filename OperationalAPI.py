import EntsogAPI

class OperationalAPI(EntsogAPI):
    def __init__(self, url:str=None, **kwargs) -> None:
        super().__init__(url=url, **kwargs)

    def read_json(self, offset=0, limit=1000) -> dict:
        """Read API Content"""
        self.set_payload(offset=offset, limit=limit)
        content = self.__r.json()
        if content:
            return content["operationaldatas"] | self.read(offset=offset+limit, limit=limit)
        return None

