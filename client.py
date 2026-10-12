import requests

USER_SVC = "http://user-svc.internal"
ORDER_SVC = "http://order-svc.internal"


def fetch_user(uid):
    # literal path templated from an f-string base
    return requests.get(f"{USER_SVC}/api/v1/users/{uid}")


def place_order(data):
    return requests.post("http://order-svc.internal/api/v1/orders", json=data)
