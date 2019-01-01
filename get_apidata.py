import requests

try:
    #resp = requests.get('http://127.0.0.1:8000/scrumboard/lists/')
    resp = requests.get('http://127.0.0.1:8000/scrumboard/lists/',
                            auth=('suresh', 'pali@123'))
    code = resp.status_code
    if resp.status_code == 200:
        for i in resp.json():
            print(i)
    else:
        print("Bad url or request or wrong password", code)

except:
    print("API not rechable")