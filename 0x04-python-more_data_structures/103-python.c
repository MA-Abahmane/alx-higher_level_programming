#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p)
{

if ((!PyBytes_CheckExact(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

}

void print_python_bytes(PyObject *p)
{

if ((!PyList_CheckExact(p))
return;

}
