import tkinter 

class Graphique():
    def __init__(self) -> None:

        self.couleurs = {2:"white", 4:"grey87", 8:"coral", 16:"coral1", 32:"IndianRed1",
                        64: "firebrick3", 128: "LightGoldenrod1", 256: "goldenrod1", 512: "", 
                        1024: "", 2048: "chocolate1" }

        # on cré le canvas
        self.fenetre = tkinter.Tk()
        self.fenetre.title("2048")
        # empêche que l'on puisse redimensionner la fenêtre
        self.fenetre.resizable(0, 0)
        # fait passer la fenêtre à l'avant plan
        self.fenetre.wm_attributes("-topmost", 1)
        self.canvas = tkinter.Canvas(self.fenetre, height = 850, width = 850, bg="white")
        self.canvas.pack()


    def grille(self):
        """crée la grille"""
        self.canvas.create_rectangle(100, 100, 700, 700, fill = 'grey66', outline="")

        x1 = 120
        y1 = 120
        x2 = 237
        y2 = 237

        self.rectangles = {}
        count = 0
        for colonne in range(4):
            for ligne in range(4):
                x10 = x1 + 147 * ligne
                y10 = y1 + 147*colonne
                x20 = x2+ 147* ligne
                y20 = y2 + 147*colonne

                rectangle = self.canvas.create_rectangle(x10,y10 ,x20 ,y20 , fill = 'grey91', outline="")
                self.rectangles[count] = {'id': rectangle, 
                                          "x1": x10, 'x2': x20, 
                                          'y1': y10, 'y2': y20, 
                                          "x_milieu": (x10+x20)/2, "y_milieu": (y10+y20)/2,
                                          "chiffre": None}
                
                count += 1


    def affiche_plateau(self, plateau):
        for id, elt in enumerate(plateau):
            if elt != 0:
                self.canvas.itemconfigure(self.rectangles[id]['id'], fill=self.couleurs[elt])
                self.canvas.create_text(self.rectangles[id]["x_milieu"], 
                                        self.rectangles[id]["y_milieu"], 
                                        text = elt,
                                        font = ("Arial", 30))


    def get_mouvement(self):
        return self.deplacement

    def bas(self):
        self.fenetre.quit()
        print(1)
        self.deplacement = 'b'
        

    def mouvements(self):
        self.canvas.bind_all("<Down>", self.bas())
        self.fenetre.mainloop()


if __name__ == "__main__":
    a = Graphique()
    a.grille()
    a.affiche_plateau([2, 8, 16, 0, 0, 2048])
    a.mouvements()