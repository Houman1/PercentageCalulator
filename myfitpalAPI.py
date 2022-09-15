import requests

base_url = "https://www.myfitnesspal.com"
login_url = base_url + "/account/login"

r = requests.get(login_url, auth= ('email', 'password'))


print(r)