
import multiprocessing

def get_numbers(n, queue):                                                                  #Hier in dieser Methode werden die Zahlen
    for i in range(n):
        queue.put(i)                                                                         #Hier werden die Zahlen an die queue übertragen
    # time.sleep(n)

def read_data(n, queue):
    while not queue.empty():                                                                #Solange sich date in der queue befinden sollen die daten in eine Variable gespeichert werden
        number = queue.get()                                    
        queue.put(number)
        #print(number)                                                                      #Debug code

def calulcate_average_and_sum(n, queue):
    sum = 0
    average = 0
    while not queue.empty():                                                                #Daten werden aus einer queue entnommen und berechnet und erneut in eine queue gesteckt
        sum += queue.get()
    average = sum / n
    queue.put(sum)
    queue.put(average)

def print_results(n, queue):                                                                #Daten werden aus einer Queue entnommen und auf die Konsole gezeigt
    sum = queue.get()
    average = queue.get()
    print("Total numbers:", n)
    print("Sum of them:", sum)
    print("Average of them:", average)

if __name__ == "__main__":
    n = 100
    pool = multiprocessing.Pool(processes=4)                                                #Anzahl der Prozesse und die Threads
    m = multiprocessing.Manager()                                                           #Wird für das Multitasking der queues und prozessen verwendet
    queue = m.Queue()                                                                       #Erstellung einer queue
    process_1 = multiprocessing.Process(target=get_numbers, args=(n, queue))                #Erstellung eines prozessen und verknüpfung zu einer queue und Funktion
    process_2 = multiprocessing.Process(target=read_data, args=(n, queue))
    process_3 = multiprocessing.Process(target=calulcate_average_and_sum, args=(n, queue))
    process_4 = multiprocessing.Process(target=print_results, args=(n, queue))
    
    
    process_1.start()                                                                       #Ausführung von prozessen 
    process_2.start()
    process_3.start()
    
    process_1.join()                                                                        #Synchro und beendigung
    process_2.join()
    process_3.join()   
    process_4.start()                                                                       #Start
    process_4.join()
    
