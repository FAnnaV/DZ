import json

# data_registr = {"login": "passwd"}
# with open("registr.json", "w") as f:
# 	json.dump(data_registr, f)


def add_registr(login, passwd):
	log = input("Введите логин: ")
	passwd = input("Введите пароль: ")
	with open("registr.json", "r") as f:
		data_registr = json.load(f)
	if login not in data_registr.keys():
		data_registr[login] = passwd
		with open("registr.json", "w") as f:
			json.dump(data_registr, f)
			pass
	