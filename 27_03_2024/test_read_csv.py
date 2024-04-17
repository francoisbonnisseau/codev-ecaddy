import csv
with open('materiel_asus.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("Nom : " + row['Nom'], "Marque : " + row['Marque'], "Prix : " + row['Prix'], "Description : " + row['Description'], "url : " + row['Url'], "Url image : " + row['Url_image'])