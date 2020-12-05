#!/usr/bin/pyntho3.7
import time
import sys
from multiprocessing import Process

animation = "|/-\\"
def anime():
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        #print("END")


def msg_anime():
    print("Teste TESTE TESTE TESTE")

func_1=Process(target=anime)
func_1.start()
func_2=Process(target=msg_anime)
func_2.start()



