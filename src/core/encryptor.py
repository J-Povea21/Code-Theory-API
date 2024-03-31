# In this module, we will implement the encryption and decryption functions

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
set_length = len(alphabet)

def encrypt(shift: int, text: str) -> str:
    return __encryptor(shift, text.upper())

def decrypt(shift: int, encrypted_text:str) -> str:
    return __encryptor(-shift, encrypted_text.upper(), True)

def __encryptor(shift: int, msg: str, decrypt: bool = False) -> str:
    
    if shift <= 0 and not decrypt:
        return {"success": False, "message": "Invalid shift. It must be positive, try again!"}
    elif msg is None or msg == '':
        return {"sucess": False, "message": "Invalid message! Please submit a valid one"} 
    
    encrypted_text = ''
    try:
        for char in msg:
            encrypted_index = (alphabet.index(char) + shift) % set_length
            encrypted_text += alphabet[encrypted_index]
        
        return {"success": True, "message": encrypted_text }
    except ValueError:
        return {"success": False,"message":"Ups! You inserted a character that we don´t support, try again"}
    except Exception as e:
        return {"success": False,"message": e.args[0]}
