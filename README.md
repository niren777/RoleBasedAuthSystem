## Assumption made

### Roles 
- AUTHOR
- CONTRIBUTOR
- ADMINISTRATOR
- SUBSCRIBER

### Actions
- Write
- Read
- Delete

### User, Role, Action relationship
- User and Role are many-to-many relationship
- Role and Actions are many-to-many relationship

### Roles and Action Type relation
- Role AUTHOR has Write/Read/Delete permission
- Role CONTRIBUTOR has Write/Read permission 
- Role ADMINISTRATOR has Write/Read/Delete permission 
- Role SUBSCRIBER has Read permission 

## Pre-Created users with roles
- User 1 has role of AUTHOR/CONTRIBUTOR/ADMINISTRATOR
- User 2 has role of SUBSCRIBER

## Command to the run thr project
cd to the directory 
python -i roll_based_auth_system.py

## Role

### Initiate Role
role=RoleLogic()

### Remove a role for the user using user id and role name
role.remove_user_from_role('1', 'ADMINISTRATOR')

//Removed ADMINISTRATOR role for user 1

### Add a role for the user using user id and role name
role.assign_role_to_user('1', 'ADMINISTRATOR')

//Added ADMINISTRATOR role for user 1


role.assign_role_to_user('1', 'SUBSCRIBER')

//Added SUBSCRIBER role for user 1



## Resource(Post)

### Initiate Resource
resource=ResourceLogic()

### Get the post by user id and post id 
resource.get_resource('1','1')

// print specified post

### Get the posts by user id
resource.get_resource('1')

// print all the posts

### Create Second post using user id who as permission to write and resource data
post_resource={
    'title': '2nd post',
    'description': "Here is the 2nd post",
}
resource.create_resource('1', post_resource)

// Successfully created post


### Create post using user id who doesn't have permission and resource data
post_resource={
    'title': '3nd post',
    'description': "Here is the 3nd post"
}
resource.create_resource('2', post_resource)

// No permision to write 

### Delete post using user id who doesn't have permission to delete 
resource.delete_resource('2', '2')

// No permision to delete 

### Delete post using user id who has permission to delete 
resource.delete_resource('1', '2')

// Able to delete
