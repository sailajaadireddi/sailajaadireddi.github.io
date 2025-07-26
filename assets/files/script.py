import string

# read the file into a string

with open('message.txt', 'r') as file:

    enc_msg = file.read()

# split the string by ' ' and insert the values into an array

enc_arr = enc_msg.split( )

# print out the array for test purposes

enc_arr_len = len(enc_arr)

# define empty mod_arr

mod_arr = []

# calculate modulo 37 of every number

for i in range(0, enc_arr_len):

        mod_arr.append(round(int(enc_arr[i]) % 37))

# get length of resulting array

mod_arr_len = len(mod_arr)

# define array for final string

final_string = []

for i in range(0, mod_arr_len):

        # try to map numbers from 0 to 25 to uppercase characters of the alphabet
        if 0 <= int(mod_arr[i]) <= 25:

                if(int(mod_arr[i]) == 0):

                        final_string.append('A')

                elif(int(mod_arr[i]) == 1):

                        final_string.append('B')

                elif(int(mod_arr[i]) == 2):

                        final_string.append('C')

                elif(int(mod_arr[i]) == 3):

                        final_string.append('D')

                elif(int(mod_arr[i]) == 4):

                        final_string.append('E')

                elif(int(mod_arr[i]) == 5):

                        final_string.append('F')

                elif(int(mod_arr[i]) == 6):

                        final_string.append('G')

                elif(int(mod_arr[i]) == 7):

                        final_string.append('H')

                elif(int(mod_arr[i]) == 8):

                        final_string.append('I')

                elif(int(mod_arr[i]) == 9):

                        final_string.append('J')

                elif(int(mod_arr[i]) == 10):

                        final_string.append('K')

                elif(int(mod_arr[i]) == 11):

                        final_string.append('L')

                elif(int(mod_arr[i]) == 12):

                        final_string.append('M')

                elif(int(mod_arr[i]) == 13):

                        final_string.append('N')

                elif(int(mod_arr[i]) == 14):

                        final_string.append('O')

                elif(int(mod_arr[i]) == 15):

                        final_string.append('P')

                elif(int(mod_arr[i]) == 16):

                        final_string.append('Q')

                elif(int(mod_arr[i]) == 17):

                        final_string.append('R')

                elif(int(mod_arr[i]) == 18):

                        final_string.append('S')

                elif(int(mod_arr[i]) == 19):

                        final_string.append('T')

                elif(int(mod_arr[i]) == 20):

                        final_string.append('U')

                elif(int(mod_arr[i]) == 21):

                        final_string.append('V')

                elif(int(mod_arr[i]) == 22):

                        final_string.append('W')

                elif(int(mod_arr[i]) == 23):

                        final_string.append('X')

                elif(int(mod_arr[i]) == 24):

                        final_string.append('Y')

                elif(int(mod_arr[i]) == 25):

                        final_string.append('Z')

        # try to map numbers from 26 to 35 to decimal digits

        elif 26 <= int(mod_arr[i]) <= 35:

                if(int(mod_arr[i]) == 26):

                        final_string.append('0')

                elif(int(mod_arr[i]) == 27):

                        final_string.append('1')

                elif(int(mod_arr[i]) == 28):

                        final_string.append('2')

                elif(int(mod_arr[i]) == 29):

                        final_string.append('3')

                elif(int(mod_arr[i]) == 30):

                        final_string.append('4')

                elif(int(mod_arr[i]) == 31):

                        final_string.append('5')

                elif(int(mod_arr[i]) == 32):

                        final_string.append('6')

                elif(int(mod_arr[i]) == 33):

                        final_string.append('7')

                elif(int(mod_arr[i]) == 34):

                        final_string.append('8')

                elif(int(mod_arr[i]) == 35):

                        final_string.append('9')

        # try to map 36 to an underscore _

        elif int(mod_arr[i]) == 36:

                final_string.append("_")
final_flag = ''.join(final_string)
print("picoCTF{" + final_flag + "}")