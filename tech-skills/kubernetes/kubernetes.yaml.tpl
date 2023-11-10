apiVersion: apps/v1
kind: Deployment
metadata:
  name: tech-skills
  labels:
    app: tech-skills
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tech-skills
  template:
    metadata:
      labels:
        app: tech-skills
    spec:
      containers:
      - name: tech-skills
        image: us-central1-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/abc-jobs-repository/tech-skills:COMMIT_SHA
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
  name: tech-skills-config
spec:
  healthCheck:
    checkIntervalSec: 30
    port: 3000
    type: HTTP
    requestPath: /tech-skills/ping
---
kind: Service
apiVersion: v1
metadata:
  name: tech-skills-microservice
  annotations:
    cloud.google.com/backend-config: '{"default": "tech-skills-config"}'
spec:
  type: NodePort
  selector:
    app: tech-skills
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
      nodePort: 31035
