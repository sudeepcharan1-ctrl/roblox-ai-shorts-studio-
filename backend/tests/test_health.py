import asyncio

import httpx

from app.main import app


async def make_request(path: str) -> httpx.Response:
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        return await client.get(path)


def test_root_endpoint():
    response = asyncio.run(make_request("/"))

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = asyncio.run(make_request("/api/v1/health"))

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "roblox-shorts-ai-studio",
    }
