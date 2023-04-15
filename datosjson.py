import json
from datetime import datetime, timedelta

with open('myfile.json') as f:
    ourjson = json.load(f)

print(f"Valor del token: {ourjson['access_token']}")

expires_in = ourjson['expires_in']
expiration_time = datetime.now() + timedelta(seconds=expires_in)
remaining_time = expiration_time - datetime.now()

print(f"Tiempo restante del token: {remaining_time}")
