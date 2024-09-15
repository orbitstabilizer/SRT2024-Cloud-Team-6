kubectl apply -f complex-frontend-deployment-autoscaling.yaml 
kubectl apply -f complex-backend-deployment-autoscaling.yaml 
kubectl apply -f complex-app-different-pods-ingress.yaml 
kubectl apply -f complex-app-different-pods-service.yaml 
kubectl apply -f complex-frontend-hpa.yaml 
kubectl apply -f complex-backend-hpa.yaml 
kubectl apply -f ingress-nginx-nodeport.yaml 