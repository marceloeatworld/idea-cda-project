import random
from datetime import datetime
import math
from fpdf import FPDF

groupes_aliments = {
"petit_dejeuner": {
"cereales": [
{"avoine": {"calories": 389, "protéines": 16.9, "lipides": 6.9, "glucides": 66.3}},
{"muesli": {"calories": 340, "protéines": 10, "lipides": 7, "glucides": 60}},
{"pain": {"calories": 265, "protéines": 9, "lipides": 1.2, "glucides": 55}},
{"céréales": {"calories": 350, "protéines": 8, "lipides": 1, "glucides": 75}},
{"granola": {"calories": 471, "protéines": 9.4, "lipides": 20.3, "glucides": 64.2}},
{"pain complet": {"calories": 247, "protéines": 9.5, "lipides": 1.7, "glucides": 49}},
{"baguette": {"calories": 255, "protéines": 9, "lipides": 1, "glucides": 53}},
{"brioche": {"calories": 361, "protéines": 7.7, "lipides": 13.6, "glucides": 53}},
],
"produits_laitiers": [
{"lait": {"calories": 42, "protéines": 3.4, "lipides": 1, "glucides": 5}},
{"yaourt": {"calories": 59, "protéines": 3.6, "lipides": 3.3, "glucides": 4.7}},
{"fromage": {"calories": 350, "protéines": 25, "lipides": 27, "glucides": 1}},
{"fromage blanc": {"calories": 97, "protéines": 7.1, "lipides": 5, "glucides": 4}},
{"crème": {"calories": 345, "protéines": 1.1, "lipides": 37, "glucides": 2.6}},
{"lait d'amande": {"calories": 25, "protéines": 0.9, "lipides": 1.1, "glucides": 3}},
{"lait de soja": {"calories": 54, "protéines": 3.3, "lipides": 1.8, "glucides": 6}},
{"lait de coco": {"calories": 230, "protéines": 2.3, "lipides": 23, "glucides": 6}},
],
"fruits": [
{"pomme": {"calories": 52, "protéines": 0.3, "lipides": 0.2, "glucides": 13.8}},
{"banane": {"calories": 89, "protéines": 1.1, "lipides": 0.3, "glucides": 22.8}},
{"orange": {"calories": 47, "protéines": 0.9, "lipides": 0.1, "glucides": 11.8}},
{"fraises": {"calories": 32, "protéines": 0.7, "lipides": 0.3, "glucides": 7.7}},
{"kiwi": {"calories": 61, "protéines": 1.1, "lipides": 0.5, "glucides": 14.7}},
{"raisins": {"calories": 67, "protéines": 0.6, "lipides": 0.4, "glucides": 17.2}},
{"ananas": {"calories": 50, "protéines": 0.5, "lipides": 0.1, "glucides": 13.1}},
{"mangue": {"calories": 60, "protéines": 0.8, "lipides": 0.4, "glucides": 14.9}}
],
},
"dejeuner": {
"proteines": [
{"poulet": {"calories": 239, "protéines": 27, "lipides": 14, "glucides": 0}},
{"boeuf": {"calories": 250, "protéines": 26, "lipides": 17, "glucides": 0}},
{"tofu": {"calories": 76, "protéines": 8, "lipides": 4.8, "glucides": 1.9}},
{"pois chiches": {"calories": 164, "protéines": 8.9, "lipides": 2.6, "glucides": 27}},
{"porc": {"calories": 242, "protéines": 25, "lipides": 16, "glucides": 0}},
{"agneau": {"calories": 294, "protéines": 25, "lipides": 21, "glucides": 0}},
{"saucisse": {"calories": 310, "protéines": 12, "lipides": 28, "glucides": 1.6}},
{"dinde": {"calories": 189, "protéines": 29, "lipides": 7.5, "glucides": 0}},
],
"legumes": [
{"brocoli": {"calories": 34, "protéines": 2.8, "lipides": 0.4, "glucides": 6.6}},
{"carottes": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 9.6}},
{"haricots verts": {"calories": 31, "protéines": 1.8, "lipides": 0.2, "glucides": 7.0}},
{"salade": {"calories": 15, "protéines": 1.4, "lipides": 0.2, "glucides": 2.9}},
{"tomates": {"calories": 18, "protéines": 0.9, "lipides": 0.2, "glucides": 3.9}},
{"concombre": {"calories": 15, "protéines": 0.7, "lipides": 0.1, "glucides": 3.6}},
{"pois": {"calories": 81, "protéines": 5.4, "lipides": 0.4, "glucides": 14.5}},
{"asperges": {"calories": 20, "protéines": 2.2, "lipides": 0.2, "glucides": 3.9}}
],
"feculents": [
{"riz": {"calories": 130, "protéines": 2.7, "lipides": 0.3, "glucides": 28}},
{"pâtes": {"calories": 131, "protéines": 5.2, "lipides": 0.8, "glucides": 25}},
{"quinoa": {"calories": 120, "protéines": 4.4, "lipides": 1.9, "glucides": 21}},
{"pommes de terre": {"calories": 77, "protéines": 2, "lipides": 0.1, "glucides": 17}},
{"semoule": {"calories": 360, "protéines": 12, "lipides": 1, "glucides": 72}},
{"gnocchi": {"calories": 165, "protéines": 4.1, "lipides": 0.5, "glucides": 33}},
{"riz complet": {"calories": 111, "protéines": 2.6, "lipides": 0.9, "glucides": 23}},
{"blé": {"calories": 327, "protéines": 12.6, "lipides": 1.5, "glucides": 71}}
],
},
"diner": {
"proteines": [
{"saumon": {"calories": 208, "protéines": 20, "lipides": 13, "glucides": 0}},
{"dinde": {"calories": 104, "protéines": 22, "lipides": 1, "glucides": 0}},
{"lentilles": {"calories": 116, "protéines": 9, "lipides": 0.4, "glucides": 20}},
{"tempeh": {"calories": 193, "protéines": 20.3, "lipides": 10.8, "glucides": 7.6}},
{"truite": {"calories": 141, "protéines": 19, "lipides": 6, "glucides": 0}},
{"thon": {"calories": 132, "protéines": 29, "lipides": 1, "glucides": 0}},
{"crevettes": {"calories": 99, "protéines": 24, "lipides": 0.3, "glucides": 0}},
{"poissons blancs": {"calories": 92, "protéines": 20, "lipides": 1, "glucides": 0}},
],
"legumes": [
{"épinards": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 3.6}},
{"chou-fleur": {"calories": 25, "protéines": 1.9, "lipides": 0.3, "glucides": 5}},
{"courgettes": {"calories": 17, "protéines": 1.2, "lipides": 0.3, "glucides": 3.1}},
{"poivrons": {"calories": 20, "protéines": 0.9, "lipides": 0.2, "glucides": 4.6}},
{"champignons": {"calories": 22, "protéines": 3.1, "lipides": 0.3, "glucides": 3.3}},
{"oignons": {"calories": 40, "protéines": 1.1, "lipides": 0.1, "glucides": 9.3}},
{"betteraves": {"calories": 43, "protéines": 1.6, "lipides": 0.2, "glucides": 9.6}},
{"radis": {"calories": 16, "protéines": 0.7, "lipides": 0.1, "glucides": 3.4}},
],
"feculents": [
{"couscous": {"calories": 112, "protéines": 3.8, "lipides": 0.2, "glucides": 23.4}},
{"patates douces": {"calories": 86, "protéines": 1.6, "lipides": 0.1, "glucides": 20.1}},
{"boulgour": {"calories": 83, "protéines": 3.1, "lipides": 0.2, "glucides": 18.6}},
{"polenta": {"calories": 85, "protéines": 1.9, "lipides": 0.7, "glucides": 18.3}},
{"maïs": {"calories": 86, "protéines": 3.2, "lipides": 1.2, "glucides": 18.7}},
{"orge": {"calories": 123, "protéines": 2.3, "lipides": 0.8, "glucides": 28.2}},
{"millet": {"calories": 118, "protéines": 3.5, "lipides": 1, "glucides": 23}},
{"riz sauvage": {"calories": 101, "protéines": 4, "lipides": 0.3, "glucides": 21.3}},
],
},
}

