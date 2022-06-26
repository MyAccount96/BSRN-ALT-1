
import multiprocessing
import numpy as np                                                                                          #Library für Arrays

def get_numbers(shared_array):                                                                              #Zahlen Generieren
    for i in range(1024):
        shared_array[i] = i

def read_data(shared_array):                                                                                #Daten aus Shared-Mem lesen
    print(shared_array)

def calulcate_average_and_sum(shared_array, avg, summation):                                                # Daten aus Shared-Mem Lesen/Berechnen/schreiben
    arr = np.array(shared_array)
    
    sum =  np.sum(np.array(shared_array))
    average = sum / len(arr)
    avg.value = average
    summation.value = sum

def print_results(shared,average, sum):                                                                     #Daten in Konsole ausgebene
    n = len(shared)
    print("Total numbers:", n)
    print("Sum of them:", sum.value)
    print("Average of them:", average.value)

if __name__ == "__main__":                                                                                  # Erstellen von einem Shared Memory Array
    shared = multiprocessing.Array('d', 1024)
    
    average = multiprocessing.Value('f')                                                                    # Erstellen von Shared Memory Variablen
    sum = multiprocessing.Value('f')
    
    process_1 = multiprocessing.Process(target=get_numbers, args=(shared,))                                 #Erstellen von Prozessen mit dem Shared Memory
    process_2 = multiprocessing.Process(target=read_data, args=(shared,))
    process_3 = multiprocessing.Process(target=calulcate_average_and_sum, args=(shared, average, sum))
    process_4 = multiprocessing.Process(target=print_results, args=(shared, average, sum))
    
    process_1.start()                                                                                       #Starten ,Snychro und beenden der Prozesse
    process_2.start()
    process_1.join()
    process_2.join()
    process_3.start()
    process_3.join()
    process_4.start()
    process_4.join()
    
