def saveTime():
    a = 95
    file = open("time.txt", "a")
    timeNOw = time.localtime()
    file.write(timeNOw)
    file.flush()
    a -= 5
    #with open("time.txt", "a") as file:
     #   file.write(time.localtime())
        

#saveTime()

file=open("data.txt","w")	# creation and opening of a CSV file in Write mode
# Type Program Logic Here
file.write(str(time.localtime())+",")# Writing data in the opened file
# file.flush()
# Internal buffer is flushed (not necessary if close() function is used)
file.write("test")
file.flush()
# The file is closed
