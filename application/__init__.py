from falcon import API

application = API(media_type="application/json")


def route(url, resource, *args, **kwargs):
    application.add_route(url, resource, *args, **kwargs)
