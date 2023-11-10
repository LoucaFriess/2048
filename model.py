import random

TAILLE = 4

class Jeu2048:
    def __init__(self):
        self.plateau = [0 for _ in range(TAILLE**2)]

    def __repr__(self):
        s  = "-"*23 + "\n"
        for y in range(TAILLE):
            s += "| "
            for x in range(TAILLE):
                n = self.plateau[y*TAILLE+x]
                if n != 0: c = str(n) 
                else: c = "."
                s += f"{c :<5}"
            s += "|\n|" 
            s += " "*21 + "|\n"
        s += "-"*23 + "\n"
        return s
    
    
    

    def droite(self):
        tableau = self.plateau.copy()
        for y in range( 4):
            c = 0
            fusionne = False
            # if tableau[y*TAILLE+3] == 0:
            #         c += 1            
            for x in range(3,-1,-1):
                i = y*TAILLE+x
                if tableau[i] == 0:
                    c += 1
                    continue
                if  x+c != 3 and tableau[i] == tableau[i+c+1] and not fusionne :
                    # print("merging")
                    fusionne = True
                    tableau[i+c+1] *=2
                    tableau[i] = 0

                    c+= 1
                elif c!= 0:
                    fusionne = False
                    # print(f"moving to {y},{x+c}")
                    tableau[i+c] = tableau[i]
                    tableau[i] = 0
                # print(self)
        return tableau

   
    def gauche(self):
        tableau = self.plateau.copy()
        for y in range(4):
            c = 0
            fusionne = False
            # if tableau[y*TAILLE+3] == 0:
            #         c += 1            
            for x in range(4):
                i = y*TAILLE+x
                if tableau[i] == 0:
                    c -= 1
                    continue
                if  x+c != 0 and tableau[i] == tableau[i+c-1] and not fusionne :
                    # print("merging")
                    fusionne = True
                    tableau[i+c-1] *=2
                    tableau[i] = 0

                    c-= 1
                elif c!= 0:
                    fusionne = False
                    # print(f"moving to {y},{x+c}")
                    tableau[i+c] = tableau[i]
                    tableau[i] = 0
                # print(self)
        return tableau


    def haut(self):
        tableau = self.plateau.copy()

        for x in range(4):
            c = 0
            fusionne = False
            # if tableau[y*TAILLE+3] == 0:
            #         c += 1            
            for y in range(4):
                i = y*TAILLE+x
                if tableau[i] == 0:
                    c -= 1
                    continue
                if  y+c != 0 and tableau[i] == tableau[i+TAILLE*(c-1)] and not fusionne :
                    # print("merging")
                    fusionne = True
                    tableau[i+TAILLE*(c-1)] *=2
                    tableau[i] = 0

                    c-= 1
                elif c!= 0:
                    fusionne = False
                    # print(f"moving to {y},{x+c}")
                    tableau[i+TAILLE*c] = tableau[i]
                    tableau[i] = 0
                # print(self)
        return tableau



    def bas(self):
        tableau = self.plateau.copy()
        for x in range(4):
            c = 0
            fusionne = False
            # if tableau[y*TAILLE+3] == 0:
            #         c += 1            
            for y in range(3, -1, -1):
                i = y*TAILLE+x
                if tableau[i] == 0:
                    c += 1
                    continue
                if  c+y != 3 and tableau[i] == tableau[i+TAILLE*(c+1)] and not fusionne :
                    # print("merging")
                    fusionne = True
                    tableau[i+TAILLE*(c+1)] *=2
                    tableau[i] = 0

                    c+= 1
                elif c!= 0:
                    fusionne = False
                    # print(f"moving to {y},{x+c}")
                    tableau[i+TAILLE*c] = tableau[i]
                    tableau[i] = 0
                # print(self)
        return tableau

   

    def cases_vides(self)-> 'list[int]':
        cases = []
        for i, n in enumerate(self.plateau):
            if n == 0:
                cases.append(i)

        return cases


    def nouveau_nombre(self) -> bool:
        vides = self.cases_vides()
        if vides == []:
            return True
        self.plateau[random.choice(vides)] = random.choice([2, 4])
        return False

    

if __name__ == "__main__":
        jeu = Jeu2048()
        jeu.nouveau_nombre()

        while True:
       

            print(jeu)
            d = input()
            if d == "z":
                tableau = jeu.haut()
            elif d == "q":
                tableau = jeu.gauche()
            elif d == "s":
               tableau = jeu.bas()
            elif d == "d":
                tableau = jeu.droite()
            else:
                continue

            if tableau == jeu.plateau:
                continue
            jeu.plateau = tableau

            if jeu.nouveau_nombre():
                break
