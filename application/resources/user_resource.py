import falcon
import json
from application.resources import PeeweeResource
from marshmallow_peewee import ModelSchema
from application.models import User


class UserSerializer(ModelSchema):
    
    class Meta:
        model = User

class UserResource(PeeweeResource):
    model = User
    serializer = UserSerializer