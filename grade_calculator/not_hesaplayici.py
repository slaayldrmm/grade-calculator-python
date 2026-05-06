def not_harf_karisligi(puan):
    if puan >= 90: return "AA"
    elif puan >= 85: return "BA"
    elif puan >= 80: return "BB"
    elif puan >= 75: return "CB"
    elif puan >= 70: return "CC"
    else: return "FF - Kaldınız"

def main():
    print("--- Öğrenci Not Hesaplama Sistemi ---")
    try:
        vize = float(input("Vize Notunuzu Giriniz: "))
        final = float(input("Final Notunuzu Giriniz: "))
        
       
        ortalama = (vize * 0.4) + (final * 0.6)
        
        print(f"\nOrtalamanız: {ortalama:.2f}")
        print(f"Harf Notunuz: {not_harf_karisligi(ortalama)}")
        
    except ValueError:
        print("Lütfen sadece sayısal değerler giriniz!")

if __name__ == "__main__":
    main()