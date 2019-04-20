#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Extendtest.h"
#include "/usr/include/python2.7/Python.h"

int fac(int n)
{
	if(n < 2) return 1;
	return (n) * fac(n-1);
}

char *reverse(char *s)
{
	register char t;
	char *p = s;
	char *q = (s + (strlen(s) - 1));

	while(s && (p < q))
	{
		t = *p;
		*p++ = *q;
		*q-- = t;
	}
	return s;
}

int test()
{
	char s[50];
	printf("4 != %d\n", fac(4));

	strcpy(s, "abcdef");
	printf("reversing 'abcdef', we get '%s'\n", reverse(s));
	return 0;
}


static PyObject *Extendtest_fac(PyObject *self, PyObject *args)
{
	int num;
	if(!PyArg_ParseTuple(args, "i", &num))
		return NULL;
	return (PyObject*)Py_BuildValue("i", fac(num));
}

static PyObject *Extendtest_doppel(PyObject *self, PyObject *args)
{
	char *orig_str;
	char *dupe_str;
	PyObject* retval;

	if(!PyArg_ParseTuple(args, "s", &orig_str))
		return NULL;
	retval = (PyObject*)Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
	free(dupe_str);
	return retval;
}

static PyObject *Extendtest_test(PyObject *self, PyObject *args)
{
	test();
	Py_INCREF(Py_None);
	return (PyObject*)Py_BuildValue("");
}

static PyMethodDef ExtendtestMethods[] = {
	{"fac", Extendtest_fac, METH_VARARGS},
	{"doppel", Extendtest_doppel, METH_VARARGS},
	{"test", Extendtest_test, METH_VARARGS},
	{NULL, NULL}
};

void initExtendtest()
{
	Py_InitModule("Extendtest", ExtendtestMethods);
}