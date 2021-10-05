#A wealthy client has forgotten the password to his business website, but he has a list of possible passwords.
# His previous developer has left a file on the server with the name password.txt. You open the file and 
# realize it's in binary format.
#Write a script that takes an array of possible passwords and a string of binary representing the possible 
# password. Convert the binary to a string and compare to the password array. If the password is found, 
# return the password string, else return false;
#decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011')
# ;    => 'password123'
#decode_pass(['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011')
# ;    => False
#decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011')
# ;    => False


def decode_pass(pass_list, bits):
    bin_lst = pass_list[0]
    bin_lst = bin(int.from_bytes(bin_lst.encode(), 'little'))
    #bin_lst = str(' '.join(format(ord(x), 'b') for x in bin_lst))
    print(str(bin_lst))
    for i in bin_lst:
        print(i)
        if i in bits:
            return pass_list[0]
        else:
            False
#https://www.codewars.com/kata/5a731b36e19d14400f000c19/train/python


print(decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
#=> 'password123'
print(decode_pass(['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
#=> False
print(decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
#=> False