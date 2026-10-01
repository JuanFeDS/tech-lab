import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

user = 'jsmith'
password = config['credentials']['usernames'][user]['password']
print(password)

hashed_passwords = stauth.Hasher([password]).generate()
print(hashed_passwords)