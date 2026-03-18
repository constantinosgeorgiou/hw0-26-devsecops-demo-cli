FROM python:3.9-slim-buster

# Intentionally using an older Debian-based tag to make known CVEs more likely.
LABEL org.opencontainers.image.source="https://github.com/constantinosgeorgiou"
LABEL org.opencontainers.image.title="hw0-constantinos-devsecops-scan"

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY app.py /app/app.py

ENTRYPOINT ["python3", "/app/app.py"]

