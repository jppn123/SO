import time
from fila import Queue

st_time = time.time()

data = [("a", 227), ("b", 234), ("c", 33), ("d", 107), ("e",473), ("f", 203), ("g",268),("h", 234), ("i",51), ("j", 190)]
qt = [20, 40, 80]
processos = Queue()

processos.printQueue()

p_len = processos.len()

for quantum in qt:
    print(f"Comportamento do round robin para o quantum {quantum}")
    for p in data:
        processos.push(p)
    while processos.len() != 0:
        valor = processos.remove()
        pName, pTime = valor
        pTime -= quantum
        if pTime > 0:
            processos.push((pName, pTime))
        if processos.len() != 1:
            if pTime > 0:
                time.sleep(pTime/1000)
            else:
                time.sleep(1/1000)
        
        processos.printQueue()
    
    print("\n\n\n")
