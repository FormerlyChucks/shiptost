import os, time, requests, traceback, json, pathlib

token_path = '/tmp/shiptost_token'

class Shiptost:
    def __init__(self, client_id, client_secret, user_agent, access_token, refresh_token,x_user_type='Bot'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.x_user_type = x_user_type
        if pathlib.Path("/tmp/shiptost_token").exists() == True:
            self.token_file=token_path
        else:
            with open(token_path,'w') as f:
                self.token_file=token_path

    def request(self, method, endpoint, data):
        auth_header = "Bearer {}".format(open(self.token_file,'r+').read().replace("\n",""))
        endpoint = endpoint.
        headers = {"Authorization": auth_header, "User-Agent": self.user_agent,"X-User-Type": str(self.x_user_type)}
        url = f'https://shiptost.com/{endpoint.split('/',1)[1]}'
        response = requests.request(method,url,headers=headers,data=data)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 204:
            return response.status_code
        elif response.status_code == 401:
            self.refresh()
            response = self.request(method,endpoint,data=data)
            return response
        else:
            raise Exception('{}/{}'.format(response.status_code,response.reason))

    def get(self, endpoint, data=None):
        return self.request('GET', endpoint, data=data)
    
    def post(self, endpoint, data=None):
        return self.request('POST', endpoint, data=data)

    def refresh(self):
        r = requests.post('https://shiptost.com/oauth/grant',
                          headers = {"User-Agent": self.user_agent},
                          data = {"client_id": self.client_id,
                                  "client_secret": self.client_secret,
                                  "grant_type": "refresh",
                                  "refresh_token": self.refresh_token})
        new_token = r.json()["access_token"]
        with open(self.token_file, 'w') as tf:
            tf.write(new_token)
        return self
