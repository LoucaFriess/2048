from model import Jeu2048;

from graphique import Graphique;

jeu = Jeu2048()
graphique = Graphique()
jeu.nouveau_nombre()

while True:
    

    graphique.affiche_plateau(jeu.plateau)
    graphique.mouvements()
    mouvements = graphique.get_mouvement()


    if mouvements == 'l':
        tableau = jeu.gauche()

    elif mouvements == 'r':
        tableau = jeu.droite()

    elif mouvements == 'u':
        tableau = jeu.haut()

    elif mouvements == 'd':
        tableau = jeu.bas()

    if jeu.plateau == tableau and jeu.cases_vides() != []:
        continue

    jeu.plateau = tableau
    if jeu.nouveau_nombre():
        won = False
        for i in jeu.plateau:
            if i == 2048:
                won = True
                break
        graphique.victory(won)

        break