groupes_aliments_vegetarien = {
"proteines": [
{"tofu": {"calories": 76, "protéines": 8, "lipides": 4.8, "glucides": 1.9}},
{"tempeh": {"calories": 193, "protéines": 20.3, "lipides": 10.8, "glucides": 7.6}},
{"lentilles": {"calories": 116, "protéines": 9, "lipides": 0.4, "glucides": 20}},
{"pois chiches": {"calories": 164, "protéines": 8.9, "lipides": 2.6, "glucides": 27}},
{"oeufs": {"calories": 143, "protéines": 13, "lipides": 9.5, "glucides": 0.7}},
{"fromage": {"calories": 350, "protéines": 25, "lipides": 27, "glucides": 1}},
{"yaourt": {"calories": 59, "protéines": 3.6, "lipides": 3.3, "glucides": 4.7}},
{"quinoa": {"calories": 120, "protéines": 4.4, "lipides": 1.9, "glucides": 21}},
{"noix": {"calories": 607, "protéines": 15, "lipides": 65, "glucides": 14}},
{"graines de tournesol": {"calories": 584, "protéines": 20.8, "lipides": 51.5, "glucides": 20}},
{"graines de chia": {"calories": 486, "protéines": 16.5, "lipides": 30.7, "glucides": 42.1}},
{"graines de lin": {"calories": 534, "protéines": 18.3, "lipides": 42.2, "glucides": 28.9}},
{"graines de citrouille": {"calories": 559, "protéines": 30.2, "lipides": 49.1, "glucides": 10.7}},
{"graines de sésame": {"calories": 573, "protéines": 17.7, "lipides": 49.7, "glucides": 23.4}},
{"lait": {"calories": 42, "protéines": 3.4, "lipides": 1, "glucides": 5}},
{"protéines de pois": {"calories": 376, "protéines": 80, "lipides": 4, "glucides": 4}},
],
"legumes": [
{"brocoli": {"calories": 34, "protéines": 2.8, "lipides": 0.4, "glucides": 6.6}},
{"carottes": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 9.6}},
{"haricots verts": {"calories": 31, "protéines": 1.8, "lipides": 0.2, "glucides": 6.9}},
{"salade": {"calories": 15, "protéines": 1.4, "lipides": 0.2, "glucides": 2.9}},
{"laitue romaine": {"calories": 17, "protéines": 1.2, "lipides": 0.3, "glucides": 3.3}},
{"tomates": {"calories": 18, "protéines": 0.9, "lipides": 0.2, "glucides": 3.9}},
{"concombre": {"calories": 15, "protéines": 0.7, "lipides": 0.1, "glucides": 3.6}},
{"petits pois": {"calories": 81, "protéines": 5.4, "lipides": 0.4, "glucides": 14.5}},
{"asperges": {"calories": 20, "protéines": 2.2, "lipides": 0.1, "glucides": 3.9}},
{"champignons": {"calories": 22, "protéines": 3.1, "lipides": 0.3, "glucides": 3.3}},
{"oignons": {"calories": 40, "protéines": 1.1, "lipides": 0.1, "glucides": 9.3}},
{"betteraves": {"calories": 43, "protéines": 1.6, "lipides": 0.2, "glucides": 9.6}},
{"radis": {"calories": 16, "protéines": 0.7, "lipides": 0.1, "glucides": 3.4}}
],
"feculents": [
{"riz": {"calories": 130, "protéines": 2.7, "lipides": 0.3, "glucides": 28.2}},
{"pâtes": {"calories": 157, "protéines": 5.8, "lipides": 0.9, "glucides": 30.9}},
{"quinoa": {"calories": 120, "protéines": 4.4, "lipides": 1.9, "glucides": 21}},
{"pommes de terre": {"calories": 77, "protéines": 2, "lipides": 0.1, "glucides": 17}},
{"semoule": {"calories": 365, "protéines": 12.7, "lipides": 0.6, "glucides": 72.8}},
{"gnocchi": {"calories": 162, "protéines": 3.1, "lipides": 0.5, "glucides": 34.8}},
{"riz complet": {"calories": 111, "protéines": 2.6, "lipides": 0.9, "glucides": 23}},
{"blé": {"calories": 327, "protéines": 12.6, "lipides": 1.5, "glucides": 71}},
{"couscous": {"calories": 112, "protéines": 3.8, "lipides": 0.2, "glucides": 23.4}},
{"patates douces": {"calories": 86, "protéines": 1.6, "lipides": 0.1, "glucides": 20.1}},
{"boulgour": {"calories": 342, "protéines": 12.3, "lipides": 1.3, "glucides": 75.9}},
{"polenta": {"calories": 85, "protéines": 1.9, "lipides": 0.6, "glucides": 18.1}}
]
}
groupes_aliments_vegan = {
    "proteines": [
        {"tofu": {"calories": 76, "protéines": 8, "lipides": 4.8, "glucides": 1.9}},
        {"tempeh": {"calories": 193, "protéines": 20.3, "lipides": 10.8, "glucides": 7.6}},
        {"lentilles": {"calories": 116, "protéines": 9, "lipides": 0.4, "glucides": 20}},
        {"pois chiches": {"calories": 164, "protéines": 8.9, "lipides": 2.6, "glucides": 27}},
        {"seitan": {"calories": 370, "protéines": 75, "lipides": 2, "glucides": 14}},
        {"quinoa": {"calories": 120, "protéines": 4.4, "lipides": 1.9, "glucides": 21}},
        {"noix": {"calories": 607, "protéines": 15, "lipides": 65, "glucides": 14}},
        {"graines": {"calories": 534, "protéines": 18.3, "lipides": 42.2, "glucides": 28.9}},
        {"lait d'amande": {"calories": 15, "protéines": 0.6, "lipides": 1.1, "glucides": 0}},
        {"lait de soja": {"calories": 54, "protéines": 3.3, "lipides": 1.8, "glucides": 6}},
        {"lait de coco": {"calories": 230, "protéines": 2.3, "lipides": 24, "glucides": 6}},
        {"protéines de pois": {"calories": 376, "protéines": 80, "lipides": 4, "glucides": 4}},
    ],
    "legumes": [
        {"brocoli": {"calories": 34, "protéines": 2.8, "lipides": 0.4, "glucides": 6.6}},
        {"carottes": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 9.6}},
        {"haricots verts": {"calories": 31, "protéines": 1.8, "lipides": 0.2, "glucides": 6.9}},
        {"salade": {"calories": 15, "protéines": 1.4, "lipides": 0.2, "glucides": 2.9}},
        {"tomates": {"calories": 18, "protéines": 0.9, "lipides": 0.2, "glucides": 3.9}},
        {"concombre": {"calories": 15, "protéines": 0.7, "lipides": 0.1, "glucides": 3.6}},
        {"pois": {"calories": 81, "protéines": 5.4, "lipides": 0.4, "glucides": 14.5}},
        {"asperges": {"calories": 20, "protéines": 2.2, "lipides": 0.1, "glucides": 3.9}},
        {"champignons": {"calories": 22, "protéines": 3.1, "lipides": 0.3, "glucides": 3.3}},
        {"oignons": {"calories": 40, "protéines": 1.1, "lipides": 0.1, "glucides": 9.3}},
        {"betteraves": {"calories": 43, "protéines": 1.6, "lipides": 0.2, "glucides": 9.6}},
        {"radis": {"calories": 16, "protéines": 0.7, "lipides": 0.1, "glucides": 3.4}},
    ],
    "feculents": [
        {"riz": {"calories": 130, "protéines": 2.7, "lipides": 0.3, "glucides": 28.2}},
        {"pâtes": {"calories": 157, "protéines": 5.8, "lipides": 0.9, "glucides": 30.9}},
        {"quinoa": {"calories": 120, "protéines": 4.4, "lipides": 1.9, "glucides": 21}},
        {"pommes de terre": {"calories": 77, "protéines": 2, "lipides": 0.1, "glucides": 17}},
        {"semoule": {"calories": 365, "protéines": 12.7, "lipides": 0.6, "glucides": 72.8}},
        {"gnocchi": {"calories": 162, "protéines": 3.1, "lipides": 0.5, "glucides": 34.8}},
        {"riz complet": {"calories": 111, "protéines": 2.6, "lipides": 0.9, "glucides": 23}},
        {"blé": {"calories": 327, "protéines": 12.6, "lipides": 1.5, "glucides": 71}},
        {"couscous": {"calories": 112, "protéines": 3.8, "lipides": 0.2, "glucides": 23.4}},
        {"patates douces": {"calories": 86, "protéines": 1.6, "lipides": 0.1, "glucides": 20.1}},
        {"boulgour": {"calories": 342, "protéines": 12.3, "lipides": 1.3, "glucides": 75.9}},
        {"polenta": {"calories": 85, "protéines": 1.9, "lipides": 0.6, "glucides": 18.1}},
    ]
}
groupes_aliments_pauvre_glucides = {
    "proteines": [
        {"poulet": {"calories": 239, "protéines": 27, "lipides": 14, "glucides": 0}},
        {"boeuf": {"calories": 250, "protéines": 26, "lipides": 17, "glucides": 0}},
        {"tofu": {"calories": 76, "protéines": 8, "lipides": 4.8, "glucides": 1.9}},
        {"pois chiches": {"calories": 364, "protéines": 19, "lipides": 6, "glucides": 61}},
        {"saumon": {"calories": 208, "protéines": 20, "lipides": 13, "glucides": 0}},
        {"dinde": {"calories": 104, "protéines": 22, "lipides": 1, "glucides": 0}},
        {"lentilles": {"calories": 116, "protéines": 9, "lipides": 0.4, "glucides": 20}},
        {"tempeh": {"calories": 193, "protéines": 20, "lipides": 11, "glucides": 9}},
        {"porc": {"calories": 242, "protéines": 25, "lipides": 16, "glucides": 0}},
        {"agneau": {"calories": 294, "protéines": 25, "lipides": 21, "glucides": 0}},
        {"truite": {"calories": 141, "protéines": 19, "lipides": 6.6, "glucides": 0}},
        {"thon": {"calories": 144, "protéines": 23, "lipides": 4.9, "glucides": 0}},
        {"crevettes": {"calories": 85, "protéines": 20, "lipides": 0.5, "glucides": 0}},
        {"poissons blancs": {"calories": 100, "protéines": 20, "lipides": 2, "glucides": 0}},
        {"oeufs": {"calories": 143, "protéines": 13, "lipides": 10, "glucides": 1}},
        {"fromage": {"calories": 402, "protéines": 25, "lipides": 33, "glucides": 1.3}},
    ],

    "legumes": [
        {"brocoli": {"calories": 34, "protéines": 2.8, "lipides": 0.4, "glucides": 6.6}},
        {"carottes": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 9.6}},
        {"haricots verts": {"calories": 31, "protéines": 1.8, "lipides": 0.1, "glucides": 7}},
        {"salade": {"calories": 15, "protéines": 1.4, "lipides": 0.2, "glucides": 2.9}},
        {"épinards": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 3.6}},
        {"chou-fleur": {"calories": 25, "protéines": 1.9, "lipides": 0.3, "glucides": 5}},
        {"courgettes": {"calories": 17, "protéines": 1.2, "lipides": 0.3, "glucides": 3.1}},
        {"poivrons": {"calories": 20, "protéines": 1, "lipides": 0.2, "glucides": 4.6}},
        {"champignons": {"calories": 22, "protéines": 3.1, "lipides": 0.3, "glucides": 3.3}},
        {"oignons": {"calories": 40, "protéines": 1.1, "lipides": 0.1, "glucides": 9.3}},
        {"betteraves": {"calories": 43, "protéines": 1.6, "lipides": 0.2, "glucides": 9.6}},
        {"radis": {"calories": 16, "protéines": 0.7, "lipides": 0.1, "glucides": 3.4}},
        {"concombre": {"calories": 15, "protéines": 0.7, "lipides": 0.1, "glucides": 3.6}},
        {"tomates": {"calories": 18, "protéines": 0.9, "lipides": 0.2, "glucides": 3.9}},
        {"asperges": {"calories": 20, "protéines": 2.2, "lipides": 0.1, "glucides": 3.9}},
        {"pois": {"calories": 81, "protéines": 5.4, "lipides": 0.4, "glucides": 14.5}},
    ],

    "gras_sains": [
        {"avocat": {"calories": 160, "protéines": 2, "lipides": 15, "glucides": 9}},
        {"huile d'olive": {"calories": 884, "protéines": 0, "lipides": 100, "glucides": 0}},
        {"noix": {"calories": 654, "protéines": 15, "lipides": 65, "glucides": 14}},
        {"graines de chia": {"calories": 486, "protéines": 17, "lipides": 31, "glucides": 42}},
        {"beurre de cacahuète": {"calories": 588, "protéines": 25, "lipides": 50, "glucides": 20}},
        {"huile de coco": {"calories": 862, "protéines": 0, "lipides": 94, "glucides": 0}},
        {"amandes": {"calories": 579, "protéines": 21, "lipides": 50, "glucides": 22}},
        {"graines de lin": {"calories": 534, "protéines": 19, "lipides": 42, "glucides": 29}},
        {"huile d'avocat": {"calories": 884, "protéines": 0, "lipides": 100, "glucides": 0}},
        {"huile de noix": {"calories": 884, "protéines": 0, "lipides": 100, "glucides": 0}},
        {"beurre d'amande": {"calories": 614, "protéines": 21, "lipides": 56, "glucides": 19}},
        {"noix de cajou": {"calories": 553, "protéines": 18, "lipides": 44, "glucides": 33}},
    ],
}

