import requests

creds = ('login', 'password')
num_records = {'per_page': '100'}


def get_pulls(state):
    if state == "open" or state == "closed":
        url = f"https://api.github.com/repos/alenaPy/devops_lab/pulls?state={state}"
        response = requests.get(url, params=num_records, auth=creds)
        pull = response.json()
    elif state == "accepted" or state == "needs work":
        url = 'https://api.github.com/search/issues?q=is:pr%20label:' \
              f'"{state}"%20repo:alenaPy/devops_lab'
        response = requests.get(url, params=num_records, auth=creds)
        pull = response.json()['items']
    else:
        url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all'
        response = requests.get(url, params=num_records, auth=creds)
        pull = response.json()

    output = []
    for item in pull:
        output.append({
            'num': item['number'], 'title': item['title'],
            'link': item['html_url']})
    return output
