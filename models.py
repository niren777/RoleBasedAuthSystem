
class User():
    id = ""
    title = ""
    description = ""
    created_at = ""
    def __init__(self, id, name, email, created_at):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at

    def __repr__(self):
       return '{id: ' + self.id + ', name: ' + self.name + ', email: ' + self.email + ', created_at: ' + self.created_at + '}'

class Role():
    id = ""
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
       return '{id: ' + self.id + ', name: ' + self.name + '}'

class ActionType():
    id = ""
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
       return '{id: ' + self.id + ', name: ' + self.name + '}'

class UserRoleRelation():
    user_id = "" #user_id
    role_id = "" #role_id
    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
       return '{user_id: ' + self.user_id + ', role_id: ' + self.role_id + '}'

class ActionTypeRoleRelation():
    action_type_id = "" #user_id
    role_id = "" #role_id
    def __init__(self, action_type_id, role_id):
        self.action_type_id = action_type_id
        self.role_id = role_id

    def __repr__(self):
       return '{action_type_id: ' +self.action_type_id + ', role_id: ' + self.role_id + '}'

# assumed Post as resource
class Resource():
    id = ""
    title = ""
    description = ""
    created_by = ""
    def __init__(self, id, title, description, created_by):
        self.id = id
        self.title = title
        self.description = description
        self.created_by = created_by

    def __repr__(self):
       return '{id: ' + self.id + ', tittle: ' + self.title + ', description: ' + self.description + ', created_by: ' + self.created_by + '}'