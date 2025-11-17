def input_angka(prompt):
    """
    Fungsi untuk input angka dengan error handling
    Mengulang sampai user input angka yang valid
    """
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < 0:
                print("❌ Error: Masukkan angka positif!")
                continue
            return nilai
        except ValueError:
            print("❌ Error: Masukkan angka yang valid!")

def input_integer(prompt):
    """
    Fungsi untuk input bilangan bulat dengan error handling
    """
    while True:
        try:
            nilai = int(input(prompt))
            if nilai < 0:
                print("❌ Error: Masukkan angka positif!")
                continue
            return nilai
        except ValueError:
            print("❌ Error: Masukkan bilangan bulat yang valid!")