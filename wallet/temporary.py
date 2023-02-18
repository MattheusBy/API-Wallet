from datetime import *

query = str({'id': 63, 'description': 'ЗП', 'category': 'ЗП', 'amount': 1150.0, 'user_id': 27, 'kind': 'Доход'})

x=query.split(",")
print(x[4].split(':')[1])