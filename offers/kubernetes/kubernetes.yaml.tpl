apiVersion: apps/v1
kind: Deployment
metadata:
  name: offers
  labels:
    app: offers
spec:
  replicas: 1
  selector:
    matchLabels:
      app: offers
  template:
    metadata:
      labels:
        app: offers
    spec:
      containers:
      - name: offers
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/offers:COMMIT_SHA
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
                key: db_app_uri
          - name: AUTH_PATH
            value: auth-microservice
        imagePullPolicy: Always
---
apiVersion: cloud.google.com/v1
kind: BackendConfig
metadata:
  name: offers-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /offers/ping
---
kind: Service
apiVersion: v1
metadata:
  name: offers-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "offers-config"}'
spec:
  type: NodePort
  selector:
    app: offers
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31045
