print(f"Silahkan Login")
Login = 3
while Login > 0:
    Username = input("Username : ")
    Password = input("Password : ")

    if Username == "loginUTS" and Password == "rpl2024":
        print("Selamat datang di aplikasi prodi RPL")
        break
    else:
        Login -= 1
        if Login > 0:
            print(f"Login Salah! Kesempatan Anda {Login}x kali lagi")
        else:
            print(f"Anda tidak diperkenankan mengakses aplikasi ini.")