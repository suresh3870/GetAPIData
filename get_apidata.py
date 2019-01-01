import requests

try:
    resp = requests.get('http://127.0.0.1:8000/scrumboard/lists/')

    if resp.status_code == 200:
        for todo_item in resp.json():
            print('{} {}'.format(todo_item['id'], todo_item['name']))
    else:
        print("Bad url or request")

except:
    print("API not rechable")