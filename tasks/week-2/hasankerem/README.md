## How to Setup

- git clone git@github.com:kodekloudhub/certified-kubernetes-administrator-course.git
  - this repository contains code to setup up all the necessary VMs and the connection between them.
- cd certified-kubernetes-administrator-course/kubeadm-clusters/virtualbox

- vagrant up

  - this will create the VMs and setup the connection between them.

- Then go to singlepod or multiplepods directory to create the pods as you need.

- bash transfer.sh

  - this will transfer the files to the VMs.

- vargrant ssh controlplane

- bash controlplane.sh

  - this will initialize the controlplane node.

- vargrant ssh node01

- bash worker.sh

  - this will initialize the node01 node.

- Then run "kubeadm token create --print-join-command" on controlplane node and run the output on node01 node using sudo.

- Then run "apply-autoscaling.sh" or "apply-no-autoscaling.sh" on controlplane as wish.

- If you run "apply-autoscaling.sh" and you want to run "apply-no-autoscaling.sh" then you need to delete the artifacts created by "apply-autoscaling.sh" first.

- If you run "apply-no-autoscaling.sh" and you want to run "apply-autoscaling.sh" then you need to delete the artifacts created by "apply-no-autoscaling.sh" first.
