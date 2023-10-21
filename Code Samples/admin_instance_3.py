from admin_3 import Admin

ndsn_admin = Admin(first_name='Anton',
                   last_name='Ruvel',
                   email='a.ruvel@ndsn.com',
                   phone_number='+74951112233',
                   city='Moscow')

ndsn_admin.greet_user()
ndsn_admin.privileges.show_privileges()