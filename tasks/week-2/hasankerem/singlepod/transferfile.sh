vagrant scp complex-app-same-pod-autoscaling.yaml controlplane:/home/vagrant/
vagrant scp complex-app-same-pod-no-autoscaling.yaml controlplane:/home/vagrant
vagrant scp complex-app-service.yaml controlplane:/home/vagrant/
vagrant scp ingress-nginx-nodeport.yaml controlplane:/home/vagrant/
vagrant scp ingress.yaml controlplane:/home/vagrant/
vagrant scp controlplane.sh controlplane:/home/vagrant/
vagrant scp complex-app-hpa.yaml controlplane:/home/vagrant
vagrant scp worker.sh node01:/home/vagrant/
vagrant scp apply-noautoscaling.sh controlplane:/home/vagrant/
vagrant scp apply-autoscaling.sh controlplane:/home/vagrant/

