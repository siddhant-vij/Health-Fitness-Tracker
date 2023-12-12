import requests
from backend.constants import USER_END_POINT


def create_graph(username, token, graph_id):
    color = "shibafu" if graph_id == "weight-gain" else "momiji"
    graph_url = f"{USER_END_POINT}/{username}/graphs"
    graph_headers = {
        "X-USER-TOKEN": token
    }
    graph_body = {
        "id": graph_id,
        "name": "Health Fitness Tracker",
        "unit": "KCal",
        "type": "int",
        "color": color
    }
    response = requests.post(graph_url, json=graph_body, headers=graph_headers)
    if response.status_code == 200:
        return True
    else:
        return False
