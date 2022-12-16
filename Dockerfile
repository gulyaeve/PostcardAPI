FROM python:3.10.5-bullseye

RUN apt update
RUN apt install chromium -y
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

WORKDIR /src

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
