import os
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, Response, request

app = Flask(__name__)

LOG_PATH = os.getenv("LOG_PATH", "/var/log/app/visitas.log")
try:
    Path(LOG_PATH).parent.mkdir(parents=True, exist_ok=True)
except PermissionError:
    pass


@app.before_request
def log_request() -> None:
    ts = datetime.now(timezone.utc).isoformat()
    client_ip = request.remote_addr or "unknown"
    line = f"{ts} ip={client_ip} method={request.method} path={request.path}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(line)


@app.get("/")
def root() -> Response:
    student_name = os.getenv("STUDENT_NAME", "Anon")
    neighborhood = os.getenv("NEIGHBORHOOD") or os.getenv("BARRIO", "Unknown")
    msg = f"Hola, I am {student_name} and I live in {neighborhood}"
    return Response(msg, mimetype="text/plain")


@app.get("/health")
def health():
    return {"status": "UP"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)