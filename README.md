Proxy Store Requests
--------------------

A wrapper for the proxy-store interface


Configure Session

```python

from proxy_store_request import ProxyStoreSession

proxy_request = ProxyStoreSession(
    server_url='http:localhost:9999',
    server_token='very secret'
)
```


Use as normal request

```python

response = proxy_request.get(
    'https://backend-service.com',
    headers=dict(Authorization='token'),
    params=dict(fields='params'),
)


```
> Sends the request through the proxy.
> Actual request sent:

`GET http:localhost:9999?url=https%3A%2F%2Fbackend-service.com&headers=%7B%27Authorization%27%3A%20%27token%27%7D&params=%7B%27fields%27%3A%20%27params%27%7D`

