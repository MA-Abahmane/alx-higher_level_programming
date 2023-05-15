#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - a C function that prints some basic info about Python lists.
 * @p: pointer to a pointer to a Python list object.
 *
 * Return: NONE
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t i, p_len, allocated_ptrs;
PyObject *data;

/* get the length of the Pyhton list object p, works like len(p) */
p_len = PyList_Size(p);

/* get the number on pointer to python list objs that are allocated */
allocated_ptrs = ((PyListObject *)p)->allocated;

/* output */
print("[*] Size of the Python List = %ld", size);
print("[*] Allocated = %ld", allocated_ptrs);

/* from list object 'p' get each elements with ptr 'data' with index 'i' */
/* then get elements type name 'data_type'/print element type and its index */
for (i = 0; i < p_len; i++)
{
    
data = PyList_GET_ITEM(p, i);
const char* data_type = data->ob_type->tp_name;

printf("Element %ld: %s\n", i, data_type);  
}
}
