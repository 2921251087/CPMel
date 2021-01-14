#include "base_class.h"
#include"iter.h"
#include"double3.h"
#include"matrix_class.h"
#include"matrix_array.h"
//�в���t�޲���METH_NOARGS������METH_O��ֵ�Բ���METH_KEYWORDS

static PyMethodDef SpamMethods[] = {
	{"NewMatrixs",
	(PyCFunction)NewMatrixs,
	METH_VARARGS,
	"����Matrix����Ԫ��"
	},
	{"NewDouble3s",
	(PyCFunction)NewDouble3s,
	METH_VARARGS,
	"����Double3����Ԫ��"
	},
    {0, 0, 0, 0}
};

PyMODINIT_FUNC initcppplug(void)
{
	PyObject *m = NULL;
    m = Py_InitModule3("cppplug", 
		SpamMethods,
		"cppplug");
	if (m == NULL)
        return;
	CPNewPyObjectClass(m, "BaseData", BaseData_Type);
	CPNewPyObjectClass(m, "Iter", Iter_Type);
	CPNewPyObjectClass(m, "Double3", Double3_Type);
	CPNewPyObjectClass(m, "Matrix", Matrix_Type);
	// PyImport_Import();
}