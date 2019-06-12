roles = [{
        'id': "1",
        'name': 'AUTHOR'
    },{
        'id': "2",
        'name': 'CONTRIBUTOR'
    },{
        'id': "3",
        'name': 'ADMINISTRATOR'
    },{
        'id': "4",
        'name': 'SUBSCRIBER'
    }
]
users = [{
    'name': 'thiru',
    'id': "1",
    'email': "abc@niren.xyz",
    'created_at':"2019-06-09T10:10:10.000Z"
},{
    'name': 'niren',
    'id': "2",
    'email': "abc@xyz.com",
    'created_at':"2019-06-10T10:10:10.000Z"
}]
action_types = [{
        'id': "1",
        'name': 'WRITE'
    },{
        'id': "2",
        'name': 'READ'
    },{
        'id': "3",
        'name': 'DELETE'
    }
]
# User 1 has role of AUTHOR/CONTRIBUTOR/ADMINISTRATOR
# User 2 has role of SUBSCRIBER
user_role_relations = [{
        'user_id': "1",
        'role_id': "1"
    },{
        'user_id': "1",
        'role_id': '2'
    },{
        'user_id': "1",
        'role_id': "3"
    },{
        'user_id': "2",
        'role_id': '4'
    }
]
resources = [{
    'title': '1st post',
    'id': "1",
    'description': "Here is the first post",
    'created_by':"1"
}]
# Role AUTHOR has Write/Read/Delete permission
# Role CONTRIBUTOR has Write/Read permission 
# Role ADMINISTRATOR has Write/Read/Delete permission 
# Role SUBSCRIBER has Read permission 
action_type_role_relations = [{
    'action_type_id': "1",
    'role_id': "1"
},{
    'action_type_id': "2",
    'role_id': "1"
},{
    'action_type_id': "3",
    'role_id': "1"
},{
    'action_type_id': "1",
    'role_id': "2"
},{
    'action_type_id': "2",
    'role_id': "2"
},{
    'action_type_id': "1",
    'role_id': "3"
},{
    'action_type_id': "2",
    'role_id': "3"
},{
    'action_type_id': "3",
    'role_id': "3"
},{
    'action_type_id': "2",
    'role_id': "4"
}]