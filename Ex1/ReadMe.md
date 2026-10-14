# Exercise 1 — Hello Pod

## Objective
Deploy an Nginx Pod on Kubernetes using Minikube and expose it through a NodePort Service.

## Environment
- Operating System: Windows 10 Pro
- Kubernetes cluster: Minikube
- Container runtime: Docker Desktop
- Application: Nginx

## Implementation

### 1. Start the Minikube cluster
```bash
minikube start --driver=docker
```

### 2. Create the Nginx Pod
```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
kubectl get pod hello-k8s --show-labels
```

### 4. Expose the Pod
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Service
```bash
kubectl get services
```

### 6. Access the application
```bash
minikube service hello-k8s
```

The Nginx welcome page was accessed through the exposed Service.

## Configuration Files
- `pod.yaml` — declarative configuration for the Nginx Pod.
- `service.yaml` — declarative configuration for the NodePort Service.


## Result
Successfully deployed an Nginx Pod on Kubernetes and exposed it using a NodePort Service.

## Key Learnings
- A Pod is the smallest deployable unit in Kubernetes.
- A Service provides a stable endpoint for accessing Pods.
- NodePort exposes a Service on a port of the Kubernetes node.
- YAML manifests allow Kubernetes resources to be defined declaratively and recreated.
