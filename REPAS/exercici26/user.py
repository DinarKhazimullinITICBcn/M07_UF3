class user:
    def __init__(self, nom, cognom, edat, altura, pes, genere):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.altura = altura
        self.pes = pes
        self.genere = genere
    def get_nom(self):
        return self.nom
    def get_cognom(self):
        return self.cognom
    def get_edat(self):
        return self.edat
    def get_altura(self):
        return self.altura
    def get_pes(self):
        return self.pes
    def get_genere(self):
        return self.genere
    def set_nom(self, nom):
        self.nom = nom
    def set_cognom(self, cognom):
        self.cognom = cognom
    def set_edat(self, edat):
        self.edat = edat
    def set_altura(self, altura):
        self.altura = altura
    def set_pes(self, pes):
        self.pes = pes
    def set_genere(self, genere):
        self.genere = genere
    def salutacio(self):
        print(f'Nom: {self.nom}\nCognom: {self.cognom}\nEdat: {self.edat}\Altura: {self.altura}\Pes: {self.pes}\Genere: {self.genere}')
    def to_dict(self):
        return {
            "Nom": self.get_nom(),
            "Cognom": self.get_cognom(),
            "Edat": self.get_edat(),
            "Altura": self.get_altura(),
            "Pes": self.get_pes(),
            "Genere": self.get_genere()
        }
