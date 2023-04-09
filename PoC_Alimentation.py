import random
from datetime import datetime

groupes_aliments = {
    "petit_dejeuner": {
        "cereales": ["avoine", "muesli", "pain", "céréales", "granola", "pain complet", "baguette", "brioche"],
        "produits_laitiers": ["lait", "yaourt", "fromage", "fromage blanc", "crème", "lait d'amande", "lait de soja", "lait de coco"],
        "fruits": ["pomme", "banane", "orange", "fraises", "kiwi", "raisins", "ananas", "mangue"],
    },
    "dejeuner": {
        "proteines": ["poulet", "boeuf", "tofu", "pois chiches", "porc", "agneau", "saucisse", "steak végétarien"],
        "legumes": ["brocoli", "carottes", "haricots verts", "salade", "tomates", "concombre", "pois", "asperges"],
        "feculents": ["riz", "pâtes", "quinoa", "pommes de terre", "semoule", "gnocchi", "riz complet", "blé"],
    },
    "diner": {
        "proteines": ["saumon", "dinde", "lentilles", "tempeh", "truite", "thon", "crevettes", "poissons blancs"],
        "legumes": ["épinards", "chou-fleur", "courgettes", "poivrons", "champignons", "oignons", "betteraves", "radis"],
        "feculents": ["couscous", "patates douces", "boulgour", "polenta", "maïs", "orge", "millet", "riz sauvage"],
    },
}

groupes_aliments_vegetarien = {
    "proteines": ["tofu", "tempeh", "lentilles", "pois chiches", "oeufs", "fromage", "yaourt", "quinoa", "noix", "graines", "lait", "protéines de pois"],
    "legumes": ["brocoli", "carottes", "haricots verts", "salade", "tomates", "concombre", "pois", "asperges", "champignons", "oignons", "betteraves", "radis"],
    "feculents": ["riz", "pâtes", "quinoa", "pommes de terre", "semoule", "gnocchi", "riz complet", "blé", "couscous", "patates douces", "boulgour", "polenta"],
}

groupes_aliments_vegan = {
    "proteines": ["tofu", "tempeh", "lentilles", "pois chiches", "seitan", "quinoa", "noix", "graines", "lait d'amande", "lait de soja", "lait de coco", "protéines de pois"],
    "legumes": ["brocoli", "carottes", "haricots verts", "salade", "tomates", "concombre", "pois", "asperges", "champignons", "oignons", "betteraves", "radis"],
    "feculents": ["riz", "pâtes", "quinoa", "pommes de terre", "semoule", "gnocchi", "riz complet", "blé", "couscous", "patates douces", "boulgour", "polenta"],
}

groupes_aliments_pauvre_glucides = {
    "proteines": ["poulet", "boeuf", "tofu", "pois chiches", "saumon", "dinde", "lentilles", "tempeh", "porc", "agneau", "truite", "thon", "crevettes", "poissons blancs", "oeufs", "fromage"],
    "legumes": ["brocoli", "carottes", "haricots verts", "salade", "épinards", "chou-fleur", "courgettes", "poivrons", "champignons", "oignons", "betteraves", "radis", "concombre", "tomates", "asperges", "pois"],
    "gras_sains": ["avocat", "huile d'olive", "noix", "graines de chia", "beurre de cacahuète", "huile de coco", "amandes", "graines de lin", "huile d'avocat", "huile de noix", "beurre d'amande", "noix de cajou"],
}

fruits_legumes_saisonniers = {
    "printemps": {
        "fruits": ["fraises", "cerises", "abricots", "pêches", "nectarines", "rhubarbe", "groseilles", "framboises", "amandes"],
        "legumes": ["asperges", "petits pois", "épinards", "radis", "artichauts", "laitue", "oignons nouveaux", "poireaux", "navets", "carottes", "chou-fleur", "fèves", "roquette", "cresson", "ail des ours"],
    },
    "ete": {
        "fruits": ["pêches", "nectarines", "melons", "framboises", "myrtilles", "abricots", "cerises", "mûres", "prunes", "raisins", "pastèques", "pommes", "poires", "figues", "groseilles", "cassis"],
        "legumes": ["tomates", "courgettes", "poivrons", "aubergines", "concombres", "haricots verts", "radis", "betteraves", "maïs", "carottes", "oïl des ours", "fenouil", "chou-rave", "salades", "épinards", "oseille", "patates douces"],
    },
    "automne": {
        "fruits": ["pommes", "poires", "raisins", "prunes", "coings", "noix", "noisettes", "amandes", "châtaignes", "mûres", "kakis", "figues", "grenades", "cynorhodons"],
        "legumes": ["chou", "potiron", "brocoli", "betteraves", "navets", "haricots verts", "panais", "poireaux", "champignons", "citrouille", "patates douces", "topinambours", "courges", "céleri-rave", "carottes", "radis", "épinards"],
    },
    "hiver": {
        "fruits": ["oranges", "clémentines", "kiwis", "pommes", "poires", "mandarines", "citrons", "bananes", "ananas", "grenades", "dattes", "noix", "noisettes", "pamplemousses", "avocats"],
        "legumes": ["choux de Bruxelles", "navets", "poireaux", "carottes", "endives", "choux", "choux-fleurs", "brocoli", "betteraves", "céleri", "épinards", "blettes", "scarole", "frisée", "mâche", "oignons", "ail", "pommes de terre"],
    },
}
collations = {
    "fruits": ["pomme", "banane", "orange", "fraises", "kiwi", "raisins", "ananas", "mangue"],
    "nuts_and_seeds": ["amandes", "noix", "noisettes", "graines de tournesol", "graines de citrouille", "pistaches"],
    "yogurts": ["yaourt nature", "yaourt aux fruits", "yaourt grec", "yaourt végétal"],
    "bars": ["barre de céréales", "barre de granola", "barre énergétique", "barre protéinée"],
}

