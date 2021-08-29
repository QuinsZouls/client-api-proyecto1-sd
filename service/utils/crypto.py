from cryptography.fernet import Fernet
import os
SECRET_KEY = os.getenv('SECRET_KEY', Fernet.generate_key()).encode()

def encryptImage(image):
  f = Fernet(SECRET_KEY)
  return f.encrypt(image.encode())

def decryptImage(image):
  f = Fernet(SECRET_KEY)
  return f.decrypt(image.encode())