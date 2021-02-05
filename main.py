import requests

# https://stackoverflow.com/questions/55262686/multiple-urls-to-save-json-data

from config import j_username, j_password, twofa_code

def main():
    url = 'https://example.com/login.action'

    page_list = [
        'https://example.com/page-1',
        'https://example.com/page-2',
        ]

    with requests.session() as session:

        data = {
            'j_username': j_username,
            'j_password': j_password,
            'twofa_code': ''
        }
        for url in page_list:
            page = session.get(url)
            print(page.text)

        with open('ke_to_suspek.csv', 'a') as f:
            f.write(page.text + '\n')

if __name__ == '__main__':
    main()
