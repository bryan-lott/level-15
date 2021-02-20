FROM python:3

RUN apt update
RUN apt install -y libgl1-mesa-glx

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./src/app.py"]