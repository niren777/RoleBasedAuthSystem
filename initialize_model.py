import initial_data as data
import models

users_collection = []
for user in data.users:
    users_collection.append(models.User(user['id'], user['name'], user['email'], user['created_at']))

roles_collection = []
for role in data.roles:
    roles_collection.append(models.Role(role['id'], role['name']))

action_types_collection = []
for action_type in data.action_types:
    action_types_collection.append(models.ActionType(action_type['id'], action_type['name']))

user_role_relation_collection = []
for user_role_relation in data.user_role_relations:
    user_role_relation_collection.append(models.UserRoleRelation(user_role_relation['user_id'], user_role_relation['role_id']))

action_type_role_relation_collection = []
for action_type_role_relation in data.action_type_role_relations:
    action_type_role_relation_collection.append(models.ActionTypeRoleRelation(action_type_role_relation['action_type_id'], action_type_role_relation['role_id']))

resource_collection = []
for resource in data.resources:
    resource_collection.append(models.Resource(resource['id'], resource['title'], resource['description'], resource['created_by']))