
def register_routes(api, root="api/v1"):
    """ Register routes """
    from authentication.controllers import api as authentication_api

    api.add_namespace(authentication_api, path=f"/{root.rstrip('/')}/authentication")