boissons = {
    "eau": ["eau plate", "eau gazeuse"],
    "the_cafe": ["thé", "café", "tisane", "infusion"],
    "jus": ["jus d'orange", "jus de pomme", "jus de raisin", "jus de tomate", "jus d'ananas", "jus de mangue"],
    "boissons_vegetales": ["lait d'amande", "lait de soja", "lait de coco", "lait de riz"],
}


def determiner_saison(date):
    if date.month in [3, 4, 5]:
        return "printemps"
    elif date.month in [6, 7, 8]:
        return "ete"
    elif date.month in [9, 10, 11]:
        return "automne"
    else:
        return "hiver"

def generer_menus(nombre_de_jours, groupes_aliments, saison, vegetarien):
    menus = {"petit_dejeuner": [], "dejeuner": [], "diner": [], "collation": [], "boisson": []}
    
    for i in range(nombre_de_jours):
        petit_dejeuner = {
            "cereales": random.choice(groupes_aliments["petit_dejeuner"]["cereales"]),
            "produits_laitiers": random.choice(groupes_aliments["petit_dejeuner"]["produits_laitiers"]),
            "fruits": random.choice(fruits_legumes_saisonniers[saison]["fruits"])
        }
        menus["petit_dejeuner"].append(petit_dejeuner)

        if vegetarien:
            proteines_dejeuner = random.choice(groupes_aliments_vegetarien["proteines"])
            proteines_diner = random.choice(groupes_aliments_vegetarien["proteines"])
        else:
            proteines_dejeuner = random.choice(groupes_aliments["dejeuner"]["proteines"])
            proteines_diner = random.choice(groupes_aliments["diner"]["proteines"])
        
        dejeuner = {
            "proteines": proteines_dejeuner,
            "legumes": random.choice(fruits_legumes_saisonniers[saison]["legumes"]),
            "feculents": random.choice(groupes_aliments["dejeuner"]["feculents"])
        }
        menus["dejeuner"].append(dejeuner)
        
        diner = {
            "proteines": proteines_diner,
            "legumes": random.choice(fruits_legumes_saisonniers[saison]["legumes"]),
            "feculents": random.choice(groupes_aliments["diner"]["feculents"])
        }
        menus["diner"].append(diner)
        collation = {
            "fruits": random.choice(collations["fruits"]),
            "nuts_and_seeds": random.choice(collations["nuts_and_seeds"]),
            "yogurts": random.choice(collations["yogurts"]),
            "bars": random.choice(collations["bars"]),
        }
        menus["collation"].append(collation)

        boisson = {
            "eau": random.choice(boissons["eau"]),
            "the_cafe": random.choice(boissons["the_cafe"]),
            "jus": random.choice(boissons["jus"]),
            "boissons_vegetales": random.choice(boissons["boissons_vegetales"]),
        }
        menus["boisson"].append(boisson)
    
    return menus

""" aliments_exclus_str = input("Veuillez entrer les aliments à exclure, séparés par des virgules (ou appuyez sur Entrée pour ignorer) : ")
aliments_exclus = [aliment.strip() for aliment in aliments_exclus_str.split(",")] if aliments_exclus_str else []
def supprimer_aliments_exclus(groupes_aliments, aliments_exclus):
    for categorie, aliments in groupes_aliments.items():
        groupes_aliments[categorie] = [aliment for aliment in aliments if aliment not in aliments_exclus]

supprimer_aliments_exclus(groupes_aliments, aliments_exclus)
supprimer_aliments_exclus(groupes_aliments_vegetarien, aliments_exclus)
supprimer_aliments_exclus(groupes_aliments_vegan, aliments_exclus)
supprimer_aliments_exclus(groupes_aliments_pauvre_glucides, aliments_exclus)
supprimer_aliments_exclus(fruits_legumes_saisonniers, aliments_exclus)
supprimer_aliments_exclus(collations, aliments_exclus)
supprimer_aliments_exclus(boissons, aliments_exclus) """

date_str = input("Entrez la date (format : JJ/MM/AAAA) : ")
date = datetime.strptime(date_str, "%d/%m/%Y")
saison = determiner_saison(date)

vegetarien_str = input("Êtes-vous végétarien ? (oui/non) : ")
vegetarien = vegetarien_str.lower() == "oui"

# nombre_de_jours = 7
nombre_de_jours_str = input("Pour combien de jours souhaitez-vous générer des menus ? : ")
nombre_de_jours = int(nombre_de_jours_str)
menus = generer_menus(nombre_de_jours, groupes_aliments, saison, vegetarien)

for i in range(nombre_de_jours):
    print(f"Jour {i+1}:")
    print(f"Petit déjeuner: {menus['petit_dejeuner'][i]}")
    print(f"Déjeuner: {menus['dejeuner'][i]}")
    print(f"Collation: {menus['collation'][i]}")
    print(f"Dîner: {menus['diner'][i]}\n")
    print(f"Boisson: {menus['boisson'][i]}\n")
