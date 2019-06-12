from initialize_model import action_types_collection, roles_collection, user_role_relation_collection,\
    resource_collection, action_type_role_relation_collection

def create_permission(function):
    def decorated(self, user_id, *args, **kwargs):
        role = get_role_by_user_id(user_id)
        if has_permission(role, 'WRITE'):
            return function(self, user_id, *args, **kwargs)
        else:
            print('No permission to write')
    return decorated

def delete_permission(function):
    def decorated(self, user_id, *args, **kwargs):
        role = get_role_by_user_id(user_id)
        if has_permission(role, 'DELETE'):
            return function(self, user_id, *args, **kwargs)
        else:
            print('No permission to delete')
    return decorated

def read_permission(function):
    def decorated(self, user_id, *args, **kwargs):
        role = get_role_by_user_id(user_id)
        if has_permission(role, 'READ'):
            return function(self, user_id, *args, **kwargs)
        else:
            print('No permission to read')
    return decorated

def has_permission(role, action_type_name):
    action_type = get_action_type(action_type_name)
    for relation in action_type_role_relation_collection:
        if relation.role_id == role.id and relation.action_type_id == action_type.id:
            return get_role_by_id(relation.role_id)

def get_role_by_user_id(user_id):
    for relation in user_role_relation_collection:
        if relation.user_id == user_id:
            return get_role_by_id(relation.role_id)

def get_role_by_id(role_id):
    for role in roles_collection:
        if role.id == role_id:
            return role

def get_action_type(type_name):
    for action_type in action_types_collection:
        if action_type.name == type_name:
            return action_type
