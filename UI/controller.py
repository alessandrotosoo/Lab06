import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def funzione_tasto_mostra_sezione_3(self, e):
        self._view.lista_strumenti.controls.clear()
        strumenti = self._model.get_strumenti()
        if strumenti:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))
        self._view.update()

    def funzione_tasto_cerca_sezione_4(self, e):
        tipo_cercato = self._view.input_tipo_strumento.value
        if not tipo_cercato:
            self._view.show_alert("Inserisci un tipo di strumento!")
            return

        self._view.lista_strumenti_ricerca.controls.clear()
        risultati = self._model.cerca_strumenti_per_tipo(tipo_cercato)
        if risultati:
            for s in risultati:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))
        else:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text("Nessuno strumento trovato."))

        self._view.update()