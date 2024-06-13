def caesar_cipher(text, shift):
    """Fungsi untuk melakukan enkripsi atau dekripsi Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def encrypt_message(message, shift):
    """Fungsi untuk mengenkripsi pesan menggunakan Caesar Cipher."""
    return caesar_cipher(message, shift)

def decrypt_message(encrypted_message, shift):
    """Fungsi untuk mendekripsi pesan yang telah dienkripsi menggunakan Caesar Cipher."""
    return caesar_cipher(encrypted_message, -shift)

# Contoh penggunaan
if __name__ == "__main__":
    # Pesan yang akan dikirim
    message = "Ini adalah pesan rahasia"

    # Shift (pergeseran) untuk Caesar Cipher
    shift = 3

    # Enkripsi pesan
    encrypted_message = encrypt_message(message, shift)
    print("Pesan terenkripsi:", encrypted_message)

    # Dekripsi pesan
    decrypted_message = decrypt_message(encrypted_message, shift)
    print("Pesan terdekripsi:", decrypted_message)
