import subprocess
import argparse

class KubeHelper:
    """A Python wrapper for common kubectl commands"""

    def run_command(self, command):
        """Execute a shell command and return the output"""
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def get_nodes(self):
        return self.run_command("kubectl get nodes")

    def get_pods(self, namespace="default"):
        return self.run_command(f"kubectl get pods -n {namespace}")

    def describe_pod(self, pod_name, namespace="default"):
        return self.run_command(f"kubectl describe pod {pod_name} -n {namespace}")

    def get_logs(self, pod_name, namespace="default", container=None):
        cmd = f"kubectl logs {pod_name} -n {namespace}"
        if container:
            cmd += f" -c {container}"
        return self.run_command(cmd)

    def apply_manifest(self, file_path):
        return self.run_command(f"kubectl apply -f {file_path}")

    def delete_pod(self, pod_name, namespace="default"):
        return self.run_command(f"kubectl delete pod {pod_name} -n {namespace}")

def main():
    parser = argparse.ArgumentParser(description="KubeHelper: A simple wrapper for kubectl")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("get-nodes", help="List all Kubernetes nodes")

    pods_parser = subparsers.add_parser("get-pods", help="List all pods in a namespace")
    pods_parser.add_argument("-n", "--namespace", default="default", help="Namespace (default: default)")

    describe_parser = subparsers.add_parser("describe-pod", help="Describe a specific pod")
    describe_parser.add_argument("pod_name", help="Pod name")
    describe_parser.add_argument("-n", "--namespace", default="default", help="Namespace (default: default)")

    logs_parser = subparsers.add_parser("get-logs", help="Get logs from a pod")
    logs_parser.add_argument("pod_name", help="Pod name")
    logs_parser.add_argument("-n", "--namespace", default="default", help="Namespace (default: default)")
    logs_parser.add_argument("-c", "--container", help="Container name (optional)")

    apply_parser = subparsers.add_parser("apply", help="Apply a Kubernetes manifest")
    apply_parser.add_argument("file_path", help="Path to YAML file")

    delete_parser = subparsers.add_parser("delete-pod", help="Delete a specific pod")
    delete_parser.add_argument("pod_name", help="Pod name")
    delete_parser.add_argument("-n", "--namespace", default="default", help="Namespace (default: default)")

    args = parser.parse_args()
    kube = KubeHelper()

    if args.command == "get-nodes":
        print(kube.get_nodes())
    elif args.command == "get-pods":
        print(kube.get_pods(args.namespace))
    elif args.command == "describe-pod":
        print(kube.describe_pod(args.pod_name, args.namespace))
    elif args.command == "get-logs":
        print(kube.get_logs(args.pod_name, args.namespace, args.container))
    elif args.command == "apply":
        print(kube.apply_manifest(args.file_path))
    elif args.command == "delete-pod":
        print(kube.delete_pod(args.pod_name, args.namespace))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
