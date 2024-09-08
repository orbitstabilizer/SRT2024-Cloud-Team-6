
# Install Kubernetes

Following this [tutorial](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)  to install `kubeadm`:

- `kubeadm` requires [linux](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin): 
```bash
# set-up two multipass ubuntu VMs (1 master, 1 worker)
# minimum requirement is 2 GB of memory and 2 CPUs 

multipass launch --name master --cpus 2 --memory 2048M --disk 5G
multipass launch --name worker --cpus 2 --memory 2048M --disk 5G

multipass mount . master:/home/ubuntu/src/

multipass shell master


multipass launch --name kube-master --cpus 6 --memory 4096M --disk 20G
multipass shell kube-master
```
(All steps below assume you have a linux machine)

- `kubeadm` requires swap to be disabled for some reason: 
> You MUST disable swap if the kubelet is not properly configured to use swap. For example, sudo swapoff -a will disable swapping temporarily. To make this change persistent across reboots, make sure swap is disabled in config files like /etc/fstab, systemd.swap, depending how it was configured on your system

[best way to disable swap on linux](https://serverfault.com/questions/684771/best-way-to-disable-swap-in-linux)



- [assuming unique MAC address per node](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#verify-mac-address) 

- [check required ports](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#check-required-ports) 
Running `nc 127.0.0.1 6443 -v` outputs `Port 6443 connection refused`, this is because we haven't set-up kubeadm yet and there is no service listening on that port.
Check this [post](https://stackoverflow.com/questions/70571312/port-6443-connection-refused-when-setting-up-kubernetes)

- We need a [container runtime](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime) to run containers in pods
- We will use [CRI-O](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#cri-o)
[Install CRI-O](https://github.com/cri-o/packaging/blob/main/README.md#usage)

KUBERNETES_VERSION=v1.31
CRIO_VERSION=v1.30

curl -fsSL https://pkgs.k8s.io/core:/stable:/$KUBERNETES_VERSION/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/$KUBERNETES_VERSION/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list

curl -fsSL https://pkgs.k8s.io/addons:/cri-o:/stable:/$CRIO_VERSION/deb/Release.key |sudo gpg --dearmor -o /etc/apt/keyrings/cri-o-apt-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/cri-o-apt-keyring.gpg] https://pkgs.k8s.io/addons:/cri-o:/stable:/$CRIO_VERSION/deb/ /" | sudo tee /etc/apt/sources.list.d/cri-o.list

sudo apt-get update

sudo apt-get install -y cri-o kubelet kubeadm kubectl

sudo systemctl start crio.service


swapoff -a
sudo modprobe br_netfilter
# consider adding this to /etc/sysctl.conf
sudo sysctl -w net.ipv4.ip_forward=1
sudo sysctl -p

# to bootstrap the clustre
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubeadm join 192.168.64.8:6443 --token zorswp.mzeokhyjiwi0ufu5 \
	--discovery-token-ca-cert-hash sha256:2b91825a72e946fad6ed1230e56fc3a745b2411851fb69250af162422cc1083b




#ingress
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install my-ingress ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace



NAME: my-ingress
LAST DEPLOYED: Sat Sep  7 15:40:49 2024
NAMESPACE: ingress-nginx
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The ingress-nginx controller has been installed.
It may take a few minutes for the load balancer IP to be available.
You can watch the status by running 'kubectl get service --namespace ingress-nginx my-ingress-ingress-nginx-controller --output wide --watch'

An example Ingress that makes use of the controller:
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: example
    namespace: foo
  spec:
    ingressClassName: nginx
    rules:
      - host: www.example.com
        http:
          paths:
            - pathType: Prefix
              backend:
                service:
                  name: exampleService
                  port:
                    number: 80
              path: /
    # This section is only required if TLS is to be enabled for the Ingress
    tls:
      - hosts:
        - www.example.com
        secretName: example-tls

If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

  apiVersion: v1
  kind: Secret
  metadata:
    name: example-tls
    namespace: foo
  data:
    tls.crt: <base64 encoded cert>
    tls.key: <base64 encoded key>
  type: kubernetes.io/tls



# locust
locust -f locustfile.py --host=http://pytime.local:30371/
