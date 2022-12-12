import re

pattern = r'https://\w+\.\w+\.\w+\/\w+\/\w+'

value = 'https://cloud.mail.ru/stock/ot7HCHvvgMZpAgi2ULUCq2JH'

match = re.fullmatch(pattern, value)

print(True if match else False)
