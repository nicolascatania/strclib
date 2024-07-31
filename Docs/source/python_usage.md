# Python Usage

To use the C library in Python, you can utilize the `ctypes` library to interface with the `.dll`.

## Example Usage

Here is how you can call the `find_char` function from Python:

```python
import ctypes

# Load the DLL
lib = ctypes.CDLL('path/to/strclib.dll')

# Define the function argument and return types with ctypes functions.
# IT MUST BE DONE WITH ALL THE FUNCTIONS YOU WILL USE
lib.find_char.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.find_char.restype = ctypes.POINTER(ctypes.c_char)

# Example usage
word = b"Hello world"
letter = b'o'
# Here you call the function
result = lib.find_char(word, letter)
if not result:
    print("NOT FOUND")
else:
    print(f"{result.contents.value.decode()}")  # Output: "o"