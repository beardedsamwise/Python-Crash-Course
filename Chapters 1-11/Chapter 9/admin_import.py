from admin import Admin

Admin_User = Admin('Peter','Griffin','IT Dept',33)
Admin_User.privileges.privileges = [
'ban hammer',
'nuke user',
'be awesome'
]

Admin_User.describe_user()
Admin_User.privileges.show_privileges()