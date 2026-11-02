from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        lista_strumenti_2 = []
        cnx=get_connection()
        if cnx is not None:
            cursor=cnx.cursor()
            query='SELECT * FROM STRUMENTO'
            cursor.execute(query)

            for riga in cursor:
                # Creiamo l'oggetto Strumento con i campi del database
                s = Strumento(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
                lista_strumenti_2.append(s)
            cursor.close()
            cnx.close()

        return lista_strumenti_2



    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        lista_strumenti_ricerca = []
        tutti = self.get_strumenti()
        if tutti is not None:
            for s in tutti:
                if s.tipo.lower() == tipo.lower():
                    lista_strumenti_ricerca.append(s)

        return lista_strumenti_ricerca