# 1. Base Image: Choose a lightweight official Python runtime
FROM python:3.14-slim
LABEL authors="chatty"
# 2. Working Directory: Set the internal app path
WORKDIR /app
# 3. Environment Variables:
# - PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files inside container
# - PYTHONUNBUFFERED=1: Flushes stdout/stderr immediately for real-time terminal logs
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1
# 4. Dependency Layer Caching Strategy:
# HINT: Copy requirements.txt FIRST before copying any application code!
COPY requirements.txt .
# 5. Install Dependencies:
# HINT: Use -no-cache-dir to keep the Docker image slim
RUN pip install --no-cache-dir -r requirements.txt
# 6. Copy Application Source & Entrypoint:
COPY src/ ./src/
COPY entrypoint.sh .
# 7. Document Exposed Ports:
# Both Streamlit (8501) and Phoenix (6006) must be exposed
EXPOSE 8501 6006
# 8. Container Entrypoint:
ENTRYPOINT ["./entrypoint.sh"]