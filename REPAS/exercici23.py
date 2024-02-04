import json
llibres = """"
    {
        "book": [
            {"title": "La Sociedad Industrial y su Futuro", "cover": "Freedom Club", "year": 2011, "pages": 181},
            {"title": "Leon Tolstoi Mejores Cuentos", "cover": "Grandes Genios De La Literatura Universal", "year": 1984, "pages": 189},
            {"title": "Las Supernovas El brillante final de una estrella", "cover": "Un paseo por el COSMOS", "year": 2016, "pages": 149},
            {"title": "Crimen y Castigo", "cover": "Fiodor Dostoyevski", "year": 2013, "pages": 797}
        ]
    }
"""
with open('llibres.json', 'w') as file:
    json.dump(llibres,file)