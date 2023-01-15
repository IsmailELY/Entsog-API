import BaseAPI
import time

class AggregatedDataAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="aggregatedData", **kwargs)