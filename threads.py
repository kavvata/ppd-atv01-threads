import threading
import random as rd
import time


def conta_tempo(nome):
    print(f"iniciando thread {nome}...")

    tempo = int(rd.random() * 10)

    for i in range(tempo):
        if i == tempo - 1:
            print(f"{nome}: {i + 1}")
        else:
            print(f"{nome}: {i + 1}...")

        time.sleep(1)

    print(f"... finalizando thread {nome}")


thread_unica = threading.Thread(target=conta_tempo, args=("unica",))
thread_unica.run()


print("Implementacao com 10 threads:")
threads = []

for i in range(10):
    threads.append(threading.Thread(target=conta_tempo, args=(i,)))

for t in threads:
    t.start()

for t in threads:
    t.join()


class MinhaThread:
    threads = []

    def criarThreads(self, quantidade):
        for i in range(quantidade):
            self.threads.append(threading.Thread(target=conta_tempo, args=(i,)))

    def iniciar(self):
        for t in self.threads:
            t.start()

        for t in self.threads:
            t.join()


print("Implementacao com classe:")
minha_thread = MinhaThread()
minha_thread.criarThreads(10)
minha_thread.iniciar()
