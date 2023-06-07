#include <stdio.h>
#include <string.h>
#include <Python.h>

void print_python_string(PyObject *p) {
    unsigned int len;
    const char *str;

    /* Flush the standard output */
    fflush(stdout);

    printf("[.] string object info\n");

    /* If p is not a valid string */
    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* retrieving the length of the string */
    len = PyUnicode_GET_LENGTH(p);

    /* Check if the string is a ASCII compact string */
    /* range (0, 127) */
    if (!PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact unicode object\n");
    }
    else {
        printf("  type: compact ascii\n");
    }

    /* get the string value */
    str = PyUnicode_AsUTF8(p);
    printf("  length: %u\n", len);
    printf("  value: %s\n", str);
}