from models import UserRoleRelation, Resource
from initialize_model import roles_collection, user_role_relation_collection, resource_collection
from helper import read_permission, create_permission, delete_permission


class RoleLogic():
    def get_role(self, role_name):
        for role in roles_collection:
            if role.name == role_name:
                return role

    def get_user_role_releation(self, user_id, role_name):
        role = self.get_role(role_name)
        for user_role_relation in user_role_relation_collection:
            if user_role_relation.role_id == role.id and user_role_relation.user_id == user_id:
                return user_role_relation

    def assign_role_to_user(self, user_id, role_name):
        role = self.get_role(role_name)
        user_role_relation_collection.append(UserRoleRelation(user_id, role.id))
        print(user_role_relation_collection)

    def remove_user_from_role(self, user_id, role_name):
        role = self.get_user_role_releation(user_id, role_name)
        user_role_relation_collection.remove(role)
        print(user_role_relation_collection)
        

class ResourceLogic():
    @read_permission
    def get_resource(self, user_id, resource_id=None):
        if resource_id:
            resource = self.get_resource_by_id(resource_id)
        else:
            resource = resource_collection
        print(resource)

    @create_permission
    def create_resource(self, user_id, resource):
        id = str(len(resource_collection) + 1)
        resource_collection.append(Resource(id, resource['title'], resource['description'], user_id))
        print(resource_collection)

    @delete_permission
    def delete_resource(self, user_id, resource_id=None):
        resource = self.get_resource_by_id(resource_id)
        resource_collection.remove(resource)
        print(resource_collection)
    
    def get_resource_by_id(self, id):
        for resource in resource_collection:
            if resource.id == id:
                return resource