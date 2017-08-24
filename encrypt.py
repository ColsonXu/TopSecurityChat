import random as r

rand_seed = input('Please enter the private key of this message: ')
raw_message = input('Please enter the message: ')

raw_message_list = []
for ch in raw_message:
	raw_message_list.append(ch)

r.seed(rand_seed)
generated_key = str(r.randint(10 ** 45, 10 ** 46 - 1))

def dict_key_generator(key):
	encrypt_list = [key[i:i+2] for i in range(0, len(key), 2)]
	return encrypt_list

def Resersion(r_str, rand_seed):
	dict_key_generator(generated_key)
	encrypted_string = r_str[::-1]
	msg_idx = 0
	lst_idx = 0
	for ch in range(len(r_str)):
		encrypted_string.insert(msg_idx, ENCRYPTION_DICTIONARY[ encrypt_list[lst_idx] ])
	return encrypted_string


print('Your encrypted message is: ' + Resersion(raw_message_list, rand_seed))

