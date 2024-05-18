from PIL import Image
import random
def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size
    random.seed(key)
    random.shuffle(pixels)
    encrypted_img = Image.new(img.mode, (width, height))
    encrypted_img.putdata(pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")
def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    decrypted_pixels = [None] * len(pixels)
    for i, index in enumerate(indices):
        decrypted_pixels[index] = pixels[i]
    decrypted_img = Image.new(img.mode, (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")
def main():
    while True:
        mode = input("Would you like to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
            continue
        image_path = input("Enter the path to the image: ")
        output_path = input("Enter the path to save the output image: ")
        key = input("Enter the encryption/decryption key: ")
        if mode == 'encrypt':
            encrypt_image("C:/Users/mahax/OneDrive/Desktop/input.jpeg","C:/Users/mahax/OneDrive/Desktop/output.jpeg","secret")
        elif mode == 'decrypt':
            decrypt_image("C:/Users/mahax/OneDrive/Desktop/input.jpeg","C:/Users/mahax/OneDrive/Desktop/output.jpeg","secret")
if __name__ == "__main__":
    main()

