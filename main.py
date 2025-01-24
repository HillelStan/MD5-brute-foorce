import itertools
import hashlib
import threading
def generate_passwords ():
    words = "0123456789abc" # passwords character
    # abcdefghijklmnopqrstuvwxyz
    passwords= list(itertools.product(words , repeat=5)) # random combination
    return passwords
def calculate_md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def decode_md5(hashed_password):
    possible_passwords = generate_passwords()
    for password in possible_passwords:
        password = "".join(password)
        print(f"Trying: {password}")
        if calculate_md5(password) == hashed_password:
            print(f"The password is: {password}")
            return password
    print("password not found!")
    return None
if __name__ =="__main__":
    #63888
    decode_md5(hashed_password="87e372e4c19d97439c2afb5b08d96697")
    """ אופציה לקחת את הרשימה ולחלק אותה לכמה טרדים שירוצו בו זמנית וזה יפחית מהזמן ב40%"""
    