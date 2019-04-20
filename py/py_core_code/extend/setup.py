from distutils.core import setup, Extension

#setup(name='Extendtest', ext_modules=[Extension('_Extendtest', sources=['Extendtest.c'])])


#swig   swig -python Extendtest.i
setup(name='Extendtest', ext_modules=[Extension('_Extendtest', sources=['Extendtest_wrap.c','Extendtest.c'])], py_modules=['Extendtest'])


#python setup.py install

