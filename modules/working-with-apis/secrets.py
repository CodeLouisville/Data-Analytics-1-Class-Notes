def get_secret_key(file_name="api-key.secret"):
    """Create your own file with a single line of just the key"""
    with open(file_name) as secret:
        key = secret.readline()

    return key