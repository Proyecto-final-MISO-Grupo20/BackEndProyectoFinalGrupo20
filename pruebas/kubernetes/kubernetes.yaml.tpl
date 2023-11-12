apiVersion: apps/v1
kind: Deployment
metadata:
  name: pruebas
  labels:
    app: pruebas
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pruebas
  template:
    metadata:
      labels:
        app: pruebas
    spec:
      containers:
      - name: pruebas
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/pruebas:COMMIT_SHA
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
  name: pruebas-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /pruebas/ping
---
kind: Service
apiVersion: v1
metadata:
  name: pruebas-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "pruebas-config"}'
spec:
  type: NodePort
  selector:
    app: pruebas
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31045
