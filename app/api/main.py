import requests
from flask import Flask, request, jsonify, Blueprint, current_app
from flask_cors import CORS
from .utils import apiRequest
import json
from . import api_bp

#
# Nodes
#
# List nodes
@api_bp.get('/v1/nodes')
def get_nodes():
    response, status_code = apiRequest("/api/v1/nodes", "GET")
    return jsonify(response), status_code

# Get node by name
@api_bp.get('/v1/nodes/<node_name>')
def get_node(node_name):    
    response, status_code = apiRequest(f"/api/v1/nodes/{node_name}", "GET")
    return jsonify(response), status_code


# Get metrics for all nodes
@api_bp.get('/v1/nodes/metrics')
def get_node_metrics():
    response, status_code = apiRequest("/apis/metrics.k8s.io/v1beta1/nodes", "GET")
    return jsonify(response), status_code

#
# Namespaces
#
# List namespaces
@api_bp.get('/v1/namespaces')
def get_namespaces():
    response, status_code = apiRequest("/api/v1/namespaces", "GET")
    return jsonify(response), status_code

# Get namespace by name
@api_bp.get('/v1/namespaces/<namespace_name>')
def get_namespace(namespace_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}", "GET")
    return jsonify(response), status_code

# Create a new namespace
@api_bp.post('/v1/namespaces')
def create_namespace():
    data = request.get_json()
    response, status_code = apiRequest("/api/v1/namespaces", "POST", data)
    return jsonify(response), status_code

# Delete a namespace
@api_bp.delete('/v1/namespaces/<namespace_name>')
def delete_namespace(namespace_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}", "DELETE")
    return jsonify(response), status_code

#
# Pods
#
#List all pods
@api_bp.get('/v1/pods')
def get_all_pods():
    response, status_code = apiRequest("/api/v1/pods", "GET")
    return jsonify(response), status_code

# List all pods in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/pods')
def get_pods(namespace_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/pods", "GET")
    return jsonify(response), status_code

# Get pod by name in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/pods/<pod_name>')
def get_pod(namespace_name, pod_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/pods/{pod_name}", "GET")
    return jsonify(response), status_code

# Create a new pod
@api_bp.post('/v1/namespaces/<namespace_name>/pods')
def create_pod(namespace_name):
    data = request.get_json()
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/pods", "POST", data)
    return jsonify(response), status_code

# Delete a pod
@api_bp.delete('/v1/namespaces/<namespace_name>/pods/<pod_name>')
def delete_pod(namespace_name, pod_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/pods/{pod_name}", "DELETE")
    return jsonify(response), status_code


#
# Deployments
#
# List all deployments
@api_bp.get('/v1/deployments')
def get_deployments():
    response, status_code = apiRequest("/apis/apps/v1/deployments", "GET")
    return jsonify(response), status_code

# List all deployments in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/deployments')
def get_deployments_in_namespace(namespace_name):
    response, status_code = apiRequest(f"/apis/apps/v1/namespaces/{namespace_name}/deployments", "GET")
    return jsonify(response), status_code

# Get deployment by name in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/deployments/<deployment_name>')
def get_deployment(namespace_name, deployment_name):
    response, status_code = apiRequest(f"/apis/apps/v1/namespaces/{namespace_name}/deployments/{deployment_name}", "GET")
    return jsonify(response), status_code

# Create a new deployment
@api_bp.post('/v1/namespaces/<namespace_name>/deployments')
def create_deployment(namespace_name):
    data = request.get_json()
    response, status_code = apiRequest(f"/apis/apps/v1/namespaces/{namespace_name}/deployments", "POST", data)
    return jsonify(response), status_code

# Delete a deployment
@api_bp.delete('/v1/namespaces/<namespace_name>/deployments/<deployment_name>')
def delete_deployment(namespace_name, deployment_name):
    response, status_code = apiRequest(f"/apis/apps/v1/namespaces/{namespace_name}/deployments/{deployment_name}", "DELETE")
    return jsonify(response), status_code


#
# Services
#
# List all services
@api_bp.get('/v1/services')
def get_services():
    response, status_code = apiRequest("/api/v1/services", "GET")
    return jsonify(response), status_code

# List all services in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/services')
def get_services_in_namespace(namespace_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/services", "GET")
    return jsonify(response), status_code

# Get service by name in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/services/<service_name>')
def get_service(namespace_name, service_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/services/{service_name}", "GET")
    return jsonify(response), status_code

# Create a new service
@api_bp.post('/v1/namespaces/<namespace_name>/services')
def create_service(namespace_name):
    data = request.get_json()
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/services", "POST", data)
    return jsonify(response), status_code

# Delete a service
@api_bp.delete('/v1/namespaces/<namespace_name>/services/<service_name>')
def delete_service(namespace_name, service_name):
    response, status_code = apiRequest(f"/api/v1/namespaces/{namespace_name}/services/{service_name}", "DELETE")
    return jsonify(response), status_code

#
# Ingress
#
# List all ingress
@api_bp.get('/v1/ingress')
def get_ingress():
    response, status_code = apiRequest("/apis/networking.k8s.io/v1/ingresses", "GET")
    return jsonify(response), status_code

# List all ingress in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/ingress')
def get_ingress_in_namespace(namespace_name):
    response, status_code = apiRequest(f"/apis/networking.k8s.io/v1/namespaces/{namespace_name}/ingresses", "GET")
    return jsonify(response), status_code

# Get ingress by name in a namespace
@api_bp.get('/v1/namespaces/<namespace_name>/ingress/<ingress_name>')
def get_ingress_by_name(namespace_name, ingress_name):
    response, status_code = apiRequest(f"/apis/networking.k8s.io/v1/namespaces/{namespace_name}/ingresses/{ingress_name}", "GET")
    return jsonify(response), status_code

# Create a new ingress
@api_bp.post('/v1/namespaces/<namespace_name>/ingress')
def create_ingress(namespace_name):
    data = request.get_json()
    response, status_code = apiRequest(f"/apis/networking.k8s.io/v1/namespaces/{namespace_name}/ingresses", "POST", data)
    return jsonify(response), status_code

# Delete a ingress
@api_bp.delete('/v1/namespaces/<namespace_name>/ingress/<ingress_name>')
def delete_ingress(namespace_name, ingress_name):
    response, status_code = apiRequest(f"/apis/networking.k8s.io/v1/namespaces/{namespace_name}/ingresses/{ingress_name}", "DELETE")
    return jsonify(response), status_code