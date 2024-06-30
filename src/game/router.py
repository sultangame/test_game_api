from fastapi import APIRouter, WebSocket


game_router = APIRouter(
    prefix="/game",
    tags=["game"]
)


@game_router.websocket("/ws/game/")
async def start_game(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive()
        await websocket.send_text(f"Message text was: {data}")
