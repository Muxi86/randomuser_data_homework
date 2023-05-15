from webbrowser import get
import get_data
import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    results = data['results']
    for user in results:
        street = user['location']['street']
        print(street['number'])
    
f = open('randomuser_data.json').read()
data = json.loads(f)
print(get_count_users(data))   