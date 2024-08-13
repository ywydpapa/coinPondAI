import jwt
import hashlib
import os
import requests
import uuid
import dotenv
from urllib.parse import urlencode, unquote


dotenv.load_dotenv()
access_key = os.getenv('UPBIT_OPEN_API_ACCESS_KEY')
secret_key = os.getenv('UPBIT_OPEN_API_SECRET_KEY')
server_url = os.getenv('UPBIT_OPEN_API_SERVER_URL')

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

params = {
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', params=params, headers=headers)
res.json()
print(res.json())