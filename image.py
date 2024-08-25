from PIL import Image


def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by modifying pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply the key to each pixel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")


def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by reversing the pixel modification
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse the key effect
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    img.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")


if __name__ == "__main__":
    # Example usage
    key = 50  # Simple integer key for encryption/decryption

    # Paths to input and output images
    input_image = "input.jpg"  # Replace with your input image path
    encrypted_image = "encrypted_image.jpg"
    decrypted_image = "decrypted_image.jpg"

    # Encrypt and decrypt the image
    encrypt_image(input_image, encrypted_image, key)
    decrypt_image(encrypted_image, decrypted_image, key)
