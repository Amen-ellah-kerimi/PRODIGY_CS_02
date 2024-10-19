from PIL import Image


# Function to "encrypt" the image by pixelation
def encrypt_image(image_path, pixelation_factor):
    try:
        # Open the image
        image = Image.open(image_path)

        # Reduce the size of the image by the pixelation factor
        small_image = image.resize(
            (image.width // pixelation_factor, image.height // pixelation_factor),
            resample=Image.BILINEAR
        )

        # Scale the image back to its original size
        encrypted_image = small_image.resize(image.size, Image.NEAREST)

        # Save the encrypted (pixelated) image
        encrypted_image.save('encrypted_image.png')
        print(f'Encryption complete! Encrypted image saved as "encrypted_image.png".')

        # Display the encrypted image
        encrypted_image.show()

    except FileNotFoundError:
        print(f'Error: The file "{image_path}" was not found.')


# Function to "decrypt" the image (show pixelated image)
def decrypt_image(image_path):
    try:
        # Open the encrypted image
        image = Image.open(image_path)

        # Display the encrypted image (in pixelated form)
        image.show()

    except FileNotFoundError:
        print(f'Error: The file "{image_path}" was not found.')


# Main execution function
if __name__ == "__main__":
    action = input("Would you like to encrypt or decrypt an image? (e/d): ").lower()

    if action == 'e':
        image_path = input("Enter the path to the image you want to encrypt: ")
        pixelation_factor = int(input("Enter the pixelation factor (e.g., 10 for high encryption): "))
        encrypt_image(image_path, pixelation_factor)

    elif action == 'd':
        image_path = input("Enter the path to the image you want to decrypt: ")
        decrypt_image(image_path)

    else:
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")
