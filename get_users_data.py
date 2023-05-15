from get_data import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    users = []
    results = data['results']
    for user in results:
        first_name = user['name']['first']
        last_name = user['name']['last']
        phone_number = user['phone']
        users.append(f'first_name:{first_name}, last_name:{last_name}, phone_number:{phone_number}')
    return users

data = get_data('randomuser_data.json')
print(get_users_data(data))