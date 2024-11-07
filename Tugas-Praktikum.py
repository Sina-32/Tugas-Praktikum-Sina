print(f"Silahkan Login")

def login():
    username_terdaftar = "Daspro2024"
    password_terdaftar = "Latihan"
    kesempatan = 5
    
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == username_terdaftar and password == password_terdaftar:
            print("Login berhasil!")
            return
        else:
            kesempatan -= 1
            if kesempatan == 0:
                break  
            if username != username_terdaftar and password != password_terdaftar:
                print(f"Username dan password anda salah kesempatan tersisa: {kesempatan}")
            elif username != username_terdaftar:
                print(f"Username anda salah kesempatan tersisa: {kesempatan}")
            elif password != password_terdaftar:
                print(f"Password anda salah kesempatan tersisa: {kesempatan}")
    
    print("Anda telah keluar dari sistem login")

login()

