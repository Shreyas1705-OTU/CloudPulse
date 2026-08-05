#!/bin/bash

set -e

echo "========================================"
echo " CloudPulse Kubernetes Deployment"
echo "========================================"

echo ""
echo "[1/8] Building backend image..."
docker build -t cloudpulse-backend:latest ./backend

echo ""
echo "[2/8] Building frontend image..."
docker build -t cloudpulse-frontend:latest ./frontend

echo ""
echo "[3/8] Loading images into Kind..."
kind load docker-image cloudpulse-backend:latest --name cloudpulse
kind load docker-image cloudpulse-frontend:latest --name cloudpulse

echo ""
echo "[4/8] Creating namespace/config..."
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml

echo ""
echo "[5/8] Deploying PostgreSQL..."
kubectl apply -f k8s/postgres/

echo ""
echo "[6/8] Deploying backend/frontend..."
kubectl apply -f k8s/backend/
kubectl apply -f k8s/frontend/

echo ""
echo "[7/8] Deploying monitoring..."
kubectl apply -f k8s/monitoring/prometheus/
kubectl apply -f k8s/monitoring/grafana/

echo ""
echo "[8/8] Deploying ingress..."
kubectl apply -f k8s/ingress/

echo ""
echo "Waiting for all deployments..."

kubectl rollout status deployment/backend -n cloudpulse
kubectl rollout status deployment/frontend -n cloudpulse
kubectl rollout status deployment/prometheus -n cloudpulse
kubectl rollout status deployment/grafana -n cloudpulse

echo ""
echo "========================================"
echo " CloudPulse deployed successfully!"
echo "========================================"

echo ""
echo "Run database migrations:"
echo "kubectl exec -it deployment/backend -n cloudpulse -- alembic upgrade head"

echo ""
echo "Port forward Prometheus:"
echo "kubectl port-forward svc/prometheus 9090:9090 -n cloudpulse"

echo ""
echo "Port forward Grafana:"
echo "kubectl port-forward svc/grafana 3000:3000 -n cloudpulse"

echo ""
echo "Frontend:"
echo "http://localhost"

echo "Prometheus:"
echo "http://localhost:9090"

echo "Grafana:"
echo "http://localhost:3000"

echo ""
kubectl get pods -n cloudpulse
