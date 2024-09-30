import cv2
import numpy as np

def encrypt_image(image_path, output_path):
  """Encrypts an image by swapping pixel values horizontally.

  Args:
    image_path: Path to the input image.
    output_path: Path to save the encrypted image.
  """

  img = cv2.imread(image_path)
  height, width, channels = img.shape

  # Create a copy of the image to avoid modifying the original
  encrypted_img = img.copy()

  # Swap pixel values horizontally
  for y in range(height):
    for x in range(width // 2):
      encrypted_img[y, x], encrypted_img[y, width - x - 1] = encrypted_img[y, width - x - 1], encrypted_img[y, x]

  cv2.imwrite(output_path, encrypted_img)

def decrypt_image(encrypted_image_path, output_path):
  """Decrypts an image previously encrypted by swapping pixel values horizontally.

  Args:
    encrypted_image_path: Path to the encrypted image.
    output_path: Path to save the decrypted image.
  """

  encrypted_img = cv2.imread(encrypted_image_path)
  height, width, channels = encrypted_img.shape

  # Decryption is the same as encryption for this method
  decrypted_img = encrypt_image(encrypted_image_path, output_path)

def main():
  image_path = input("Enter the input image path: ")
  mode = input("Enter mode (encrypt/decrypt): ")
  output_path = input("Enter the output image path: ")

  if mode == "encrypt":
    encrypt_image(image_path, output_path)
    print("Image encrypted successfully!")
  elif mode == "decrypt":
    decrypt_image(image_path, output_path)
    print("Image decrypted successfully!")
  else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
  main()
  