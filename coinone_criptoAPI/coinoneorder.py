import hashlib, hmac, time, json

class CoinOneOrder():
	ACCESS_TOKEN = ''
	SECRET_KEY = ''
	API_HOST = 'https://api.coinone.co.kr/'

	#Ordering for read UserInfomation of Coin_One Account
	def userinfo_parm(self):
		t = int(time.time()*1000) 
		createParm = { 'access_token':self.ACCESS_TOKEN,
					   'nonce': t,
					   }
		return createParm


	#Ordering for create_parameter to below.
	def order_parm(self, krwPrice, qty, coinName):
		t = int(time.time()*1000)
		createParm = { 'access_token':self.ACCESS_TOKEN, 
					   'price':krwPrice,
					   'qty':qty,
					   'currency':coinName,
					   'nonce':t,
					   }

		return createParm





