#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0, size_p, allocated_ptr;
  
	PyObject *data;

	size_p = PyList_Size(p);
	allocated_ptr = ((PyListObject *)p)->allocated;
  
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated_ptr);
  
	while (i < size_p)
	{
		data = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, data->ob_type->tp_name);
		i++;
	}
}
