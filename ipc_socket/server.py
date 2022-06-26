from multiprocessing.connection import Listener
import multiprocessing
import numpy as np

def get_numbers(shared_array):                                      #Zahlen Generieren
    for i in range(1024):
        shared_array[i] = i


def read_data(shared_array):                                        #Zahlen auslesen und in Sharedmemory speichern
    print(shared_array)


def calulcate_average_and_sum(shared_array, avg, summation):        #Lesen Berechnen und Schreiben von Daten
    arr = np.array(shared_array)

    sum = np.sum(np.array(shared_array))
    average = sum / len(arr)
    avg.value = average
    summation.value = sum


def print_results(shared, average, sum):                            #Lesen und ausgabe in der Konsole
    n = len(shared)
    print("Total numbers:", n)
    print("Sum of them:", sum.value)
    print("Average of them:", average.value)


def start():                                                        #Name der funktion
    shared = multiprocessing.Array('d', 1024)                       #erstellen von Speicher

    average = multiprocessing.Value('f')
    sum = multiprocessing.Value('f')

    process_1 = multiprocessing.Process(target=get_numbers, args=(shared,))
    process_2 = multiprocessing.Process(target=read_data, args=(shared,))
    process_3 = multiprocessing.Process(
        target=calulcate_average_and_sum, args=(shared, average, sum))
    process_4 = multiprocessing.Process(
        target=print_results, args=(shared, average, sum))

    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    process_3.start()
    process_3.join()
    process_4.start()
    process_4.join()


if __name__ == "__main__":                                          #Aufbau vom Socket 
    address = ('localhost', 301)                                    #Gibt an wo sich lokal der socket befindet
    listener = Listener(address, authkey=b'secret password')        #
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    while True:
        msg = conn.recv()
        if msg == "start":
            start()
        if msg == 'close':
            conn.close()
            break
    listener.close()







