import random as r
from main import Main
from keygen import Keygen

main = Main()
key = Keygen(main.rand_seed)

raw_message_list = []
for ch in main.raw_message:
	raw_message_list.append(ch)


def Resersion(r_str, rand_seed):
	encrypt_list = key.resersion_key_gen()
	encrypted_string = r_str[::-1]
	msg_idx = 0
	lst_idx = 0
	for ch in range(len(r_str)):
		encrypted_string.insert(msg_idx, ENCRYPTION_DICTIONARY[ encrypt_list[lst_idx] ])
	return encrypted_string


print('Your encrypted message is: ' + Resersion(raw_message_list, key.RAND_SEED))
