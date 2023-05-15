from get_data import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    results = data['results']
    gender = []
    for user in results:
        gender.append(user['gender'])
    return gender

data = get_data('randomuser_data.json')
print(get_gender_users(data))