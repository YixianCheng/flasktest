from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# 这是user会在form里提供的信息
password = "something"

# 密码加密
hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password)

# 判断密码是否正确
check = bcrypt.check_password_hash(hashed_password,'nothing')

print(check)

# 或者
from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('password')
print(hashed_pass)
check = check_password_hash(hashed_pass,'wrongword')
print(check)
