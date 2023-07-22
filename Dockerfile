FROM python:3.9

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .

RUN pip install streamlit

COPY app/algos /app/algos
EXPOSE  80

CMD ["streamlit", "run", "app.py", "--server.port", "80"]
