import requests

# https://stackoverflow.com/questions/55262686/multiple-urls-to-save-json-data

from config import j_username, j_password, twofa_code

def main():
    url = 'https://silacak.kemkes.go.id/dhis-web-commons-security/login.action'

    page_list = [
        'https://site.com/page-1',
        'https://site.com/page-2'
    ]

    with requests.session() as session:

        data = {
            'j_username': j_username,
            'j_password': j_password,
            'twofa_code': ''
        }
        response = session.post(url, data=data)
        for url in page_list:
            page = session.get(url)
            print(page.text)

        with open('namafile.csv', 'a') as f:
            f.write(page.text + '\n')

if __name__ == '__main__':
    main()
