import falcon
import json

class BaseResource:
    """Abstract class for falcon resources
       Has methods for orm interactions, queries,
       serializing and deserializing data for falcon consumption.
    """


    def create(self, data):
        """Creates a single object in the corresponding table
           Args:
               data: Deserialized input coressponds to model attribute.
           Returns:
               obj: Newly created peewee object.
        """
        obj = self.model.create(**data)
        return obj

    def fetch(self, obj_id):
        """Rerieve a single record given its id
           Args:
               obj_id: object priamary key(id)
           Returns:
               obj: Record if found or 404 if not found
        """
        try:
            obj = self.model.get(self.model.id == obj_id)
        except (self.model.DoesNotExist, ValueError):
            raise falcon.errors.HTTPNotFound
        return obj

    def list(self, query=None):
        """Returns a list of object based on the passed query
           or it will select all the rows in the table.
           Args:
               query(optional): Peewee query Expression.
        """
        result = self.model.select()
        if query:
            result = result.where(query)
        return result

    def update(self, data, obj_id):
        """Updates an object(row) using its primary key(id)
           Args:
               data: dict with changes {'attr': 'change'}
               obj_id: object priamary key(id)
           returns:
               updated: number of rows updated
        """
        try:
            query = self.model.update(**data).where(self.model.id == obj_id)
            updated = query.execute()
        except KeyError:
            raise falcon.errors.HTTPBadRequest
        return updated

    def delete(self, obj_id):
        """Deletes an object(row) using its primary key(id)
           Args:
               obj_id: object priamary key(id)
           returns:
               deleted: number of rows deleted
        """
        try:
            query = self.model.delete().where(self.model.id == obj_id)
            deleted = query.execute()
        except self.model.DoesNotExist:
            raise falcon.errors.HTTPNotFound
        return deleted 

class PeeweeResource(BaseResource):
    model = None

    def on_get(self, request, response, pk=None):

        instance = self.fetch(pk)
