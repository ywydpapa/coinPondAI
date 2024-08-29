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

params = {
	'market': 'KRW-ETH',
  'states[]': ['done', 'cancel'],
  'start_time': '2024-01-01T00:00:00+09:00',
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/orders', params=params, headers=headers)

for rr in res.json():
    print(rr)