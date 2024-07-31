import ctypes
import os

dll_path = os.path.abspath(r"C:\Users\nicol\OneDrive\Escritorio\Strclib_shared\strclib.dll")

if not os.path.exists(dll_path):
    raise FileNotFoundError(f"No se pudo encontrar el archivo DLL en la ruta: {dll_path}")

strclib = ctypes.CDLL(dll_path)

# Define argument and return types
strclib.str_upper_case.argtypes = [ctypes.c_char_p]
strclib.str_lower_case.argtypes = [ctypes.c_char_p]

strclib.to_upper_case.argtypes = [ctypes.c_char_p]
strclib.to_upper_case.restype = ctypes.c_char

strclib.to_lower_case.argtypes = [ctypes.c_char_p]
strclib.to_lower_case.restype = ctypes.c_char

strclib.find_char.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
strclib.find_char.restype = ctypes.c_char_p

strclib.find_char_idx.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
strclib.find_char_idx.restype = ctypes.c_int

strclib.reverse_str_in_situ.argtypes = [ctypes.c_char_p]

strclib.is_palindrome.argtypes = [ctypes.c_char_p]
strclib.is_palindrome.restype = ctypes.c_int

strclib.stringlen.argtypes = [ctypes.c_char_p]
strclib.stringlen.restype = ctypes.c_int

strclib.strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
strclib.strcmp.restype = ctypes.c_int

strclib.strcmp_nocase.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
strclib.strcmp_nocase.restype = ctypes.c_int

strclib.encryption_cesar.argtypes = [ctypes.c_char_p, ctypes.c_int]
strclib.decryption_cesar.argtypes = [ctypes.c_char_p, ctypes.c_int]

# Test functions

def test_str_upper_case():
    text = b"Hello World!"
    text_buffer = ctypes.create_string_buffer(text)
    strclib.str_upper_case(text_buffer)
    assert text_buffer.value.decode('utf-8') == "HELLO WORLD!"

def test_str_lower_case():
    text = b"HELLO WORLD!"
    text_buffer = ctypes.create_string_buffer(text)
    strclib.str_lower_case(text_buffer)
    assert text_buffer.value.decode('utf-8') == "hello world!"

def test_to_upper_case():
    # Prueba con 'a' que debería convertirse en 'A'
    char = b'a'
    result = strclib.to_upper_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('A'), f"Expected 'A', got '{chr(result)}'"

    # Prueba con 'A' que debería permanecer 'A'
    char = b'A'
    result = strclib.to_upper_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('A'), f"Expected 'A', got '{chr(result)}'"

    # Prueba con un carácter que no debe cambiar
    char = b'1'
    result = strclib.to_upper_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('1'), f"Expected '1', got '{chr(result)}'"

    print("All to_upper_case tests passed")



def test_to_lower_case():
    # Prueba con 'A' que debería convertirse en 'a'
    char = b'A'
    result = strclib.to_lower_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('a'), f"Expected 'a', got '{chr(result)}'"

    # Prueba con 'a' que debería permanecer 'a'
    char = b'a'
    result = strclib.to_lower_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('a'), f"Expected 'a', got '{chr(result)}'"

    # Prueba con un carácter que no debe cambiar
    char = b'1'
    result = strclib.to_lower_case(char)
    result = ord(result)  # Convertir el resultado a un entero
    assert result == ord('1'), f"Expected '1', got '{chr(result)}'"

    print("All to_lower_case tests passed")

def test_find_char():
    text = b"Hello World!"
    letter = b"o"
    result = strclib.find_char(text, letter)
    assert result == text[4:]

def test_find_char_idx():
    text = b"Hello World!"
    letter = b"o"
    result = strclib.find_char_idx(text, letter)
    assert result == 4

def test_reverse_str_in_situ():
    text = b"Hello"
    text_buffer = ctypes.create_string_buffer(text)
    strclib.reverse_str_in_situ(text_buffer)
    assert text_buffer.value.decode('utf-8') == "olleH"

def test_is_palindrome():
    palindrome = b"Radar"
    non_palindrome = b"Hello"
    assert strclib.is_palindrome(palindrome) == 1
    assert strclib.is_palindrome(non_palindrome) == 0

def test_stringlen():
    text = b"Hello"
    result = strclib.stringlen(text)
    assert result == 5

def test_strcmp():
    str1 = b"Hello"
    str2 = b"Hello"
    str3 = b"World"
    assert strclib.strcmp(str1, str2) == 0
    assert strclib.strcmp(str1, str3) != 0

def test_strcmp_nocase():
    str1 = b"Hello"
    str2 = b"hello"
    str3 = b"World"
    assert strclib.strcmp_nocase(str1, str2) == 0
    assert strclib.strcmp_nocase(str1, str3) != 0

def test_encryption_cesar():
    text = b"Hello World!"
    offset = 3
    text_buffer = ctypes.create_string_buffer(text)
    strclib.encryption_cesar(text_buffer, offset)
    assert text_buffer.value.decode('utf-8') == "Khoor Zruog!"

def test_decryption_cesar():
    text = b"Khoor Zruog!"
    offset = 3
    text_buffer = ctypes.create_string_buffer(text)
    strclib.decryption_cesar(text_buffer, offset)
    assert text_buffer.value.decode('utf-8') == "Hello World!"

# Run tests
if __name__ == "__main__":
    test_str_upper_case()
    test_str_lower_case()
    test_to_upper_case()
    test_to_lower_case()
    test_find_char()
    test_find_char_idx()
    test_reverse_str_in_situ()
    test_is_palindrome()
    test_stringlen()
    test_strcmp()
    test_strcmp_nocase()
    test_encryption_cesar()
    test_decryption_cesar()

    print("All tests passed!")
