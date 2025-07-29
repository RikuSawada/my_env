FROM python:3.11-slim

# poppler-utils を追加（pdf → image変換に必要）
RUN apt-get update && apt-get install -y poppler-utils

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]