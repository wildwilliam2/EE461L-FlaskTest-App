'''
	File: Encryptor_Tester.py
	Purpose: Test the functionality of teh methods in Encryptor.py
	Author(s):  William
	Last Edit: 2/26/2022 
'''
import Encryptor as e

# Input: None
# Output: None
# Purpose: Test the functionality of Encryptor.py
def test_encryptor():
	test_num = 3
	try:
		test_num = int(input("Enter the number of tests to run: "))
	except ValueError:
		print("Invalid Input Will use 3 test")
	for i in range(test_num):
		try:
			enc = e.Encryption(N = int(input("Enter a shift value: ")), D = int(input("Enter a direction (1 or -1): ")))	
			test = input("Enter a text to encrypt: ")
			enc_text = enc.encrypt(test)
			print("Your text encrypted: ", enc_text)
			dec_text  = enc.decrypt(enc_text)
			print("Your text decrypted: ", dec_text)
		except ValueError:
			print("Invalid Input Try again")
			continue
	print("Done testing the encryption class")
	return
	
def main():
	print("Testing the Encryptor.py functions")
	test_encryptor()
	
if __name__ == "__main__":
	main()
