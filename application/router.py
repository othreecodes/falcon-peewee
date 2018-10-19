from application import route
from application.resources.user_resource import UserResource

routes = [route("/", UserResource())]
