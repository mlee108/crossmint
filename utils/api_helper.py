import requests
import time

class ApiHelper:
    @staticmethod
    def get(url: str) -> dict:
        try:
            r = requests.get(url)
            r.raise_for_status()
            print('Get request succeeded')
            return r.json()
        except requests.exceptions.HTTPError as e:
            print(f'Get request failed w/ status code {e.response.status_code} and message {e.response.text}')
        except requests.exceptions.RequestException as e:
            print('Get request encountered an exception')
            raise

    @staticmethod
    def post(url: str, payload: dict):
        try:
            r = requests.post(url, json=payload)
            match r.status_code:
                case requests.codes.ok:
                    print(f'Post request succeeded w/ payload {payload}')
                case requests.codes.too_many_requests:
                    # no retry-after in the response header, so choose a constant time to wait
                    print(f'Too many requests, retrying in 4 seconds')
                    time.sleep(4)
                    return ApiHelper.post(url, payload)
                case _:
                    print(f'Post request failed w/ status code {r.status_code} and message {r.text}')
        except requests.exceptions.RequestException as e:
            print('Post request encountered an exception')
            raise

    @staticmethod
    def delete(url: str, payload: dict):
        try:
            r = requests.delete(url, json=payload)
            r.raise_for_status()
            print(f'Delete request succeeded w/ payload {payload}')
        except requests.exceptions.HTTPError as e:
            print(f'Delete request failed w/ status code {e.response.status_code} and message {e.response.text}')
        except requests.exceptions.RequestException as e:
            print('Delete request encountered an exception')
            raise