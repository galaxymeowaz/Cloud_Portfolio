# 1. Use a lightweight Python base image (The OS)
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local files into the container
COPY . /app

# 4. Install dependencies (if you had a requirements.txt)
# RUN pip install requests google-api-python-client

# 5. The command to run when the container starts
CMD ["python", "calendar_sync.py"]