fruits_legumes_saisonniers = {
    "printemps": {
            "fruits": [
            {"fraise": {"calories": 33, "protéines": 0.7, "lipides": 0.3, "glucides": 7.7}},
            {"cerise": {"calories": 63, "protéines": 1.1, "lipides": 0.3, "glucides": 13}},
            {"abricot": {"calories": 48, "protéines": 1, "lipides": 0.4, "glucides": 11}},
            {"pêche": {"calories": 39, "protéines": 0.9, "lipides": 0.3, "glucides": 9}},
            {"nectarine": {"calories": 44, "protéines": 1, "lipides": 0.4, "glucides": 10}},
            {"rhubarbe": {"calories": 21, "protéines": 0.9, "lipides": 0.2, "glucides": 4}},
            {"groseille": {"calories": 33, "protéines": 1.4, "lipides": 0.2, "glucides": 5}},
            {"framboise": {"calories": 26, "protéines": 1.2, "lipides": 0.5, "glucides": 5}},
            {"amande": {"calories": 576, "protéines": 21, "lipides": 49, "glucides": 22}}
            ],
      "légumes": [
            {"asperge": {"calories": 20, "protéines": 2.2, "lipides": 0.2, "glucides": 3}},
            {"petit pois": {"calories": 81, "protéines": 5.2, "lipides": 0.5, "glucides": 14}},
            {"épinard": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 1.8}},
            {"radis": {"calories": 14, "protéines": 0.7, "lipides": 0.1, "glucides": 2}},
            {"artichaut": {"calories": 47, "protéines": 3.3, "lipides": 0.2, "glucides": 10}},
            {"laitue": {"calories": 14, "protéines": 1.4, "lipides": 0.2, "glucides": 2}},
            {"oignon nouveau": {"calories": 32, "protéines": 1.3, "lipides": 0.2, "glucides": 6}},
            {"poireau": {"calories": 61, "protéines": 2.2, "lipides": 0.3, "glucides": 12}},
            {"navet": {"calories": 28, "protéines": 1.1, "lipides": 0.2, "glucides": 5}},
            {"carotte": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 8}},
            {"chou-fleur": {"calories": 23, "protéines": 2, "lipides": 0.3, "glucides": 2}},
            {"fève": {"calories": 88, "protéines": 7.6, "lipides": 0.4, "glucides": 12}},
            {"roquette": {"calories": 25, "protéines": 2.6, "lipides": 0.7, "glucides": 2}},
            {"cresson": {"calories": 21, "protéines": 2.8, "lipides": 0.4, "glucides": 0.7}},
            {"ail des ours": {"calories": 47, "protéines": 3, "lipides": 0.5, "glucides": 0.8}}
            ]
    },
    "ete": {
      "fruits": [
{"pêche": {"calories": 39, "protéines": 0.9, "lipides": 0.3, "glucides": 9}},
{"nectarine": {"calories": 44, "protéines": 1, "lipides": 0.4, "glucides": 10}},
{"melon": {"calories": 34, "protéines": 0.9, "lipides": 0.2, "glucides": 8}},
{"framboise": {"calories": 26, "protéines": 1.2, "lipides": 0.5, "glucides": 5}},
{"myrtille": {"calories": 57, "protéines": 0.7, "lipides": 0.3, "glucides": 14}},
{"abricot": {"calories": 48, "protéines": 1, "lipides": 0.4, "glucides": 11}},
{"cerise": {"calories": 63, "protéines": 1.1, "lipides": 0.3, "glucides": 13}},
{"mûre": {"calories": 43, "protéines": 1.4, "lipides": 0.5, "glucides": 7}},
{"prune": {"calories": 46, "protéines": 0.9, "lipides": 0.2, "glucides": 11}},
{"raisin": {"calories": 69, "protéines": 0.7, "lipides": 0.2, "glucides": 18}},
{"pastèque": {"calories": 30, "protéines": 0.6, "lipides": 0.2, "glucides": 7}},
{"pomme": {"calories": 52, "protéines": 0.3, "lipides": 0.2, "glucides": 14}},
{"poire": {"calories": 57, "protéines": 0.4, "lipides": 0.2, "glucides": 15}},
{"figue": {"calories": 74, "protéines": 0.8, "lipides": 0.3, "glucides": 19}},
{"groseille": {"calories": 33, "protéines": 1.4, "lipides": 0.2, "glucides": 5}},
{"cassis": {"calories": 43, "protéines": 1.4, "lipides": 0.4, "glucides": 8}}
],
      "legumes": [
{"tomate": {"calories": 18, "protéines": 0.9, "lipides": 0.2, "glucides": 3.5}},
{"courgette": {"calories": 19, "protéines": 1.2, "lipides": 0.3, "glucides": 3}},
{"poivron": {"calories": 31, "protéines": 1.3, "lipides": 0.4, "glucides": 5}},
{"aubergine": {"calories": 25, "protéines": 1, "lipides": 0.2, "glucides": 6}},
{"concombre": {"calories": 12, "protéines": 0.7, "lipides": 0.1, "glucides": 2}},
{"haricot vert": {"calories": 31, "protéines": 1.9, "lipides": 0.2, "glucides": 5}},
{"radis": {"calories": 14, "protéines": 0.7, "lipides": 0.1, "glucides": 2}},
{"betterave": {"calories": 43, "protéines": 1.6, "lipides": 0.1, "glucides": 10}},
{"maïs": {"calories": 86, "protéines": 3.5, "lipides": 1.5, "glucides": 14}},
{"carotte": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 8}},
{"ail des ours": {"calories": 47, "protéines": 3, "lipides": 0.5, "glucides": 0.8}},
{"fenouil": {"calories": 31, "protéines": 1.2, "lipides": 0.2, "glucides": 7}},
{"chou-rave": {"calories": 27, "protéines": 1.6, "lipides": 0.1, "glucides": 5}},
{"salade": {"calories": 14, "protéines": 1.4, "lipides": 0.2, "glucides": 2}},
{"épinard": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 1.8}},
{"oseille": {"calories": 22, "protéines": 2, "lipides": 0.5, "glucides": 2}},
{"patate douce": {"calories": 86, "protéines": 1.6, "lipides": 0.1, "glucides": 20}}
]
    },
    "automne": {
       "fruits": [
{"pomme": {"calories": 52, "protéines": 0.3, "lipides": 0.2, "glucides": 14}},
{"poire": {"calories": 57, "protéines": 0.4, "lipides": 0.2, "glucides": 15}},
{"raisin": {"calories": 69, "protéines": 0.7, "lipides": 0.2, "glucides": 18}},
{"prune": {"calories": 46, "protéines": 0.9, "lipides": 0.2, "glucides": 11}},
{"coing": {"calories": 63, "protéines": 0.6, "lipides": 0.1, "glucides": 15}},
{"noix": {"calories": 654, "protéines": 15.2, "lipides": 65.2, "glucides": 13}},
{"noisette": {"calories": 628, "protéines": 14, "lipides": 61.3, "glucides": 16.7}},
{"amande": {"calories": 579, "protéines": 21.2, "lipides": 49.9, "glucides": 21.7}},
{"châtaigne": {"calories": 213, "protéines": 2.7, "lipides": 2.2, "glucides": 46}},
{"mûre": {"calories": 43, "protéines": 1.4, "lipides": 0.5, "glucides": 7}},
{"kaki": {"calories": 71, "protéines": 0.6, "lipides": 0.2, "glucides": 18}},
{"figue": {"calories": 74, "protéines": 0.8, "lipides": 0.3, "glucides": 19}},
{"grenade": {"calories": 83, "protéines": 1.2, "lipides": 1.2, "glucides": 19}},
{"cynorhodon": {"calories": 162, "protéines": 1.6, "lipides": 0.7, "glucides": 38}}
],
"legumes": [
{"chou": {"calories": 27, "protéines": 1.4, "lipides": 0.1, "glucides": 5.2}},
{"potiron": {"calories": 20, "protéines": 1, "lipides": 0.1, "glucides": 4}},
{"brocoli": {"calories": 34, "protéines": 4, "lipides": 0.4, "glucides": 2.8}},
{"betterave": {"calories": 43, "protéines": 1.6, "lipides": 0.1, "glucides": 10}},
{"navet": {"calories": 20, "protéines": 1, "lipides": 0.1, "glucides": 4}},
{"haricot vert": {"calories": 31, "protéines": 1.9, "lipides": 0.2, "glucides": 5}},
{"panais": {"calories": 75, "protéines": 1.4, "lipides": 0.3, "glucides": 18}},
{"poireau": {"calories": 61, "protéines": 2.3, "lipides": 0.3, "glucides": 12}},
{"champignon": {"calories": 22, "protéines": 3.1, "lipides": 0.3, "glucides": 0.2}},
{"citrouille": {"calories": 26, "protéines": 1, "lipides": 0.1, "glucides": 6}},
{"patate douce": {"calories": 86, "protéines": 1.6, "lipides": 0.1, "glucides": 20}},
{"topinambour": {"calories": 73, "protéines": 2, "lipides": 0.4, "glucides": 16}},
{"courge": {"calories": 26, "protéines": 1, "lipides": 0.1, "glucides": 6}},
{"céleri-rave": {"calories": 42, "protéines": 1.5, "lipides": 0.3, "glucides": 8}},
{"carotte": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 8}},
{"radis": {"calories": 14, "protéines": 0.7, "lipides": 0.1, "glucides": 2}},
{"épinard": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 0.4}}],
    },
    "hiver": {
"fruits": [
{"orange": {"calories": 47, "protéines": 0.9, "lipides": 0.2, "glucides": 11}},
{"clémentine": {"calories": 47, "protéines": 0.9, "lipides": 0.2, "glucides": 11}},
{"kiwi": {"calories": 61, "protéines": 1.1, "lipides": 0.6, "glucides": 14}},
{"pomme": {"calories": 52, "protéines": 0.3, "lipides": 0.2, "glucides": 14}},
{"poire": {"calories": 57, "protéines": 0.4, "lipides": 0.2, "glucides": 15}},
{"mandarine": {"calories": 53, "protéines": 0.8, "lipides": 0.3, "glucides": 12}},
{"citron": {"calories": 29, "protéines": 1.1, "lipides": 0.3, "glucides": 9}},
{"banane": {"calories": 89, "protéines": 1.1, "lipides": 0.3, "glucides": 23}},
{"ananas": {"calories": 50, "protéines": 0.5, "lipides": 0.1, "glucides": 13}},
{"grenade": {"calories": 83, "protéines": 1.2, "lipides": 1.2, "glucides": 19}},
{"datte": {"calories": 282, "protéines": 2.5, "lipides": 0.5, "glucides": 75}},
{"noix": {"calories": 654, "protéines": 15.2, "lipides": 65.2, "glucides": 13}},
{"noisette": {"calories": 628, "protéines": 14, "lipides": 61.3, "glucides": 16.7}},
{"pamplemousse": {"calories": 42, "protéines": 0.7, "lipides": 0.1, "glucides": 10}},
{"avocat": {"calories": 160, "protéines": 2, "lipides": 15, "glucides": 9}}
],
        "legumes": [
{"choux de Bruxelles": {"calories": 43, "protéines": 3.8, "lipides": 0.5, "glucides": 7.9}},
{"navet": {"calories": 20, "protéines": 1, "lipides": 0.1, "glucides": 4}},
{"poireau": {"calories": 61, "protéines": 2.3, "lipides": 0.3, "glucides": 12}},
{"carotte": {"calories": 41, "protéines": 0.9, "lipides": 0.2, "glucides": 8}},
{"endive": {"calories": 17, "protéines": 1.1, "lipides": 0.2, "glucides": 2.2}},
{"chou": {"calories": 27, "protéines": 1.4, "lipides": 0.1, "glucides": 5.2}},
{"chou-fleur": {"calories": 25, "protéines": 2, "lipides": 0.3, "glucides": 4}},
{"brocoli": {"calories": 34, "protéines": 4, "lipides": 0.4, "glucides": 2.8}},
{"betterave": {"calories": 43, "protéines": 1.6, "lipides": 0.1, "glucides": 10}},
{"céleri": {"calories": 16, "protéines": 0.7, "lipides": 0.2, "glucides": 3}},
{"épinard": {"calories": 23, "protéines": 2.9, "lipides": 0.4, "glucides": 0.4}},
{"blette": {"calories": 19, "protéines": 2.3, "lipides": 0.3, "glucides": 1.2}},
{"scarole": {"calories": 17, "protéines": 1.5, "lipides": 0.2, "glucides": 2.8}},
{"frisée": {"calories": 15, "protéines": 1.5, "lipides": 0.2, "glucides": 1.1}},
{"mâche": {"calories": 22, "protéines": 2, "lipides": 0.3, "glucides": 2}},
{"oignon": {"calories": 40, "protéines": 1.1, "lipides": 0.1, "glucides": 9}},
{"ail": {"calories": 149, "protéines": 6.4, "lipides": 0.5, "glucides": 33}},
{"pomme de terre": {"calories": 77, "protéines": 2, "lipides": 0.1, "glucides": 17}}
],
    },
}
collations = {
    "fruits": [
{"pomme": {"calories": 52, "protéines": 0.3, "lipides": 0.2, "glucides": 14}},
{"banane": {"calories": 89, "protéines": 1.1, "lipides": 0.3, "glucides": 23}},
{"orange": {"calories": 47, "protéines": 0.9, "lipides": 0.2, "glucides": 11}},
{"fraise": {"calories": 33, "protéines": 0.7, "lipides": 0.5, "glucides": 7}},
{"kiwi": {"calories": 61, "protéines": 1.1, "lipides": 0.6, "glucides": 14}},
{"raisin": {"calories": 69, "protéines": 0.7, "lipides": 0.2, "glucides": 18}},
{"ananas": {"calories": 50, "protéines": 0.5, "lipides": 0.1, "glucides": 13}},
{"mangue": {"calories": 60, "protéines": 0.8, "lipides": 0.4, "glucides": 15}}
],
    "nuts_and_seeds": [
{"amande": {"calories": 579, "protéines": 21, "lipides": 50, "glucides": 22}},
{"noix": {"calories": 654, "protéines": 15, "lipides": 65, "glucides": 14}},
{"noisette": {"calories": 628, "protéines": 14, "lipides": 62, "glucides": 17}},
{"graines de tournesol": {"calories": 584, "protéines": 21, "lipides": 51, "glucides": 20}},
{"graines de citrouille": {"calories": 559, "protéines": 30, "lipides": 49, "glucides": 11}},
{"pistache": {"calories": 557, "protéines": 20, "lipides": 45, "glucides": 27}}
],  
 "yogurts": [
{"yaourt nature": {"calories": 63, "protéines": 4.1, "lipides": 3.5, "glucides": 4.7}},
{"yaourt aux fruits": {"calories": 83, "protéines": 3.1, "lipides": 2.9, "glucides": 12.6}},
{"yaourt grec": {"calories": 133, "protéines": 9, "lipides": 10, "glucides": 3.5}},
{"yaourt végétal": {"calories": 60, "protéines": 1.5, "lipides": 2.5, "glucides": 7.5}}
],

"bars": [
{"barre de céréales": {"calories": 120, "protéines": 2, "lipides": 3, "glucides": 21}},
{"barre de granola": {"calories": 118, "protéines": 3, "lipides": 5, "glucides": 16}},
{"barre énergétique": {"calories": 250, "protéines": 10, "lipides": 9, "glucides": 33}},
{"barre protéinée": {"calories": 220, "protéines": 20, "lipides": 7, "glucides": 22}}
]
}

