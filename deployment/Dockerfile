FROM python:3.10-slim

# 📁 Set working directory
WORKDIR /app

# 🔄 Copy files into container
COPY . .

# 📦 Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 🚪 Expose FastAPI port
EXPOSE 8000

# 🚀 Command to start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
