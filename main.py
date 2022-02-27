import qrcode
url = input('Please input your URL.')
img = qrcode.make(f'{url}')
img.save(f'{url}.png')
img.show()