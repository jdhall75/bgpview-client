import requests
from requests.status_codes import codes as STATUS
from bgpview.util import VERSION

API_URL = "https://api.bgpview.io"
DEFAULT_UA = f"Python-BGPView/{VERSION}"
API_STATUS_OK = "ok"


class APIError(Exception):
    def __init__(self, message: str = "An API error occurred."):
        super(APIError, self).__init__(message)


class InvalidResponseError(APIError):
    def __init__(self, response: requests.Response, message: str = "Invalid response received from API."):
        super(InvalidResponseError, self).__init__(f"{message} Code: {response.status_code}, Body: {response.content}")


class QueryError(InvalidResponseError):
    def __init__(self, response: requests.Response, message: str = "Query error received from API."):
        super(QueryError, self).__init__(response, message)


class APIClient:
    def __init__(self, user_agent: str = None):
        if user_agent is None:
            user_agent = DEFAULT_UA
        self.s = requests.Session()
        self.s.headers["user-agent"] = user_agent

    def get(self, endpoint: str) -> dict:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        r = self.s.get(f"{API_URL}{endpoint}")
        if r.status_code == STATUS["ok"]:
            try:
                j = r.json()
                if j["status"] != API_STATUS_OK:
                    raise QueryError(r)
                return j
            except ValueError:
                pass  # handled below
        raise InvalidResponseError(r)

    def __del__(self):
        del self.s
