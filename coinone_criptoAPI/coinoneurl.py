import json, hashlib, hmac, base64
from urllib.request import urlopen, Request

class CoinOneURLapi():

	#####P R I V A T E F U N C T I O N S#######################
	#copy to CoinOne Api page, for encoding payload.
	
	def __req_header(self, encoded_payload, signature):
		headers = {
			'Content-Type' : 'application/json',
			'X-COINONE-PAYLOAD' : encoded_payload,
			'X-COINONE-SIGNATURE' : signature
		}
		return headers

	def __get_payload(self, payload):
		#payload['nonce'] = int(time.time()*1000);
		dumped_json = json.dumps(payload);
		#json_dump = base64.b64encode(str(dumped_json))
		encode_json = base64.b64encode(bytes(dumped_json, 'utf-8')); #simple encrypt data
		return encode_json;

	def __get_signature(self, secretkey, payload):
		signature = hmac.new(bytes(secretkey.upper(),'utf-8'), payload, hashlib.sha512); #simple encrypt data
		return signature.hexdigest();

    ###########################################################

	def get_URL_api(self, action):
		# URL API
		switch = { 1 : 'v2/order/limit_buy/',
				   2 : 'v2/order/limit_sell/',
				   3 : 'v2/account/user_info/',
				   4 : 'v2/account/balance/',
				   7 : 'v2/transaction/history/',
				 }

		return switch.get(action, 9)#default '9'



	#get data from coinOne server.
	#you should must be make 'state block'.
	def response(self, secretkey,HOST,endpointPath, parmameter):

		json_payload = self.__get_payload(parmameter)
		signature = self.__get_signature(secretkey,json_payload)
		headers = self.__req_header(json_payload, signature)
		URL = HOST + endpointPath
		req = Request(URL, data=json_payload, headers=headers, method='POST')
		#print(str(URL))
		#print(str(json_payload))
		#print(str(headers))
		res = urlopen(req)

		return res

