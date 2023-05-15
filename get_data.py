import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f = open(filename).read()
    data = json.loads(f)
    return data
def main():
    print(get_data('randomuser_data.json'))

if __name__ == '__main__':
    main()