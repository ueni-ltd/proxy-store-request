from urllib.parse import urlencode

from requests import Session


class ProxyStoreClientException(Exception):
    pass


class ProxyStoreSession(Session):

    def __init__(self, server_url, server_token, user='Proxy-Client'):
        super().__init__()

        self.server_url = server_url
        self.server_headers = {
            'Authorization': f'Token {server_token}',
            'User-Agent': user
        }

    def request(self, method, url,
                params=None, data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, json=None):

        if '?' in url:
            raise ProxyStoreClientException('Pass all url parameters using the "params" kwarg')

        proxy_params = self.clean_dict(params)
        proxy_headers = self.clean_dict(headers)
        proxy_data = self.clean_dict(data)
        proxy_data.update(self.clean_dict(json))

        server_payload = dict(
            url=url,
            params=proxy_params,
            headers=proxy_headers,
            data=proxy_data,
        )

        if method == 'GET':
            params = urlencode(server_payload)
            return super().request(method, self.server_url, params=params)

        return super().request(method, self.server_url, json=server_payload)

    def clean_dict(self, v):
        return v or {}

