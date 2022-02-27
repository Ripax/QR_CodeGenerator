# File name : QR_CodeGenerator
# Author : HTMLDigger
# Date : Fab 27th 2022
# ## ############################################
#    test Script.
# ## ############################################

import qrcode
url = input('Please input your URL.')
img = qrcode.make(f'{url}')
img.save(f'{url}.png')
img.show()
