#include <Python.h>

static PyObject * demo_add(PyObject *self, PyObject *args)
{
    const int a, b;
    if(!PyArg_ParseTuple(args, 'ii', &a, &b))
        return NULL;
    return Py_BuildValue('i', a+b);
}

static PyMethodDef DemoMethods[] = {
    {"add", demo_add, METH_VARARGS, "add two integers"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initdemo(void){
    (void)Py_InitModule("demo", DemoMethods);
}