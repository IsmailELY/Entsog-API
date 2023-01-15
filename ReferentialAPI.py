import BaseAPI
import time

class OperatorsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="operators", **kwargs)

class BalancingZonesAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="balancingZones", **kwargs)

class OperatorPointDirectionsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="operatorPointDirections", **kwargs)

class InterconnectionsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="interconnections", **kwargs)

class AggregateInterconnectionsAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="aggregateInterconnections", **kwargs)