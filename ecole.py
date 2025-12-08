#TODO : faire un programme qui permet à un enseingant
#TODO : d'entrer des noms d'élèves, des matière et des notes
#TODO : et enregister les bulletins dans un ou des fichiers
#TODO : on doit avoir plusieurs notes par étudiant par matière

"""
exemple :
bulletin = {
    "élève" : ["Alice", "Bob", "Chloé"],
    "français" : [[95, 100, 90], [80, 70, 75], [50, 60, 65],
    "math" : [[95, 100, 90], [80, 70, 75], [50, 60, 65]
}
pseudocode :
bulletin = {
     "élève" : []
}
while true
    nom = quel élève?
    bulletin[eleve].append(nom)
    while true
        matiere = quelle matière?
        créer une clé matière dans le bulletin avec une liste vide imbriquée
        while true
            note = quelle note?
            ajouter la note dans la liste imbriquée
        conditions d'arrêts...
sauvegarder le bulletin dans un fichier
"""
bulletin = {
     "eleve" : []
}
nb_eleves = 0
while True:
    nom = input("Quel élève? ")
    if nom == "":
        break
    bulletin["eleve"].append(nom)
    while True:
        matiere = input("Quelle matière? ")
        if matiere == "":
            break
        if not matiere in bulletin:
            bulletin[matiere] = []
        bulletin[matiere].append([]) # on veut juste ajouter une liste imbriquer dans la liste
        while True:
            note = input("Quelle note? ")
            if note == "":
                break
            bulletin[matiere][nb_eleves].append(int(note))
    nb_eleves += 1
print(bulletin)
with open("ecole/mon_bulletin.txt", "w") as f:
    for i in range(len(bulletin["eleve"])):
        f.write(bulletin["eleve"][i] + "\n")
        for k, v in bulletin.items():
            if k != "eleve":
                f.write(k + " : " + str(v[i]) + "\n")
        f.write("\n")
