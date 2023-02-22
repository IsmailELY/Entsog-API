import BaseAPI
import time

class OperationalDataAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="operationaldatas", **kwargs)

class CmpUnsuccessfulRequestsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="cmpUnsuccessfulRequests", **kwargs)

class CmpUnavailablesAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="cmpUnavailables", **kwargs)

class CmpAuctionsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="cmpAuctions", **kwargs)

class InterruptionsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="interruptions", **kwargs)
