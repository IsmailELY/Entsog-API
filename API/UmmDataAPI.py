import BaseAPI
import time

class UrgentMarketMessagesAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="urgentMarketMessages", **kwargs)
