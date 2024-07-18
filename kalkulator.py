print(
    """
    Menu:
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    """
)

jawaban_menu = str(input("Jawaban anda: "))

if (jawaban_menu.strip() == "1" or jawaban_menu.strip().lower() == "penjumlahan"):
    try:
        var1 = float(input("Masukan angka pertama: ").replace(" ", ""))
        var2 = float(input("Masukan angka kedua: ").replace(" ", ""))

        hasil = var1 + var2

        print(f"Hasil {hasil}")
    except ValueError:
        print("Masukan input berupa angka!")
    except Exception as e:
        print(f"Error: {e}")
elif (jawaban_menu.strip() == "2" or jawaban_menu.strip().lower() == "pengurangan"):
    try:
        var1 = float(input("Masukan angka pertama: ").replace(" ", ""))
        var2 = float(input("Masukan angka kedua: ").replace(" ", ""))

        hasil = var1 - var2

        print(f"Hasil {hasil}")
    except ValueError:
        print("Masukan input berupa angka!")
    except Exception as e:
        print(f"Error: {e}")
elif (jawaban_menu.strip() == "3" or jawaban_menu.strip().lower() == "perkalian"):
    try:
        var1 = float(input("Masukan angka pertama: ").replace(" ", ""))
        var2 = float(input("Masukan angka kedua: ").replace(" ", ""))

        hasil = var1 * var2

        print(f"Hasil {hasil}")
    except ValueError:
        print("Masukan input berupa angka!")
    except Exception as e:
        print(f"Error: {e}")
elif (jawaban_menu.strip() == "4" or jawaban_menu.strip().lower() == "pembagian"):
    try:
        var1 = float(input("Masukan angka pertama: ").replace(" ", ""))
        var2 = float(input("Masukan angka kedua: ").replace(" ", ""))

        hasil = var1 / var2

        print(f"Hasil {hasil}")
    except ValueError:
        print("Masukan input berupa angka!")
    except ZeroDivisionError:
        print("Tidak bisa membagi bilangan dengan nol!")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Invalid Input")