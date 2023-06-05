#include <stdio.h>
#include "Python.h"


void print_python_string(PyObject *p)
{

unsigned int len;
char *str;

/* Flush the standard output */
fflush(stdout);


printf("[.] string object info\n");

/* If p is not a valid string */
if (strcmp(p->ob_type->tp_name, "str") != 0)
{
printf("  [ERROR] Invalid String Object\n");
return;
}

/* retreaving the length of the string */
len = ((PyASCIIObject*)(p))->length;

/* Check if the string is a ASCII compact string */
/* range (0, 127) */
if (!PyUnicode_IS_COMPACT_ASCII(p))
{
printf(" type: compact unicode object\n");
}
else
{
printf(" type: compact ascii\n");
}

/* get the string value by converting it to a wide */
/* character string in case of special chars ex:(在, щ) */
str = PyUnicode_AsWideCharString(p, &len);
printf("  length: %d\n", len);
printf("  value: %s\n", str);

}