boissons = {
"eau": [
{"eau plate": {"calories": 0, "protéines": 0, "lipides": 0, "glucides": 0}},
{"eau gazeuse": {"calories": 0, "protéines": 0, "lipides": 0, "glucides": 0}}
],
   "the_cafe": [
{"thé": {"calories": 1, "protéines": 0, "lipides": 0, "glucides": 0.2}},
{"café": {"calories": 1, "protéines": 0.1, "lipides": 0, "glucides": 0}},
{"tisane": {"calories": 0, "protéines": 0, "lipides": 0, "glucides": 0}},
{"infusion": {"calories": 0, "protéines": 0, "lipides": 0, "glucides": 0}}
],
"jus": [
{"jus d'orange": {"calories": 46, "protéines": 0.7, "lipides": 0.2, "glucides": 10}},
{"jus de pomme": {"calories": 50, "protéines": 0.1, "lipides": 0, "glucides": 13}},
{"jus de raisin": {"calories": 70, "protéines": 0.5, "lipides": 0.2, "glucides": 17}},
{"jus de tomate": {"calories": 17, "protéines": 0.9, "lipides": 0.2, "glucides": 3.5}},
{"jus d'ananas": {"calories": 50, "protéines": 0.5, "lipides": 0, "glucides": 12}},
{"jus de mangue": {"calories": 65, "protéines": 0.7, "lipides": 0.4, "glucides": 15}}
],
"boissons_vegetales": [
{"lait d'amande": {"calories": 36, "protéines": 1, "lipides": 3, "glucides": 1}},
{"lait de soja": {"calories": 54, "protéines": 3.3, "lipides": 1.8, "glucides": 4}},
{"lait de coco": {"calories": 230, "protéines": 2, "lipides": 24, "glucides": 5}},
{"lait de riz": {"calories": 47, "protéines": 0.3, "lipides": 1, "glucides": 9.7}}
],
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

def poids_aliments(calories, macronutriments):
    somme_macronutriments = (macronutriments["protéines"] * 4) + (macronutriments["lipides"] * 9) + (macronutriments["glucides"] * 4)
    if somme_macronutriments == 0:
        return 0
    poids = 100 * (calories / somme_macronutriments)
    return round(poids, 2)

def generer_menus(nombre_de_jours, groupes_aliments, saison, vegetarien, calories_quotidiennes):
    menus = {"petit_dejeuner": [], "dejeuner": [], "diner": [], "collation": [], "boisson": []}
    
    for i in range(nombre_de_jours):
        petit_dejeuner = {
            "cereales": random.choice(groupes_aliments["petit_dejeuner"]["cereales"]),
            "produits_laitiers": random.choice(groupes_aliments["petit_dejeuner"]["produits_laitiers"]),
            "fruits": random.choice(fruits_legumes_saisonniers[saison]["fruits"])
        }
        for aliment, details in petit_dejeuner.items():
            # print(f"Avant : {details}")
            nom = list(details.keys())[0]
            details_aliment = details[nom]
            details_aliment['nom'] = nom.capitalize()
            # print(f"Après : {details}")
            if 'calories' in details_aliment:
                poids = poids_aliments(details_aliment['calories'], details_aliment)
                details_aliment['poids'] = poids
            details['nom'] = details_aliment
                
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
        for aliment, details in dejeuner.items():
            nom = list(details.keys())[0]
            details_aliment = details[nom]
            details_aliment['nom'] = nom.capitalize()
            if 'calories' in details_aliment:
                poids = poids_aliments(details_aliment['calories'], details_aliment)
                details_aliment['poids'] = poids
            details['nom'] = details_aliment
                
        menus["dejeuner"].append(dejeuner)

        diner = {
            "proteines": proteines_diner,
            "legumes": random.choice(fruits_legumes_saisonniers[saison]["legumes"]),
            "feculents": random.choice(groupes_aliments["diner"]["feculents"])
        }
        for aliment, details in diner.items():
            nom = list(details.keys())[0]
            details_aliment = details[nom]
            details_aliment['nom'] = nom.capitalize()            
            if 'calories' in details_aliment:
                poids = poids_aliments(details_aliment['calories'], details_aliment)
                details_aliment['poids'] = poids
            details['nom'] = details_aliment
                
        menus["diner"].append(diner)

        collation = {
            "fruits": random.choice(collations["fruits"]),
            "nuts_and_seeds": random.choice(collations["nuts_and_seeds"]),
            "yogurts": random.choice(collations["yogurts"]),
            "bars": random.choice(collations["bars"]),
        }
        for aliment, details in collation.items():
            nom = list(details.keys())[0]
            details_aliment = details[nom]
            details_aliment['nom'] = nom.capitalize()
            if 'calories' in details_aliment:
                poids = poids_aliments(details_aliment['calories'], details_aliment)
                details_aliment['poids'] = poids
            details['nom'] = details_aliment
                
        menus["collation"].append(collation)

        boisson = {
            "eau": random.choice(boissons["eau"]),
            "the_cafe": random.choice(boissons["the_cafe"]),
            "jus": random.choice(boissons["jus"]),
            "boissons_vegetales": random.choice(boissons["boissons_vegetales"]),
        }
        for aliment, details in boisson.items():
            nom = list(details.keys())[0]
            details_aliment = details[nom]
            details_aliment['nom'] = nom.capitalize()
            if 'calories' in details_aliment:
                poids = poids_aliments(details_aliment['calories'], details_aliment)
                details_aliment['poids'] = poids
            details['nom'] = details_aliment
                
        menus["boisson"].append(boisson)

        # Modification pour prendre en compte les calories quotidiennes
        for repas in menus.values():
            for jour in repas:
                calories_total = 0
                for aliment in jour.values():
                    if "calories" in aliment:
                        calories_total += aliment["calories"]
                        
                if calories_total > 0:
                    ratio_calories = calories_quotidiennes / calories_total
                    
                    for aliment, details in jour.items():
                        if "calories" in details:
                            calories_par_gramme = details["calories"] / 100
                            poids = (details["calories"] * ratio_calories) / calories_par_gramme
                            details['poids'] = round(poids, 2)
                            details['calories'] = int(details['calories'] * ratio_calories)
                            details['protéines'] = round(details['protéines'] * ratio_calories, 2)
                            details['lipides'] = round(details['lipides'] * ratio_calories, 2)
                            details['glucides'] = round(details['glucides'] * ratio_calories, 2)

    return menus

date_str = input("Entrez la date (format : JJ/MM/AAAA) : ")
date = datetime.strptime(date_str, "%d/%m/%Y")
saison = determiner_saison(date)


calories_quotidiennes_str = input("Entrez le nombre de calories quotidiennes souhaitées : ")
calories_quotidiennes = int(calories_quotidiennes_str)

vegetarien_str = input("Êtes-vous végétarien ? (oui/non) : ")
vegetarien = vegetarien_str.lower() == "oui"

nombre_de_jours_str = input("Pour combien de jours souhaitez-vous générer des menus ? : ")
nombre_de_jours = int(nombre_de_jours_str)
menus = generer_menus(nombre_de_jours, groupes_aliments, saison, vegetarien, calories_quotidiennes)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)


