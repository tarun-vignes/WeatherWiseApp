from fastapi import FastAPI

app = FastAPI(title="WeatherWise API")


@app.get("/api/health")
def health_check() -> dict[str, str]:
    """Provide a simple way to confirm the API is running."""
    return {"status": "ok"}
