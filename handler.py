import runpod
from api_v2 import TTS_Request, tts_handle


async def handler(request: TTS_Request):
    req = request.dict()
    return await tts_handle(req)


runpod.serverless.start({"handler": handler})
