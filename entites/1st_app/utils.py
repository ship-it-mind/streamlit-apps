import validators

def is_url(text):
    if validators.url(text.strip()):
        return True
    else:
        return False