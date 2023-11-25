apiVersion: apps/v1
kind: Deployment
metadata:
  name: contratos
  labels:
    app: contratos
spec:
  replicas: 1
  selector:
    matchLabels:
      app: contratos
  template:
    metadata:
      labels:
        app: contratos
    spec:
      containers:
      - name: contratos
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/contratos:COMMIT_SHA
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
  name: contratos-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /contratos/ping
---
kind: Service
apiVersion: v1
metadata:
  name: contratos-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "contratos-config"}'
spec:
  type: NodePort
  selector:
    app: contratos
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31055
