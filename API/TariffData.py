import BaseAPI
import time

class TariffsSimulationsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="tariffsSimulations", **kwargs)

class TariffsFullsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="tariffsFulls", **kwargs)