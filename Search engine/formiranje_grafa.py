#ucitavanje
import os
from graph import Graph
from parser import Parser
from quicksort import quick_sort
from trie import Trie



# Funkcija za obilazak stabla direktorijuma pocevsi od datog korena


def search_node(path, rec):
    pass

def prolazak_kroz_direktorijume(cvor):
    graf = Graph(True)
    parser = Parser()
    cvorovi = {}
    tries = {}

    for koren, dirs, fajlovi in os.walk(cvor):
        for fajl in fajlovi:
            if fajl.endswith(".html"):
                putanja=os.path.join(koren, fajl)
                cvorovi[putanja] = graf.insert_vertex(putanja)
            else:
                continue

    for koren, dirs, fajlovi in os.walk(cvor):
        for fajl in fajlovi:

            if fajl.endswith(".html"):     #isprintaj sve html fajlove
                print(fajl)
                putanja = os.path.join(koren, fajl)     #putanja od korenaa do fajla
                linkovi, reci = parser.parse(putanja)   #parser na osnovu nje izdeli svaki fajl na linkove i reci

                for link in linkovi:  # zastita ako link nije dobar>>>>>>> treba dodati !!
                    if link not in cvorovi:
                        continue
                    edge = graf.get_edge(cvorovi[putanja], cvorovi[link])
                    if edge is None:
                        graf.insert_edge(cvorovi[putanja], cvorovi[link], 1)
                    else:
                        edge._element += 1
                trie = Trie()

                for rec in reci:       
                    trie.insert(rec)     #svaki fajl ima svoj trie u kom su izlistane sve reci tog fajla
                tries[putanja] = trie


    #print(graf.vertex_count())
    #print(graf.edge_count())
    return cvorovi, tries, graf

def trazenje_reci_sa_izbacivanjem(cvorovi, tries, graf, rec):       #izbacuju se linkovi u koima nije pronadjena rec
    number_of_words = {}


    for fajl in cvorovi.keys():
        fajl_trie = tries[fajl]
        node = fajl_trie.search_node(rec)
        number_of_words[fajl] = [] 
        if node is not None:
            broj_reci = node.counter
            if broj_reci == 0:
                del number_of_words[fajl]
                continue
            #print(broj_reci)    #printa broj reci koju pretrazujemo u svakom fajlu-dokumentu
            number_of_words[fajl].append(broj_reci)
        else:
            del number_of_words[fajl]       #ako nema reci u pretrazi-----> ne izvrsava ovaj kod, nastavlja se samo, brise se deo kljuc-vrednost
            continue
            #print("nema rezultata")    



        edges = list(graf.incident_edges(cvorovi[fajl], False))
        links_number = len(edges)
        number_of_words[fajl].append(links_number)


       #broj reci unutar svakog od linka koji pokazuje na dokument

        number_of_words[fajl].append(0)
        for edge in edges:
            incoming_file_trie = tries[edge._origin._element]   #fajl
            nodeDva = incoming_file_trie.search_node(rec)
            if nodeDva is not None:
                broj_reci_u_linku = nodeDva.counter
                number_of_words[fajl][2] += broj_reci_u_linku

    #pretraga stringa od jedne reci- i njegovo rangiranje (python)

        number_of_words[fajl] = 2.2 * number_of_words[fajl][0] + 1.2 * number_of_words[fajl][1] + 0.4 * number_of_words[fajl][2]
    return number_of_words

def trazenje_reci(cvorovi, tries, graf, rec):
    number_of_words = {}


    for fajl in cvorovi.keys():
        fajl_trie = tries[fajl]
        node = fajl_trie.search_node(rec)
        number_of_words[fajl] = [] 
        if node is not None:
            broj_reci = node.counter
            #print(broj_reci)    #printa broj reci koju pretrazujemo u svakom fajlu-dokumentu
            number_of_words[fajl].append(broj_reci)
        else:
            number_of_words[fajl].append(0)   



        edges = list(graf.incident_edges(cvorovi[fajl], False))
        links_number = len(edges)
        number_of_words[fajl].append(links_number)


       #broj reci unutar svakog od linka koji pokazuje na dokument

        number_of_words[fajl].append(0)
        for edge in edges:
            incoming_file_trie = tries[edge._origin._element]   #fajl
            second_node = incoming_file_trie.search_node(rec)
            if second_node is not None:
                broj_reci_u_linku = second_node.counter
                number_of_words[fajl][2] += broj_reci_u_linku

    #pretraga stringa od jedne reci- i njegovo rangiranje (python)

        number_of_words[fajl] = 2 * number_of_words[fajl][0] + 1 * number_of_words[fajl][1] + 0.3 * number_of_words[fajl][2]
    return number_of_words

def sortiranje(number_of_words):
    lista = lista_kljuc_vrednost(number_of_words)

    quick_sort(lista, 0, len(lista) - 1)
    #sort_number_of_words = sorted(number_of_words.items(), key=lambda x: x[1], reverse=True)
    return lista

    #for fajl in sort_number_of_words:
        #print(fajl[0] + " " + str(fajl[1]))


def lista_kljuc_vrednost(number_of_words):
    lista=[]
    for key in number_of_words:
        lista.append([key, number_of_words[key]])
    return lista

#pretraga stringa od vise reci bez log operanda (python programming language)
#1. SPLITUJEMO UNOS
#2. POZOVEMO FUNKCIJU ZA PRETRAGU RECI
#3. RANGIRAMO?


#pretraga stringa od vise reci- sa logickim operandima (AND OR NOT)


#def logicki_operatori():
    #pass


