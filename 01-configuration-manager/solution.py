def add_setting(user_config, new_config):
    new_key, new_value = (new_config[0].lower(), new_config[1].lower())

    if new_key in user_config:
        return f'Setting \'{new_key}\' already exists! Cannot add a new setting with this name.'
    else:
        user_config[new_key] = new_value
        return f'Setting \'{new_key}\' added with value \'{new_value}\' successfully!'


def update_setting(user_config, new_config):
    key, new_value = (new_config[0].lower(), new_config[1].lower())

    if key in user_config:
        user_config[key] = new_value
        return f'Setting \'{key}\' updated to \'{new_value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'


def delete_setting(user_config, key):
    if not isinstance(key, str):
        print(f'{key} must be a string.')
        return None

    deleted_key = key.lower()

    if deleted_key in user_config:
        user_config.pop(deleted_key)
        return f'Setting \'{deleted_key}\' deleted successfully!'
    else:
        return('Setting not found!')
    

def view_settings(user_config):
    if len(user_config) == 0:
        return f'No settings available.'

    keys_values_lines ='\n'.join(f'{key.capitalize()}: {value}' for key, value in user_config.items())

    return f"""Current User Settings:
{keys_values_lines}
"""
    

test_settings = {'theme': 'light', 'language': 'English'}