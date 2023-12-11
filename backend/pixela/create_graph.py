import requests


USER_ENDPOINT = "https://pixe.la/v1/users"


def create_graph(username, token, goal):
    if goal == "Weight Loss":
        graph_id = "weight-loss"
    elif goal == "Weight Gain":
        graph_id = "weight-gain"
    else:
        return False
    color = "shibafu" if goal == "Weight Gain" else "momiji"
    graph_url = f"{USER_ENDPOINT}/{username}/graphs"
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
