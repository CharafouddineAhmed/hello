#/usr/bin/python 

# Ouverture du fichier de confi YML 

input_path = '/Users/ahmedcharafouddine/hello/config/001-input.yml'

def recuperation_des_valeurs(file):
    import yaml
    with open(str(file)) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        fruits_list = yaml.load(file, Loader=yaml.FullLoader)
        print(fruits_list)

recuperation_des_valeurs(input_path)

# initialisation 
# - Generation des fichier pipeline  pour ligstash 
# - creation de repertoire /appli/.../alerting

# lancement de la requete
# formatisation de de l'output / recuperation de la valeur
# envoie dans le output path host 


# [2021-03-26 18:54:22.2443453] [job_name] [valeur] [seuil]