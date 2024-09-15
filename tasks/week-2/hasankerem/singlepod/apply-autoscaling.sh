kubectl apply -f complex-app-same-pod-autoscaling.yaml
kubectl apply -f complex-app-service.yaml 
kubectl apply -f ingress-nginx-nodeport.yaml 
kubectl apply -f ingress.yaml 
kubectl apply -f complex-app-hpa.yaml 