#include <stdio.h>
#include <Python.h>
#include <string.h>

/*
This is a function that is dedicated to printing Python strings.
*/



void print_python_string(PyObject *p)
{
unsigned int len;
const char *str;

/* Flush the standard output */
fflush(stdout);

printf("[.] string object info\n");

/* Check If p is a valid string */
if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

/* retrieving the length of the string */
len = PyUnicode_GET_LENGTH(p);

/* Check if the string is a ASCII compact string */
/* [!] compact string: range (0, 127) */
if (!PyUnicode_IS_COMPACT_ASCII(p))
{
printf("  type: compact unicode object\n");
}
else
{
printf("  type: compact ascii\n");
}

/* get the string values and print */
str = PyUnicode_AsUTF8(p);
printf("  length: %u\n", len);
printf("  value: %s\n", str);

}