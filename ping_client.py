# ping_client.py - BrennerCampos

from time import *
from socket import *

localhost = '127.0.0.1'


# Send 10 ping request messages
for i in range(1, 11):

    # Create client UDP socket
    cSocket = socket(AF_INET, SOCK_DGRAM)

    # Current time in calendar format
    dateTime = ctime()



    # begin RTT timer
    startTime = time()

    # Set a timeout value of 0.5
    cSocket.settimeout(0.5)


    try:

        requestMessage = bytes("Ping " + str(i) + " " + dateTime, 'utf8')

        cSocket.sendto(requestMessage, (localhost, 12000))
        # os.system('ping 127.0.0.1')
        echoMessage, rand = cSocket.recvfrom(1024)

        # end RTT timer
        endTime = time()

        # RTT is equal to endTime minus startTime
        RTT = endTime - startTime

        print(echoMessage.decode())
        print("Reply from "+localhost+" RTT: "+str(float(RTT)))
        print()
    except:
        print(requestMessage.decode())
        print("Time out")
        print()
