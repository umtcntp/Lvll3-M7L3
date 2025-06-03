import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test eder"""
    desired_length = 50
    password = generate_password(desired_length)
    assert len(password) == desired_length

def test_password_uniqueness():
    """Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test eder"""
    password1 = generate_password(30)
    password2 = generate_password(30)
    assert password1 != password2
