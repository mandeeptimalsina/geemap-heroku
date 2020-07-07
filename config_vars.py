import os

def set_heroku_vars(token_name='EARTHENGINE_TOKEN'):
    """Extracts Earth Engine token from the local computer and sets it as an environment variable on heroku.

    Args:
        token_name (str, optional): Name of the Earth Engine token. Defaults to 'EARTHENGINE_TOKEN'.
    """
    try:

        ee_token_dir = os.path.expanduser("~/.config/earthengine/")
        ee_token_file = os.path.join(ee_token_dir, 'credentials')

        if not os.path.exists(ee_token_file):
            print('The credentials file does not exist.')
        else:
            with open(ee_token_file) as f:
                content = f.read()
                token = content.split(':')[1][1:-3]
                command = 'heroku config:set {}={}'.format(token_name, token)
                os.system(command)

    except Exception as e:
        print(e)
        return

if __name__ == '__main__':

    set_heroku_vars()