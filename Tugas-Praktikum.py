print(f"Silahkan Login")

def login():
    username_terdaftar = "Daspro2024"
    password_terdaftar = "Latihan"
    kesempatan = 3
    
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == username_terdaftar and password == password_terdaftar:
            print("Login berhasil!")
            return
        else:
            kesempatan -= 1
            if kesempatan == 0:
                break  # Keluar dari loop langsung jika kesempatan habis
            if username != username_terdaftar and password != password_terdaftar:
                print(f"Username dan password salah! Kesempatan tersisa: {kesempatan}")
            elif username != username_terdaftar:
                print(f"Username salah! Kesempatan tersisa: {kesempatan}")
            elif password != password_terdaftar:
                print(f"Password salah! Kesempatan tersisa: {kesempatan}")
    
    print("Anda telah keluar dari sistem login")

login()

