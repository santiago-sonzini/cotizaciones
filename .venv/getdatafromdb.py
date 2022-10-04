from os import name
from prisma import Prisma
import asyncio

db = Prisma()

async def createCotizacion(data) -> None:
    await db.connect()

    cotizacion = await db.cotizacion.create(
        {
            #'name': 'MyControl',
            #'email': 'santisonzini1234@gmail.com',
            #'servicios': {'connect': [{'id': "cl8tjrkar0000vj1fyfljdzvw"}, {'id': 'cl8tjtbpo0000wu1fmyzqtz65'}]}
            
            data
        }
    )
    print(f'created post: {cotizacion.json(indent=2, sort_keys=True)}')

   

    await db.disconnect()


async def getCotizacion(id) -> None:
    await db.connect()

    cotizacion = await db.cotizacion.find_unique(
        
            where={'id': id}, include= {'servicios': True}
        
    )

    assert cotizacion is not None
    print(f'found cotizacion: {cotizacion.json(indent=2, sort_keys=True)}')

    await db.disconnect()
    
    
async def createServicio(data) -> None:
    await db.connect()

    servicio = await db.servicios.create(
        {   
            
            #'name': 'Desarrollo Web',
            #'description': 'creacion de web con teconoligias de punta',
            #'price': 3424
            
            data
        }
    )
    print(f'created service: {servicio.json(indent=2, sort_keys=True)}')

   

    await db.disconnect()
    
    
asyncio.run(createServicio())