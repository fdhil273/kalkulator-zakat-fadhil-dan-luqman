from data_zakat import *
from validasi import input_angka, input_integer

class KalkulatorZakat:
    def __init__(self):
        self.harga_emas = 0
        self.harga_beras = 0
    
    def set_harga_terkini(self):
        print("\n=== INPUT HARGA TERKINI ===")
        self.harga_emas = input_angka("Harga emas per gram saat ini (Rp): ")
        self.harga_beras = input_angka("Harga beras per kg (Rp): ")
        print("✓ Harga berhasil diupdate!")
    
    def info_zakat(self):
        print("\n" + "="*50)
        print("INFORMASI TENTANG ZAKAT")
        print("="*50)
        print(f"Pengertian (Bahasa): {PENGERTIAN_ZAKAT['bahasa']}")
        print(f"Pengertian (Istilah): {PENGERTIAN_ZAKAT['istilah']}")
        
        print("\nPENERIMA ZAKAT (8 Golongan):")
        for i, penerima in enumerate(PENERIMA_ZAKAT, 1):
            print(f"{i}. {penerima}")
        
        print(f"\nHUKUM ZAKAT:")
        print(HUKUM_ZAKAT)
        
        print("SYARAT WAJIB ZAKAT:")
        for i, syarat in enumerate(SYARAT_ZAKAT, 1):
            print(f"{i}. {syarat}")
        
        input("\nTekan Enter untuk kembali ke menu...")
    
    def zakat_fitrah(self):
        print("\n" + "="*50)
        print("ZAKAT FITRAH")
        print("="*50)
        print("Ketentuan: 2.5 kg makanan pokok per orang")
        
        if self.harga_beras == 0:
            self.harga_beras = input_angka("Harga beras per kg (Rp): ")
        
        jumlah_orang = input_integer("Jumlah orang yang wajib zakat: ")
        
        # Validasi jumlah orang
        if jumlah_orang == 0:
            print("❌ Jumlah orang tidak boleh 0!")
            return
        
        total_beras = NISAB['fitrah'] * jumlah_orang
        total_uang = total_beras * self.harga_beras
        
        print(f"\n=== HASIL PERHITUNGAN ZAKAT FITRAH ===")
        print(f"Jumlah orang: {jumlah_orang} orang")
        print(f"Zakat beras: {total_beras} kg beras")
        print(f"Zakat uang: Rp {total_uang:,.0f}")
        print(f"\nWaktu pembayaran: Malam idul fitri hingga sebelum sholat id")
        
        input("\nTekan Enter untuk kembali ke menu...")
    
    def zakat_mal(self):
        print("\n" + "="*50)
        print("ZAKAT MAL (HARTA)")
        print("="*50)
        print("Ketentuan: Nisab 85 gram emas, Haul 1 tahun, Kadar 2.5%")
        
        if self.harga_emas == 0:
            self.harga_emas = input_angka("Harga emas per gram (Rp): ")
        
        total_harta = input_angka("Total harta/simpanan (Rp): ")
        hutang = input_angka("Total hutang (Rp): ")
        
        # Validasi hutang tidak lebih dari harta
        if hutang > total_harta:
            print("❌ Error: Hutang tidak boleh lebih dari total harta!")
            return
        
        # Hitung nisab dalam rupiah
        nisab_rupiah = NISAB['emas'] * self.harga_emas
        harta_bersih = total_harta - hutang
        
        print(f"\nNisab (85 gram emas): Rp {nisab_rupiah:,.0f}")
        print(f"Harta bersih: Rp {harta_bersih:,.0f}")
        
        if harta_bersih >= nisab_rupiah:
            zakat = KADAR_ZAKAT['mal'] * harta_bersih
            print(f"\n=== ANDA WAJIB ZAKAT ===")
            print(f"Zakat yang harus dibayar: Rp {zakat:,.0f}")
            print(f"(2.5% dari harta bersih)")
        else:
            print(f"\n=== BELUM WAJIB ZAKAT ===")
            print(f"Harta bersih Anda belum mencapai nisab")
        
        input("\nTekan Enter untuk kembali ke menu...")
    
    def main_menu(self):
        calculator = KalkulatorZakat()
        
        while True:
            print("\n" + "="*50)
            print("KALKULATOR ZAKAT - BERDASARKAN DATA SYAR'I")
            print("="*50)
            print("1. Informasi Tentang Zakat")
            print("2. Input Harga Terkini (Emas & Beras)")
            print("3. Zakat Fitrah")
            print("4. Zakat Mal (Harta)")
            print("5. Keluar")
            print("="*50)
            
            pilihan = input("Pilihan menu (1-5): ").strip()
            
            if pilihan == "1":
                calculator.info_zakat()
            elif pilihan == "2":
                calculator.set_harga_terkini()
            elif pilihan == "3":
                calculator.zakat_fitrah()
            elif pilihan == "4":
                calculator.zakat_mal()
            elif pilihan == "5":
                print("\nTerima kasih! Semoga menjadi amal sholeh 🤲")
                print("Program selesai.")
                break
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 1-5")
                input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    kalkulator = KalkulatorZakat()
    kalkulator.main_menu()