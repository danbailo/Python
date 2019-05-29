# def foo():
#     raise AssertionError("Batata") 

def foo(x):
    assert (x<10),'assert error, entro aq'

def foo2():
    raise TimeoutError("timeout porra")


try:
    foo(11)
    foo2()
except RuntimeError as e:
    print("deu erro runtime:",e)
except AssertionError as e:
    print("assert erro ",e)
except TimeoutError as e:
    print("deu erro timeout ",e)
except Exception as e:
    print("deu erro padrao:",e)
else:
    print("deu certo")