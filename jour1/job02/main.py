class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def __str__(self):
        return f"Le nombre1 est {self.nombre1}\nLe nombre2 est {self.nombre2}"

# Instanciation de la classe Operation
operation = Operation(12, 3)
print(operation)