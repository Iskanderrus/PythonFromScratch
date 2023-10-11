# function can take several arguments in case you don't know how many of them will be passed:
def build_user(first_name, last_name, **user_info) -> dict:
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user_data = build_user('Alex', 'Chasovskoy', age='43', sex='male', city='Sombor', origin='Russia')
print(user_data)

# if only mandatory data provided:
user_data = build_user('Alex', 'Chasovskoy')
print(user_data)