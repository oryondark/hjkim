# -*- coding : utf-8 -*-
from coinoneorder import CoinOneOrder
from coinoneurl import CoinOneURLapi
import json
#CoinOne create by KIM.H.J


ONE = CoinOneOrder()
API = CoinOneURLapi()

def tokenCheck():
	if ONE.ACCESS_TOKEN == '':
		print("Access Token failed")
		return -1
	if ONE.SECRET_KEY == '':
		print("Secret key failed")
		return -1

	return 0

def userSignIn():

	print("Please input your ACCESSTOKEN and SECRETKEY that The Key-Information received from CoinOne Mail.")
	ONE.ACCESS_TOKEN = input("input Access token (from coinone mail) : ").strip()
	ONE.SECRET_KEY = input("input SECRET KEY (from coinone mail) : ").strip()


def selectAction(num):
	if tokenCheck() == -1:
		print("Please User signment.[Number 5]")
		#userSignIn()
		return main()

	if num == 1 or num == 2:
		buyORsell_Coin(num)
	elif num == 3 or num == 4:
		getInfo(num)
	elif num == 7:
		read_History(num)

	#return switch.get(num, 9)#default '9'

def getInfo(num): #3 is to get user information
	parm = ONE.userinfo_parm()
	req_url = API.get_URL_api(int(num))
	HOST = ONE.API_HOST
	sKey = ONE.SECRET_KEY

	res = API.response(sKey, HOST, req_url, parm)
	print(res.read())

def buyORsell_Coin(num):
	KRW = input('How buy want to amount?(input number) : ');
	QRY = input('Input Balance(input number) : ');
	coinName = input('What buy coin?(input String) :');
	#print(type(float(QRY)))
	print("is it right? " + str(int(KRW)) +"/"+str(float(QRY))+"/"+coinName)

	parm = ONE.order_parm(int(KRW), float(QRY), coinName)
	req_url = API.get_URL_api(int(num))
	HOST = ONE.API_HOST
	sKey = ONE.SECRET_KEY
	
	res = API.response(sKey, HOST, req_url, parm)
	print(res.read())

def read_History(num):
	coinName = input("What kind of Coin showing? : ");
	parm = ONE.transaction_parm(coinName)
	req_url = API.get_URL_api(int(num))
	#print(req_url)
	HOST = ONE.API_HOST
	sKey = ONE.SECRET_KEY

	res = API.response(sKey, HOST, req_url, parm)
	print(res.read())

"""
def getBalance():
	parm = ONE.userinfo_parm()
	req_url = API.get_URL_api(4)
	HOST = ONE.API_HOST
	sKey = ONE.SECRET_KEY

	res = API.response(sKey, HOST, req_url, parm)
	print(res.read())
"""
#### main function #####
def main():


	sel = input('What do you want to action?(input number) : ')
	try:
		if int(sel) == 5:
			userSignIn()
			return main()
		elif int(sel) == 6:
			quit()
	except Exception as e:
		print("input failed")
		main()

	selectAction(int(sel))
	return main()

if __name__ == "__main__":
	#ONE = CoinOneOrder()
	#urlapi = CoinOneURLapi()

	print("CoinOne에 오신 것을 환영합니다.\n"+
			"먼저 유저 등록을 진행해 주세요.(5번)\n"+
		   "여러분은 CoinOne에서 거래하기 앞서, 각자의 거래 가능한 코인 수를 확인하셔야 합니다.\n" +
		   "가장 먼저 물어보는 질의문의 대해 번호 '4'를 통해 각자 구매 가능한 코인의 한도량을\n" +
		   "꼭 확인 부탁드립니다. 감사합니다.\n"
		   )
	
	print("1 - buy \n" +
		  "2 - sell \n" +
		  "3 - my_info \n" +
		  "4 - current_balance\n"+
		  "5 - user_sign\n"+
		  "7 - history\n"+
		  "6 - program exit.")

	main() #start






	
