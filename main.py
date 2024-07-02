import customtkinter  # la bibliotheque de interface graphique


class IdentificationWindow:
    # __init__ c'est le constructeur d'une classe , elle est appelé directement ou automatiquement a chaque fois on
    # creer une instance
    def __init__(self, master):
        self.error_message = None  # on utilise self pour acceder aux attributes et methodes de la classe python
        self.equation = None
        self.entry = None
        self.master = master  # on as intialisé une variable master
        master.title("Calculator")

        self.frames = customtkinter.CTkFrame(master=master)  # pour creer un cadre dans la fenetre principale
        self.frames.pack(padx=12, pady=12, expand=True,
                         fill=customtkinter.BOTH)  # on as assigné true a expand (elargir) pour
        # que le cadre prendre tous l'espace
        # de la fenetre

        self.label = customtkinter.CTkLabel(master=self.frames, text="Se Connecter",
                                            font=customtkinter.CTkFont(family="Arial", size=30))
        self.label.pack(padx=12, pady=40)

        self.user_input = customtkinter.CTkEntry(master=self.frames, placeholder_text="nom d'utilisateur", width=300,
                                                 height=40)
        self.user_input.pack(padx=12, pady=12, )  # pour creer le champ d'utilisateur

        self.password_input = customtkinter.CTkEntry(master=self.frames, placeholder_text="Mot de passe", width=300,
                                                     height=40,
                                                     show="*")
        self.password_input.pack(padx=12, pady=12)  # pour creer le champ password

        self.button = customtkinter.CTkButton(master=self.frames, text="connecter", height=40, width=300,
                                              command=self.login)
        self.button.pack(padx=12, pady=12)  # pour ceer le button # master c'est le parent du button(savedire on a
        # creer l
        # le button a l interieur de cadre )

        self.frames2 = customtkinter.CTkFrame(master=master)

    def login(self):
        # cette method pour afficher la calculatrice quand l'utlisateur entre le bon nom d'utlisateur et le bon mot
        # de passe
        username = self.user_input.get()  # j'ai recuperé le nom d'utilisatur avec la method get
        password = self.password_input.get() #j'ai recupére le mot de passe

        # on as utiliser if statement pour verfier est ce que l'utilistaeur est egale a "admin" et le mot de passe
        if username == "admin" and password == "admin":
            # print("Login successful")
            self.frames.pack_forget() # elle vas detruire le premier cadre

            self.frames2.grid(row=2, column=10, padx=600, pady=150) # grid c'est une grille

            self.label = customtkinter.CTkLabel(master=self.frames2, text="Bienvenue",
                                                font=customtkinter.CTkFont(family="Arial", size=30))
            self.label.grid(row=0, column=12, padx=12, pady=40)

            self.equation = customtkinter.StringVar()
            self.entry = customtkinter.CTkEntry(master=self.frames2, width=500, height=100, textvariable=self.equation,
                                                font=customtkinter.CTkFont(family="Arial",
                                                                           size=20))
            self.entry.grid(padx=0, pady=0, row=0, column=0, columnspan=4)

            self.buttons()  # j'ai appelé la methode button() pour créer les buttons

        else:
            # j'ai ajouté if pour verfier que le message d'erreur n'est pas deja affiché , si il est affiche il faut l'effacer avant
            # d'executer la ligne suivante
            if self.error_message:
                self.error_message.destroy()  # j'ai créé cet if pour verfier est ce que le lable error message existe deja , si il existe il faut le detruire
                # pour ne pas céér des doublon
            self.error_message = customtkinter.CTkLabel(master=self.frames, text="l'utilisateur n'existe pas")
            self.error_message.pack(padx=50, pady=50)

    def buttons(self):
        # this method to create a buttons => cette methode utiliser pour creer les button de la calculatrice
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton("+")
        b_sub = self.addButton("-")
        b_mult = self.addButton("*")
        b_div = self.addButton("/")
        b_clear = self.addButton("c")
        b_equal = self.addButton("=")

        # on vas arranger les button dans des lignes

        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mult]
        row4 = [b_clear, b0, b_equal, b_div]

        # assiger pour chaque button

        r = 1 # represente une ligne dans un tableau
        for row in [row1, row2, row3, row4]:
            c = 0  # represente une column dans un tableau
            for b in row: #b represnte une cellule dans un tableau
                b.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def addButton(self, value):
        # une methode pour creer un seul button

        return customtkinter.CTkButton(master=self.frames2, text=value, width=120, height=50,
                                       font=customtkinter.CTkFont(family="Arial", size=20),
                                       command=lambda: self.buttonAction(value),
                                       ) # value c'est le text affiché a l'interieur de button

    #  cette methode pour ajouter des actions au button
    def buttonAction(self, value):
        current_equation = self.equation.get()  # recupere la valeur d'une eqution '
        if value == "c":
            self.equation.set("")
        elif value == "=":
            try:
                result = eval(current_equation)
                self.equation.set(str(result))
            except Exception as e:
                self.equation.set("Error")
        else:
            new_equation = current_equation + str(value)  # pour ajouter la valeur actuelle a lequation
            self.equation.set(new_equation)


# cette method est utiliser souvent comme un point d'entré d"un script , il vas commencer l"esxecution depuis cette ligne

if __name__ == "__main__":
    root = customtkinter.CTk()

    my_calculator = IdentificationWindow(master=root)

    root.mainloop()
