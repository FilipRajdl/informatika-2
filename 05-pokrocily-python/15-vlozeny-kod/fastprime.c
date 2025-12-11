#include <Python.h>

/*
 * Logika v jazyce C (Výpočetně náročná část)
 * Zjišťuje, zda je číslo n prvočíslo.
 */
int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

/*
 * Najde k-té prvočíslo.
 */
int kthPrime(int k) {
    int candidate = 2;
    int count = 0;
    while (count < k) {
        if (isPrime(candidate)) {
            count++;
        }
        if (count < k) candidate++;
    }
    return candidate;
}

/*
 * Wrapper funkce pro Python.
 * Převede Python argumenty na C typy, zavolá C funkci a výsledek převede zpět.
 */
static PyObject* py_kthPrime(PyObject* self, PyObject* args)
{
    int n;
    // Parsování argumentů: "i" znamená integer
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL; // Chyba při parsování
    }
    
    // Volání C funkce
    int result = kthPrime(n);
    
    // Převedení C int zpět na Python int
    return Py_BuildValue("i", result);
}

/*
 * Definice metod modulu.
 * Mapuje názvy funkcí v Pythonu na C funkce.
 */
static PyMethodDef FastPrimeMethods[] = {
    // {název_v_pythonu, C_funkce, typ_argumentů, dokumentace}
    {"kth_prime", (PyCFunction)py_kthPrime, METH_VARARGS, "Vypočítá k-té prvočíslo."},
    {NULL, NULL, 0, NULL} // Sentinel (ukončení pole)
};

/*
 * Definice struktury modulu.
 */
static struct PyModuleDef fastprimemodule = {
    PyModuleDef_HEAD_INIT,
    "fastprime",   /* název modulu */
    "Modul pro rychlý výpočet prvočísel v C.", /* dokumentace */
    -1,       /* velikost stavu per-interpreter (-1 = globální stav) */
    FastPrimeMethods
};

/*
 * Inicializační funkce modulu.
 * Volá se, když v Pythonu napíšete 'import fastprime'.
 */
PyMODINIT_FUNC PyInit_fastprime(void)
{
    return PyModule_Create(&fastprimemodule);
}