import EntsogAPI

class OperationalAPI(EntsogAPI):
    def __init__(self, url:str=None, **kwargs) -> None:
        super().__init__(url=url, **kwargs)

