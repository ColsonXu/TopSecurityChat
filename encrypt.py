import random as r

rand_seed = input('Please enter the private key of this message: ')
raw_message = input('Please enter the message: ')


def encrypt(r_str, rand_seed):
	r.seed(rand_seed)
	generated_key = str(r.randint(1000000000000000000000000000000000000000000000,9999999999999999999999999999999999999999999999))
	encrypt_list = [generated_key[i:i+2] for i in range(0, len(generated_key), 2)]
	print(encrypt_list) # Debug line
	encrypted_string = reversed(r_str)
	return encrypted_string


print('Your encrypted message is: ' + encrypt(raw_message, rand_seed))


# Encryption Dictionary, DO NOT TEMPER WITH!!!

##############################################################################

ENCRYPTION_DICTIONARY = {'01':'@', '02':'#', '03':'^', '04':'!',

			'05':'s', '06':'a', '07':'d', '08':'x',
			'09':'r', '10':'h', '11':'b', '12':'v',
			'13':'n', '14':'z', '15':'q', '16':'w',
			'17':'y', '18':'u', '19':'k', '20':'m',
			'21':'e', '22':'p', '23':'l', '24':'i',
			'25':'f', '26':'g', '27':'j', '28':'c',
			'29':'t', '30':'o', '31':'s',

			'32':'2', '33':'3', '34':'5', '35':'1',
			'36':'4', '37':'7', '38':'9', '39':'8',
			'40':'6', '41':'0', '42':'apple', '43':'Sunday',
			'44':'send', '45':'sandbox',
			}

#############################################################################
