from utils.api_helper import ApiHelper

class ComethApi:
    def __init__(self, config):
        self.url = config['url']
        self.endpoint = config['cometh_endpoint']
        self.candidate_id = config['candidate_id']

    def post(self, row: int, col: int, direction: str):
        payload = {
            'candidateId': self.candidate_id,
            'row': row,
            'column': col,
            'direction': direction
        }

        ApiHelper.post(self.url + self.endpoint, payload)

    def delete(self, row: int, col: int):
        payload = {
            'candidateId': self.candidate_id,
            'row': row,
            'column': col
        }

        ApiHelper.delete(self.url + self.endpoint, payload)