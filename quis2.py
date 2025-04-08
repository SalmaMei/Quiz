# Fungsi untuk mengenkripsi teks menggunakan Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    # Membuat hasil enkripsi
    ciphertext = []
    
    # Menyusun nilai abjad (A=0, B=1, ..., Z=25)
    plaintext = plaintext.upper()  # Mengubah menjadi huruf kapital
    key = key.upper()  # Mengubah kunci menjadi huruf kapital
    
    # Panjang plaintext dan kunci
    text_len = len(plaintext)
    key_len = len(key)
    
    for i in range(text_len):
        # Mengambil nilai dari huruf plaintext dan kunci
        p = ord(plaintext[i]) - ord('A')  # Mengubah ke nilai numerik
        k = ord(key[i % key_len]) - ord('A')  # Mengambil kunci berulang
        
        # Enkripsi dengan Vigenère: (P + K) mod 26
        c = (p + k) % 26
        
        # Menambahkan huruf hasil enkripsi ke ciphertext
        ciphertext.append(chr(c + ord('A')))  # Mengubah kembali ke huruf
    
    # Menggabungkan ciphertext menjadi string
    return ''.join(ciphertext)

# Plaintext dan kunci
plaintext = "DISEB"  # 5 huruf pertama dari teks
key = "SALMA"

# Mengenkripsi plaintext
encrypted_text = vigenere_encrypt(plaintext, key)

# Menampilkan hasil enkripsi
print("Plaintext: ", plaintext)
print("Kunci: ", key)
print("Encrypted Text: ", encrypted_text)
