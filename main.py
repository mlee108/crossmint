import configparser

from apis.cometh_api import ComethApi
from apis.goalmap_api import GoalMapApi
from apis.polyanets_api import PolyanetsApi
from apis.soloons_api import SoloonsApi

configParser = configparser.ConfigParser()
configParser.read('config.ini')
config = configParser['DEFAULT']

def x_mark(n: int):
    api = PolyanetsApi(config)
    for i in range(2, n-2):
        api.post(i, i)
        if i != n-i-1:
            api.post(i, n-i-1)

def megaverse():
    map_api = GoalMapApi(config)
    polyanets_api = PolyanetsApi(config)
    soloons_api = SoloonsApi(config)
    cometh_api = ComethApi(config)

    goal_map = map_api.get()

    n = len(goal_map)
    for i in range(n):
        for j in range(n):
            curr = goal_map[i][j]
            if curr == 'SPACE':
                continue
            elif curr == 'POLYANET':
                polyanets_api.post(i, j)
            else:
                modifier, type_ = curr.split('_')
                modifier = modifier.lower()
                if type_ == 'SOLOON':
                    soloons_api.post(i, j, modifier)
                else:
                    cometh_api.post(i, j, modifier)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Phase 1
    # x_mark(11)

    # Phase 2
    megaverse()