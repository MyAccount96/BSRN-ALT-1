from multiprocessing.connection import Client

if __name__ == "__main__":
    address = ('localhost', 301)                        #Addresse für den Server
    conn = Client(address, authkey=b'secret password')  #Die verbindung zum Server incl. einem "Passwort"
    conn.send("start")                                  #Der CLient befehlt der den Starten und dann Schliessen soll
    conn.send('close')                                  
    conn.close()                                        #Die verbindung trennen
