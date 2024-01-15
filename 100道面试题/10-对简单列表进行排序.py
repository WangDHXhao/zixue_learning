lista = [20, 40, 30, 50, 10]
# lista.sort()                  ###这种方法的lista本身是被改变了的


listb = sorted(lista, reverse=True)   # 默认升序
print(f"lista is {lista}")
print(f"listb is {listb}")  
