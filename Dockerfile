FROM python:3.11-slim
WORKDIR /app
COPY requirements-advanced.txt requirements-core.txt ./
RUN pip install --no-cache-dir -r requirements-advanced.txt
COPY src ./src
COPY artifacts ./artifacts
EXPOSE 8000
CMD ["uvicorn", "src.production_example.api:app", "--host", "0.0.0.0", "--port", "8000"]
