# KubeHelper 🛠️  
A simple **Python wrapper for kubectl**, making it easier to interact with Kubernetes clusters.

## 🚀 Features
- **Get cluster information** (nodes, pods)
- **Describe pods** for troubleshooting
- **Fetch logs from a pod**
- **Apply YAML manifests**
- **Delete pods easily**
- **Works as a CLI tool**

---

## 📌 Installation
### 1️⃣ Install from Source
Clone the repository and install locally:
```bash
git clone https://github.com/icordus/kubehelper.git
cd kubehelper
pip install .
```
## Running kubehelper.py
```bash
./kubehelper.py get-nodes
./kubehelper.py get-pods -n kube-system
./kubehelper.py describe-pod my-pod -n default
./kubehelper.py get-logs my-pod -n default
./kubehelper.py apply my-deployment.yaml
./kubehelper.py delete-pod my-pod -n default
```
