import multiprocessing

def get_numbers(n, parent):                                             #Hier in dieser Methode werden die Zahlen generiert.
    for i in range(n):
        parent.send(i)                                                  #Hier werden die Zahlen an die Pipe Weiter geleitet
    parent.close()                                                      #Hier wird die Pipe geschlossen

def read_data(end_n, con, parent):                                      #In dieser Methode werden die Daten aus einer Pipe ausgelesen  
    while True:                     
        n = con.recv()                                                  # Hier werden erhaltenen Daten als Variable gespeichert
        parent.send(n)                                                  # Es erneut eine Pipe genutzt um weitere Datenübertragungen zu erstellen
        if n == end_n:              
            break

def calulcate_average_and_sum(end_n, child, parent):                    #Diese Methode berechnet durschnittswert und anzahl der Daten
    sum = 0
    average = 0
    while True: 
        n = child.recv()                                                # Hier werden die Daten ausgelesen aus der Pipe
        sum += n
        if n == end_n:
            break
    average = sum / n
    parent.send(sum)                                                    # Hier wird die Summe versendet.
    parent.send(average)                                                # Hier wird der durschnitt weiter verschickt.
    # parent.close()

def print_results(n, child):                                            # Diese Funktion wird zum Schluss aufgerufen um alles in der Konsole anzuzeigen
    sum = child.recv()                                                  # Hier wird zu erst die Summe ausgelesen und dann der Durschschnitt
    average = child.recv()                      
    print("Total numbers:", n)
    print("Sum of them:", sum)
    print("Average of them:", average)

if __name__ == "__main__":
    parent, child = multiprocessing.Pipe()                                                              # Hier wird eine Pipe erstellt Parent wird zum schreiben und Child zum lesen genutzt
    n = 100                                                                                             # Dies ist ein Übergabe Parameter für das erstellen von Zahlen
    process_1 = multiprocessing.Process(target=get_numbers, args=(105, parent))                         # Hier wird der erste Prozess erstellt der mit einer pipe die daten überträgt
    process_2 = multiprocessing.Process(target=read_data, args=(104, child, parent))                    # Hier wird der zweite Prozess erstellt und mit einer Pipe werden die Daten gelesen 

    process_3 = multiprocessing.Process(target=calulcate_average_and_sum, args=(104, child, parent))    # Hier wird der Dritte Prozess erstellt und mit einer Pipe werden die Daten gelesen 
    process_4 = multiprocessing.Process(target=print_results, args=(105, child))                        # Hier wird der vierte Prozess erstellt und mit einer Pipe werden die Daten gelesen
    
    process_1.start()                                                                                  #Hier werden die Prozesse gestartet
    process_2.start()
    process_3.start()
    process_4.start()
    

    process_1.join()                                                                                   #Hier werden die Prozesse synchronisiert und geschlossen
    process_2.join()
    process_3.join()
    process_4.join()
    
    parent.close()                                                                                      #Hier werden Pipes geschlossen
    child.close()




