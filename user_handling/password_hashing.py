from argon2 import PasswordHasher

class PasswordHashing:
    def __init__(self):
        self.ph = PasswordHasher()

    def hash_password(self, password):
        return self.ph.hash(password)

    def verify_password(self, hashed_password, input_password):
        try:
            # Verify the input password against the stored hash -> return True
            return self.ph.verify(hashed_password, input_password)
        except:
            # If verification fails (e.g., wrong password) -> return False
            return False