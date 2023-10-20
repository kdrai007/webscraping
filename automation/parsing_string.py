from parse import parse

# data = search('Age: {:d}\n', 'Name: Rufus\nAge: 42\nColor: red\n')
# print(data)

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE:$09.99'
FORMAT = '[{date:ti}] - SALE - PRODUCT: {product} - PRICE: ${price}'
result = parse(FORMAT, LOG)
print(result)
