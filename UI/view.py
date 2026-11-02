import flet as ft
from flet import TextField, MainAxisAlignment
from UI.alert import AlertManager

'''
    VIEW:
- Rappresenta l'interfaccia utente

- Riceve i dati dal MODELLO e li presenta senza modificarli

'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI
        self.page.scroll = 'auto'

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di strumenti aggiornata
        self.lista_strumenti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca strumento per tipo
        self.input_tipo_strumento = ft.TextField(label="Tipo")

        # ListView per mostrare il risultato della ricerca strumenti per tipo
        self.lista_strumenti_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        # TODO
        self.testo_Strumenti_sezione_3 = ft.Text('Strumenti', size=20)
        self.bottone_mostra_sezione_3 = ft.Button(
            'Mostra',
            on_click=self.controller.funzione_tasto_mostra_sezione_3
        )
        self.riga_sezione_3 = ft.Row(
            controls=[self.testo_Strumenti_sezione_3, self.bottone_mostra_sezione_3],
            alignment=ft.MainAxisAlignment.START
        )
        self.seconda_riga_sezione_3 = ft.Container(content=self.lista_strumenti, height=120)

        self.testo_cerca_strumento_per_tipo_sezione_4 = ft.Text('Cerca Strumenti per Tipo', size=20)
        self.prima_riga_sezione_4 = ft.Row(
            spacing=200,
            controls=[self.testo_cerca_strumento_per_tipo_sezione_4],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.bottone_cerca_sezione_4 = ft.Button(
            'Cerca',
            on_click=self.controller.funzione_tasto_cerca_sezione_4
        )
        self.seconda_riga_sezione_4 = ft.Row(
            controls=[self.input_tipo_strumento, self.bottone_cerca_sezione_4],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.terza_riga_sezione_4 = ft.Container(content=self.lista_strumenti_ricerca, height=120)

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            # TODO
            self.riga_sezione_3,
            self.seconda_riga_sezione_3,
            ft.Divider(),

            # Sezione 4
            # TODO
            self.prima_riga_sezione_4,
            self.seconda_riga_sezione_4,
            self.terza_riga_sezione_4
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()