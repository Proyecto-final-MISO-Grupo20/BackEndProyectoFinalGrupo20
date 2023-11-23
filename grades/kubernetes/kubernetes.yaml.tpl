apiVersion: apps/v1
kind: Deployment
metadata:
  name: grades
  labels:
    app: grades
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grades
  template:
    metadata:
      labels:
        app: grades
    spec:
      containers:
      - name: grades
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/grades:COMMIT_SHA
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
          - name: USERS_PATH
            value: usuarios-microservice
        imagePullPolicy: Always
---
apiVersion: cloud.google.com/v1
kind: BackendConfig
metadata:
  name: grades-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /grades/ping
---
kind: Service
apiVersion: v1
metadata:
  name: grades-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "grades-config"}'
spec:
  type: NodePort
  selector:
    app: grades
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31085
