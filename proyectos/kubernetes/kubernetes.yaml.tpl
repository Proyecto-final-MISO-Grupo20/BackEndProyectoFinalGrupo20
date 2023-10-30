apiVersion: apps/v1
kind: Deployment
metadata:
  name: proyectos
  labels:
    app: proyectos
spec:
  replicas: 1
  selector:
    matchLabels:
      app: proyectos
  template:
    metadata:
      labels:
        app: proyectos
    spec:
      containers:
      - name: proyectos
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/proyectos:COMMIT_SHA
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
        imagePullPolicy: Always
---
apiVersion: cloud.google.com/v1
kind: BackendConfig
metadata:
  name: proyectos-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /proyectos/ping
---
kind: Service
apiVersion: v1
metadata:
  name: proyectos-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "proyectos-config"}'
spec:
  type: NodePort
  selector:
    app: proyectos
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31025
