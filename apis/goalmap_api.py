from utils.api_helper import ApiHelper

class GoalMapApi:
    def __init__(self, config):
        self.url = config['url']
        self.endpoint = f'map/{config["candidate_id"]}/goal'

    def get(self) -> []:
        response = ApiHelper.get(self.url + self.endpoint)
        if 'goal' not in response:
            print('Unexpected formatting in goal map response')
            return []

        return response['goal']