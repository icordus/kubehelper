Running kubehelper.py

./kubehelper.py get-nodes
./kubehelper.py get-pods -n kube-system
./kubehelper.py describe-pod my-pod -n default
./kubehelper.py get-logs my-pod -n default
./kubehelper.py apply my-deployment.yaml
./kubehelper.py delete-pod my-pod -n default
