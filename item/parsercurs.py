import requests

# Курс пары валют (коды валют в String)
def exchange(api_access_token, currency_to, currency_from):
	s = requests.Session()
	s.headers = {'content-type': 'application/json'}
	s.headers['authorization'] = 'Bearer ' + api_access_token
	s.headers['User-Agent'] = 'Android v3.2.0 MKT'
	s.headers['Accept'] = 'application/json'
	res = s.get('https://edge.qiwi.com/sinap/crossRates')

	# все курсы
	rates = res.json()['result']

	# запрошенный курс
	rate = [x for x in rates if x['from'] == currency_from and x['to'] == currency_to]
	if (len(rate) == 0):
		print('No rate for this currencies!')
		return
	else:
		curs = 1/(float(rate[0]['rate']))
		print(curs)
		return rate[0]['rate']        

exchange("9afbe13e92d995dfc17befa52e6af754", "398", "643")