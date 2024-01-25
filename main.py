from fastapi import FastAPI
import requests
import json

# TEST

url_test = "http://genrestest.nntc.pro/auth/realms/genrestest/protocol/openid-connect/token"
payload_test = 'grant_type=password&client_id=resources&redirect_uri=http%3A%2F%2Fgenrestest.nntc.pro%2Fmodels-catalog%2Fmain&username=dev&password=qwe123R!'
headers_test = {
            'Content-Type': 'application/x-www-form-urlencoded'
}

# DEV

url_dev = "http://generated.dev.nntc.pro/auth/realms/cartography/protocol/openid-connect/token"
payload_dev = 'grant_type=password&client_id=mars&redirect_uri=http%3A%2F%2Fgenerated.dev.nntc.pro%2Fmodels-catalog%2Fmain&username=dev&password=qwe123R!'
headers_dev = {
    'Content-Type': 'application/x-www-form-urlencoded'
}


app = FastAPI(
    title="IIFA_test_server"
)


@app.get("/get_token")
def get_token(stand: str):
    if stand == 'test':
        response = requests.request("POST", url_test, headers=headers_test, data=payload_test)
        data = response.json()
        token = data['access_token']
        access_token = token
        print("token для test стенда получен")
        return token
    if stand == 'dev':
        response = requests.request("POST", url_dev, headers=headers_dev, data=payload_dev)
        data = response.json()
        token = data['access_token']
        print("token для dev стенда получен")
        return token
    else:
        logtext = 'не удалось получить token'
        return logtext