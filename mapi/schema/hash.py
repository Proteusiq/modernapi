from passlib.context import CryptContext

password_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return password_ctx.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return password_ctx.verify(plain_password, hashed_password)
