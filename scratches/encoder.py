def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    global option
    option = input("Please enter an option: ")

def encode(password):
    global enc_pass
    enc_pass = ""
    for i in range(0, len(password)):
        if int(password[i]) < 7:
            num = int(password[i]) + 3
            enc_pass += str(num)
        else:
            num = int(password[i]) - 7
            enc_pass += str(num)
    print(enc_pass)

def decode(enc_pass):
    dec_pass = ""
    for i in range(0, len(enc_pass)):
        if int(enc_pass[i]) > 3:
            num = int(enc_pass[i]) - 3
            dec_pass += str(num)
        else:
            num = int(enc_pass[i]) + 7
            dec_pass += str(num)
    print(f"The encoded password is {enc_pass}, and the original password is {dec_pass}")



menu()
while True:
    if option == "1":
        password = input("Please input your passcode: ")
        encode(password)
        menu()
        continue
    elif option == "2":
        decode(enc_pass)
        menu()
        continue
    elif option == "3":
        break

