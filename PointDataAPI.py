import BaseAPI
import time

class OperationalAPI(BaseAPI.BaseAPI):
    def __init__(self, **kwargs) -> None:
        super().__init__(category="operationaldatas", **kwargs)

class cmpRequests
"cmpUnsuccessfulRequests"

if __name__=='__main__':
    # Test API section
    a = OperationalAPI()
    for row in a.read_json(0,50):
        print("row: ",row)
        time.sleep(0.3)
