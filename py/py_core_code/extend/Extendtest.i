%module Extendtest

%{
#define SWIG_FILE_WITH_INIT
#include "Extendtest.h"
%}

int fac(int n);
char *reverse(char *s);
int test();