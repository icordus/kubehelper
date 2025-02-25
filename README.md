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
### 1️⃣ Install via pip (After Publishing to PyPI)
```bash
pip install kubehelper
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
