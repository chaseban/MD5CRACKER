import hashlib, os

print (os.getcwd())

print('=====================')
print('=====================')
print('=====================')
print('=====================')
print('=====================')
print('=====================')
print('WELCOME TO MD5 CRACKER')
print('=====================')
print('ENTER YOUR HASH BELOW')
print('TO GET STARTED |')
print('===============|=====')
print('===============|=====')
print('===============|=====')
print('===============|=====')
print('===============|=====')
print('===============V=====')

flag = 0

#locate wordlists
pass_hash = input("Enter MD5:")
wordlist = ('/home/fedora/alert/pwfile4.txt') #<----- Enter password file location here.
#open wordlist file
try:
	pass_file = open (wordlist, "r")
	quit()
except:
	print('===============')
  
#digest information & compare
for word in pass_file:
	
	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	
	if digest == pass_hash:
		print('PASSWORD FOUND!')
		print('===============')
		print('|||||||||||||||')
		print('vvvvvvvvvvvvvvv')
		print('---------------')
		print("password is: " + word)
		print('---------------')
		flag = 1
		break

if flag == 0:
	print("password/passphrase is not in the list")
	
