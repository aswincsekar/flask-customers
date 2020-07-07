
def register_routes(api, root="api/v1"):
    """ Register routes """
    from customers.controllers import api as customers_api

    api.add_namespace(customers_api, path=f"/{root.rstrip('/')}/customers")