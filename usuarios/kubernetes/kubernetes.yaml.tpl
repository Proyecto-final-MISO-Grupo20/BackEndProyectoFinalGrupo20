apiVersion: apps/v1
kind: Deployment
metadata:
  name: usuarios
  labels:
    app: usuarios
spec:
  replicas: 1
  selector:
    matchLabels:
      app: usuarios
  template:
    metadata:
      labels:
        app: usuarios
    spec:
      containers:
      - name: usuarios
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/usuarios:COMMIT_SHA
        ports:
          - containerPort: 3000
        env:
          - name: JWT_SECRET_KEY
            valueFrom:
              secretKeyRef:
                name: appsecrets
                key: jwt_secret_key
          - name: DATABASE_URL
            valueFrom:
              secretKeyRef:
                name: appsecrets
                key: usuarios_uri
          - name: AUTH_PATH
            value: auth-microservice
        imagePullPolicy: Always
---
apiVersion: cloud.google.com/v1
kind: BackendConfig
metadata:
  name: usuarios-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /usuarios/ping
---
kind: Service
apiVersion: v1
metadata:
  name: usuarios-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "usuarios-config"}'
spec:
  type: NodePort
  selector:
    app: usuarios
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31015
