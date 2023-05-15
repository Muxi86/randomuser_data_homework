from get_data import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    results = data['results']
    count = 0
    for user in results:
        count += 1
    return count

data = get_data('randomuser_data.json')
print(get_count_users(data)) 

