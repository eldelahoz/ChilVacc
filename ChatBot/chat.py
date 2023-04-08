from botbuilder.core import TurnContext, BotFrameworkAdapter, BotFrameworkAdapterSettings, ActivityHandler
from botbuilder.schema import Activity, ActivityTypes
import asyncio

# Configurar el adaptador de BotFramework
SETTINGS = BotFrameworkAdapterSettings("TU_APP_ID", "TU_APP_PASSWORD")
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Clase de manejador de actividad
class MyBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Obtener texto del usuario
        text = turn_context.activity.text

        # Crear respuesta
        response = f"¡Hola, {text}! Soy un bot creado con BotBuilder."

        # Enviar respuesta al usuario
        await turn_context.send_activity(Activity(type=ActivityTypes.message, text=response))

# Configurar el enrutador de mensajes
async def on_turn(turn_context: TurnContext):
    # Crear manejador de actividad
    bot = MyBot()

    # Manejar actividad del usuario
    await bot.on_turn(turn_context)

# Ejecutar el bot
async def main(req, res):
    if req.method == 'POST':
        # Convertir solicitud en actividad
        activity = await ADAPTER.process_activity(req, res, on_turn)

        if activity:
            # Enviar actividad al usuario
            await ADAPTER.send_activities_async([activity])

    else:
        # Responder que el método no está permitido
        res.status = 405

if __name__ == "__main__":
    # Ejecutar aplicación
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(ADAPTER.process_async())
    app.router.add_post("/api/messages", main)
    loop.run_until_complete(app.startup())
    loop.run_forever()
