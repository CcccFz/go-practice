from nose.tools import with_setup

def setUp():
    print("function setup")

def tearDown():
    print("function teardown")
    

def func1Start():
    print("func1 start") 

def func1End():
    print("func1 end") 

def func2Start():
    print("func2 start") 
 
def func2End():
    print("func2 end") 


@with_setup(func1Start, func1End)
def Testfunc1():
    print("Testfunc1") 
    assert True

@with_setup(func2Start, func2End)
def Testfunc2():
    print("Testfunc2") 
    assert True
	