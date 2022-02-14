from pwn import *
import sys
import termcolor

if len(sys.argv) !=2:
	print("Invalid Argument!")
	exit()

wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

if wanted_hash == '--help':
	print('If you want to use this tool, You need to specify some arguments on it, Like: \n')
	print(termcolor.colored(f'>> {sys.argv[0]} <sha256sum> \n', 'green'))
else:
	with log.progress("Attempting to back {}!\n".format(wanted_hash)) as p:
		with open(password_file, 'r', encoding="latin-1") as password_list:
			for password in password_list:
				password = password.strip('\n').encode('latin-1')
				password_hash = sha256sum(password)
				p.status("[{}] {}== {}".format(attempts, password.decode('latin-1'),password_hash))
				if password_hash == wanted_hash:
					p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
					exit()
				attempts += 1
			p.failure("Password hash not found!")