def print_repas(repas, repas_label):
    pdf.cell(10)
    pdf.cell(180, 10, txt=f"{repas_label}:", ln=True)

    aliments_list = []
    for aliment, details in repas.items():
        aliment_str = f"{details['nom']}"

        if 'poids' in details:
            aliment_str += f" ({details['poids']}g)"

        calories_str = f"{details['calories']} kcal" if 'calories' in details else "N/A"
        proteines_str = f"{details['protéines']}g" if 'protéines' in details else "N/A"
        lipides_str = f"{details['lipides']}g" if 'lipides' in details else "N/A"
        glucides_str = f"{details['glucides']}g" if 'glucides' in details else "N/A"

        aliments_list.append(f"  - {aliment_str}: Calories: {calories_str}, Protéines: {proteines_str}, Lipides: {lipides_str}, Glucides: {glucides_str}")

    for aliment in aliments_list:
        pdf.cell(10)
        pdf.cell(180, 10, txt=aliment, ln=True)

    pdf.cell(10)
    pdf.cell(180, 10, txt="", ln=True)

for i in range(nombre_de_jours):
    pdf.cell(10)
    pdf.cell(180, 10, txt=f"Jour {i+1}:", ln=True, align="C")
    pdf.cell(10)
    pdf.cell(180, 10, txt=f"Date : {date.strftime('%d/%m/%Y')}", ln=True, align="R")
    pdf.cell(10)
    pdf.cell(180, 10, txt=f"Saison : {saison.capitalize()}", ln=True, align="R")

    pdf.cell(10)
    print_repas(menus['petit_dejeuner'][i], "Petit déjeuner")
    print_repas(menus['dejeuner'][i], "Déjeuner")
    print_repas(menus['collation'][i], "Collation")
    print_repas(menus['diner'][i], "Dîner")
    print_repas(menus['boisson'][i], "Boisson")
    pdf.cell(10)
    pdf.cell(180, 10, txt="", ln=True)
    
pdf.output("menus.pdf")
print("Fichier PDF créé avec succès.")


""" for i in range(nombre_de_jours):
    print(f"Jour {i+1}:")
    print(f"Petit déjeuner: {menus['petit_dejeuner'][i]}")
    print(f"Déjeuner: {menus['dejeuner'][i]}")
    print(f"Collation: {menus['collation'][i]}")
    print(f"Dîner: {menus['diner'][i]}\n")
    print(f"Boisson: {menus['boisson'][i]}\n") """