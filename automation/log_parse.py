import delorean
from decimal import Decimal

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE:$09.99'
divide_it = log.split(' - ')
timestamp_string, _, product_string, price_string = divide_it
timestamp = delorean.parse(timestamp_string.strip('[]'))
product_id = int(product_string.split(':')[-1])
price = Decimal(price_string.split('$')[-1])
print(price)
