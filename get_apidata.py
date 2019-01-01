import requests

try:
    resp = requests.get('http://127.0.0.1:8000/scrumboard/lists/')

    if resp.status_code == 200:
        for i in resp.json():
            print('{} {}'.format(i['id'], i['name']))
    else:
        print("Bad url or request")

except:
    print("API not rechable")