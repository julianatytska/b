from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return 'Hello, World!'

if name == 'main':
    app.run(debug=True)

# Файл deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: your-username/hello-world-app
        ports:
        - containerPort: 5000




FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]
Flask==2.0.1
