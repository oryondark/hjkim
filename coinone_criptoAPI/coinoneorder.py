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
	def transaction_parm(self, coinName):
		t = int(time.time()*1000)
		createParm = {
			'access_token':self.ACCESS_TOKEN,
			'currency': coinName,
			'nonce':t,
		}

	#convert to json that is for read from recieved webserver(bytes)data.
	def read_json(self, res):
		dump = json.dumps(res.decode('utf-8'))
		#print(type(dump))
		info = json.loads(dump)
		if type(info).__name__ != 'dict':
			#if info value isn't dict then onemore time initiation to loads json.
			info = json.loads(info)
		#print(type(info))

		return info


