#creamdo un diccionario
persona={
    "Nombre":"Oscar",
    "Edad":16,
    "Profecion":"programador",
    "Estudiante":False
}
print(persona)
print(persona["Nombre"])
print(persona.get("profecion"))
persona["Edad"]=16
print(persona["Edad"])