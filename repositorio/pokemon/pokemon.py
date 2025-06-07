class Pokemon:
    def __init__(self, nombre, defensa, ataque, tipo="N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.atque = ataque
        self.tipo = tipo

    def __str__(self):
        tipo_emojis ={
            "Fuego": "🔥",
            "Hierba": "🌿",
            "Venenoso": "🤢",
            "Electrico": "🌩️"
        }
        emoji = tipo_emojis.get(self.tipo, "?")
        return f"{self.nombre}{self.tipo}"