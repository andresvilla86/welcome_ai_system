import json

guest_list = [
    {
        "nombre": "andres",
        "registro": "pendiente"
    },
    {
        "nombre": "elon",
        "registro": "completo"
    }
]



for guest in guest_list:
    if guest["nombre"] == "elon":
        print("hay un match")
        if guest["registro"] == "pendiente":
            print("enviar mensaje y update lista")






#print(json.dumps(guest_list, indent=2))

