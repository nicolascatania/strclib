
# C Usage

### `void str_upper_case(char* c)`
Optimized for strings.
- **Parameters**: Pointer to `char`.
- **Return type**: `void`.
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
- **Example**:
  ```c
  char str[] = "hEllo";
  str_upper_case(str);
  printf("%s\n", str); // Output: "HELLO"

### `void str_lower_case(char* c)`
Optimized for strings.
- **Parameters**: Pointer to `char`.
- **Return type**: `void`.
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char str[] = "HeLlO";
  str_lower_case(str);
  printf("%s\n", str); // Output: "hello"

### `char to_upper_case(const char* c)`
Converts a single character to uppercase.
- **Parameters**: Pointer to `const char`.
- **Return type**: `char`.
- **Raisings**: If the input character is not a lowercase letter, it remains unchanged.
  ```c
  char c = 'a';
  char r = to_upper_case(&c);
  printf("%c\n", r); // Output: "A"

### `char to_lower_case(const char* c)`
Converts a single character to lowercase.
- **Parameters**: Pointer to `const char`.
- **Return type**: `char`.
- **Raisings**: If the input character is not an uppercase letter, it remains unchanged.
  ```c
  char c = 'A';
  char r = to_lower_case(&c);
  printf("%c\n", r); // Output: "a"

### `char* find_char(const char* str, const char* c)`
Finds the first occurrence of a character in a string.
- **Parameters**: Pointer to `const char` for both string and character.
- **Return type**: Pointer to `char` (location of the character or `NULL` if not found).
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Hello world";
  const char letter = '0';
  char* result = find_char(word, &letter);
  if(!result)
  {
    puts("NOT FOUND");
  }
  else
  {
    printf("%c\n", *result); // Output: "o" from Hello, or the direction of its memory position. 
  }

### `int find_char_idx(const char* str, const char* c)`
Finds the index of the first occurrence of a character in a string.
- **Parameters**: Pointer to `const char` for both string and character.
- **Return type**: `int` (index of the character or `-1` if not found).
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Hello world";
  const char letter = '0';
  int result = find_char(word, &letter);
  if(result==-1)
  {
    puts("NOT FOUND");
  }
  else
  {
    printf("%d\n", result); // Output: 4, index of 'o' from Hello. 
  }

### `void reverse_str_in_situ(char* str)`
Reverses a string in place.
- **Parameters**: Pointer to `char`.
- **Return type**: `void`.
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Hello";
  reverse_str_in_situ(word);
  printf("%s\n", word); //Output: olleH.


### `int is_palindrome(const char* str)`
Checks if a string is a palindrome.
- **Parameters**: Pointer to `const char`.
- **Return type**: `int` (1 if the string is a palindrome, 0 otherwise).
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Radar";
  if(is_palindrome(word))
  {
    puts("¡Is palindrome!");
  }
  else
  {
    puts("Not palindrome");
  }



### `int stringlen(const char* str)`
Calculates the length of a string.
- **Parameters**: Pointer to `const char`.
- **Return type**: `int` (length of the string).
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Radar";
  printf("Length: %d\n", stringlen(word));//Output 5

### `int strcmp(const char* str1, const char* str2)`
Compares two strings.
- **Parameters**: Pointers to `const char` for both strings.
- **Return type**: `int` (difference between the first unmatched characters, or 0 if strings are equal). The substract works Left to Right.
- **Raisings**: If any string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Radar", word2[]="RaDAR";
  if(strcmp(word,word2)==0)
  {
    puts("Equal");
  }
  else
  {
    puts("Not equal");
  }//Output Not equal 

### `int strcmp_nocase(const char* str1, const char* str2)`
Compares two strings without case sensitivity.
- **Parameters**: Pointers to `const char` for both strings.
- **Return type**: `int` (difference between the first unmatched characters, or 0 if strings are equal).
- **Raisings**: If any string lacks a `\0` terminator, it may cause issues.
  ```c
  char word[] = "Radar", word2[]="RaDAR";
  if(strcmp_nocase(word,word2)==0)
  {
    puts("Equal");
  }
  else
  {
    puts("Not equal");
  }//Output Equal 

### `void encryption_cesar(char* str, int offset)`
Encrypts a string using the Caesar cipher.
- **Parameters**: Pointer to `char` for the string and an `int` for the offset.
- **Return type**: `void`.
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
  ```c
    char str[] = "abc";
    encryption_cesar(str, 3);
    printf("%s\n", str); // Output: "def"   

### `void decryption_cesar(char* str, int offset)`
Decrypts a string encrypted with the Caesar cipher.
- **Parameters**: Pointer to `char` for the string and an `int` for the offset.
- **Return type**: `void`.
- **Raisings**: If the string lacks a `\0` terminator, it may cause issues.
    ```C
    char str[] = "def";
    decryption_cesar(str, 3);
    printf("%s\n", str); // Output: "abc"