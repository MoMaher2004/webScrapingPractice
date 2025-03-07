'''
in this file i will login to stdch.menofia.education and get my data from it
this website is my faculty's website to manage students, courses, etc
as an example i will just get my name that is in arabic
please note that i have replaced my username and my password because i dont trust you 😊
'''

import requests
import json

session = requests.Session()

loginUrl = 'https://stdch.menofia.education/studentLogin'
myInfoPage = 'https://stdch.menofia.education/static/PortalStudent.html'

payload = {
    'UserName': USER_NAME,
    'Password': PASSWORD,
    'sysID': '313.',
    'UserLang': 'E',
    'userType': 2
}

login = session.post(loginUrl, data=payload, verify=False)

info = session.post(
    'https://stdch.menofia.education/getJCI',
    data = {
        'param0': 'stuAdmission.stuAdmission',
        'param1': 'GetStudentPersonalData'
    }, verify=False)

i = json.loads(info.text.encode('utf-8').decode('unicode_escape'))['personal'][0]['Name']

print('---------------------\n', i)
