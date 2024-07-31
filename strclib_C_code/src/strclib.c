#include "../include/strclib.h"

void str_upper_case(char* c)
{
    while(*c)
    {
        if(ISMINUS(*c))
        {
            *c = *c - 32;
        }
        c++;
    }
}


void str_lower_case(char* c)
{
    while(*c)
    {
        if(ISMAYUS(*c))
        {
            *c = *c + 32;
        }
        c++;
    }
}

char to_upper_case(const char* c)
{
    if(ISMINUS(*c))
    {
        return *c - 32;
    }
    return *c;
}
char to_lower_case(const char* c)
{
    if(ISMAYUS(*c))
    {
        return *c + 32;
    }
    return *c;
}
char* find_char(const char* str, const char* c)
{
    while(*str)
    {
        if(*c == *str)
        {
            return (char*)str;
        }
        str++;
    }
    return NULL;
}
int find_char_idx(const char* str, const char* c)
{
    int idx = 0;
    while(*str)
    {
        if(*c == *str)
        {
            return idx;
        }
        str++;
        idx++;
    }

    return -1;
}
void reverse_str_in_situ(char* str)
{
    int len = 0;
    char* ps = str, *pf, aux;
    while(*ps)
    {
        len++;
        ps++;
    }
    if(len < 1)
    {
        return;
    }
    ps = str;
    pf = str + len - 1;
    while(ps < pf)
    {
        aux = *ps;
        *ps = *pf;
        *pf = aux;
        ps++;
        pf--;
    }

}

int is_palindrome(const char* str)
{
    int len = 0;
    char* ps = (char*)str, *pf;
    while(*str)
    {
        len++;
        str++;
    }
    pf = ps + len - 1;
    while(ps < pf)
    {
        while(!ISCHAR(*ps))
        {
            ps++;
        }
        while(!ISCHAR(*pf))
        {
            pf--;
        }

        if(to_lower_case(ps)!= to_lower_case(pf))
        {
            return 0;
        }
        ps++;
        pf--;
    }

    return 1;
}
int stringlen(const char* str)
{
    int c = 0;
    while(*str)
    {
        c++;
        str++;
    }
    return c;
}
int strcmp(const char* str1, const char* str2)
{
    while(*str1 && *str2 && *str1 == *str2)
    {
        str1++;
        str2++;
    }

    return *str1 - *str2;
}

int strcmp_nocase(const char* str1, const char* str2)
{
    while(*str1 && *str2 && (to_upper_case((char*)str1))==(to_upper_case((char*)str2)))
    {

        str1++;
        str2++;
    }

    return (to_upper_case(str1) - to_upper_case(str2));
}

void encryption_cesar(char* str, int offset)
{
    char c;
    while(*str)
    {
        c = *str;
        if(c>= 'A' && c <='Z')
        {
            c = (c - 'A' + offset) % 26 + 'A';
        }
        else if (c>= 'a' && c <='z')
        {
            c = (c - 'a' + offset) % 26 + 'a';
        }
        *str = c;
        str++;
    }
}

void decryption_cesar(char* str, int offset)
{
    char c;
    while(*str)
    {
        c = *str;
        if(c>= 'A' && c <='Z')
        {
            c = (c - 'A' - offset + 26) % 26 + 'A';
        }
        else if (c>= 'a' && c <='z')
        {
            c = (c - 'a' - offset + 26) % 26 + 'a';
        }
        *str = c;
        str++;
    }
}

