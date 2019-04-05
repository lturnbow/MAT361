from modexp import modexp
from multinv import multinv


# This function is for sender to request RSA modulus N and 
# RSA encryption e from another team.
# Arguments:
# a - the selected secret number
# m_s - the requester's team ID
# N_s - the requester's RSA modulus N
# prime1 - N_s = prime1 * prime2
# prime2 - N_s = prime1 * prime2
# e_s - the requester's RSA encryption exponent e
# r_r - the receiver's ElGamal key r
# p_r - the receiver's ElGamal key p
def request(a, m_s, N_s, prime1, prime2, e_s, r_r, p_r):
	A = modexp(r_r, a, p_r)
	d = multinv(e_s, prime1 * prime2)
	signature = modexp(m_s, d, N_s)

	print("[A, Ns, es, ms^ds] =")
	print([A, N_s, e_s, signature])
	return([A, N_s, e_s, signature])


# This function is for checking the digital signature when 
# received a request. S^e (mod N) should equal to m_s.
# Arguments:
# A - received A = r^a
# N - received N (requester's N)
# e - received e (requester's e)
# S - signature
# m_s - signatured message
def checkDigitalSignature(A, N, e, S, m_s):
	signature = modexp(S, e, N)
	if signature != m_s:
		print("Signature check fails.")
	else:
		print("Signature check success.")


# This function is for encrypting message using ElGamal.
# Arguments:
# A - received A
# b - the selected secret number
# r_s - the ElGamal key r
# p_s - the ElGamal key p
# message - message to be encrypted
def elGamalEncrypt(A, b, r_s, p_s, message):
	B = modexp(r_s, b, p_s)
	encrypted = modexp(message * modexp(A, b, p_s), 1, p_s)

	print("[B encypted]")
	print([B encrypted])
	return ([B encrypted])


# This function is for decrypting message.
# Arguments:
# B - received B
# a - the secret number selected before
# p_s - the ElGamal key of the message sender
# encrypted - the encrypted message from the message sender
def elGamalDecrypt(B, a, p_s, encrypted):
	R = modexp(B, a, p_s)
	invR = multinv(R, p_s)
	decrypted = modexp(encrypted * invR, 1, p_s)

	print("[decrypted]")
	print([decrypted])
	return ([decrypted])


# This function is for prompting inputs from the user.
def sendRequest():
	print("Send A, Ns, es, ms^ds to request other's N and e.")
	a = int(input("Decide a secret a: "))
	m = int(input("Your team ID: "))
	N = int(input("Your RSA modulus N = p * q: "))
	p1 = int(input("Enter p: "))
	p2 = int(input("Enter q: "))
	e = int(input("Your RSA encryption e: "))
	r = int(input("The ElGamal key r of whom you are sending request to: "))
	p = int(input("The ElGamal key p of whom you are sending request to: "))
	request(a, m, N, p1, p2, e, r, p)
	print("================================================")


# This function is for prompting inputs from the user.
def receiveRequest():
	print("Check the digital signature on received request.")
	A = int(input("The A you received: "))
	N = int(input("The N you received: "))
	e = int(input("The e you received: "))
	S = int(input("The encoded message you received: "))
	expected = int(input("The expected result: "))
	checkDigitalSignature(A, N, e, S, expected)
	print("================================================")


# This function is for prompting inputs from the user.
def sendResponse():
	print("Send encrypted N, e to requester.")
	A = int(input("The A you received: "))
	b = int(input("Decide a secret b: "))
	r = int(input("Your ElGamal key r: "))
	p = int(input("Your ElGamal key p: "))
	message = int(input("Message to be encrypted: "))
	elGamalEncrypt(A, b, r, p, message)
	print("================================================")


# This function is for prompting inputs from the user.
def receiveResponse():
	print("Decrypt the received message.")
	B = int(input("The B you received: "))
	a = int(input("Your secret a: "))
	p = int(input("The ElGamal key p of the sender: "))
	encrypted = int(input("The encrypted message: "))
	elGamalDecrypt(B, a, p, encrypted)
	print("================================================")


def main():
	run = 1
	while run:
		print("(1) Send Request")
		print("(2) Receive Request (Check Digital Signature)")
		print("(3) Send Response")
		print("(4) Receive Response")

		run = int(input("Select one (0 to quit): "))
		if run == 0:
			break
		elif run == 1:
			sendRequest()
		elif run == 2:
			receiveRequest()
		elif run == 3:
			sendResponse()
		elif run == 4:
			receiveResponse()


if __name__ == "__main__":
	main()