#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
    PyObject *encoded_str;
    PyObject *utf8_str;

    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
        else
            printf("  type: compact unicode object\n");

        printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));

        // Convert the Python Unicode object to a UTF-8 encoded string
        encoded_str = PyUnicode_AsUTF8String(p);
        if (encoded_str != NULL)
        {
            // Convert the encoded string to a C string
            utf8_str = PyBytes_AsString(encoded_str);
            if (utf8_str != NULL)
            {
                printf("  value: %s\n", utf8_str);
            }
            else
            {
                printf("  [ERROR] Failed to convert to UTF-8 string\n");
            }
            // Don't forget to release the memory
            Py_XDECREF(encoded_str);
        }
        else
        {
            printf("  [ERROR] Failed to encode string to UTF-8\n");
        }
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
