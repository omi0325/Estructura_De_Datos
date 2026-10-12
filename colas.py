from collections import deque
import time
cola= deque()
cola.append("mango")
cola.append("platano")
cola.append("sandia")
cola.append("fresa")
print(list(cola))
atendido=cola.popleft()
time.sleep(2)
print("La siguiente en atender: ",cola[0])
print(list(cola))
