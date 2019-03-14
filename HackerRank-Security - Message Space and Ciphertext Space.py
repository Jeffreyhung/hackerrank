message = raw_input()

message_list = list(message)
result=''
for i in message_list:
    tem = ( int(i)+1)%10
    result+=str(tem)

print result
