#ifndef STRCLIB_H_INCLUDED
#define STRCLIB_H_INCLUDED

#include <stdlib.h>

#define ISMINUS(c)(c>='a' && c<='z')
#define ISMAYUS(c)(c>='A' && c<='Z')
#define ISCHAR(c)((c>='a' && c<='z') || (c>='A' && c<='Z'))


void str_upper_case(char* c);
void str_lower_case(char* c);
char to_upper_case(const char* c);
char to_lower_case(const char* c);
char* find_char(const char* str, const char* c);
int find_char_idx(const char* str, const char* c);
void reverse_str_in_situ(char* str);
int is_palindrome(const char* str);
int stringlen(const char* str);
int strcmp(const char* str1, const char* str2);
int strcmp_nocase(const char* str1, const char* str2);

void encryption_cesar(char* str, int offset);
void decryption_cesar(char* str, int offset);


#endif // STRCLIB_H_INCLUDED
