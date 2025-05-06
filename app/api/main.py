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

# Create a new namespace
@api_bp.post('/v1/namespaces')
def create_namespace():
    data = request.get_json()
    response, status_code = apiRequest("/api/v1/namespaces", "POST", data)
    return jsonify(response), status_code

#
# Deployments
#
# List all deployments
@api_bp.get('/v1/deployments')
def get_deployments():
    response, status_code = apiRequest("/apis/apps/v1/deployments", "GET")
    return jsonify(response), status_code

# Create a new deployment
@api_bp.post('/v1/namespaces/<namespace_name>/deployments')
def create_deployment(namespace_name):
    data = request.get_json()
    response, status_code = apiRequest(f"/apis/apps/v1/namespaces/{namespace_name}/deployments", "POST", data)
    return jsonify(response), status_code

#
# Pods
#
# List all pods
@api_bp.get('/v1/pods')
def get_all_pods():
    response, status_code = apiRequest("/api/v1/pods", "GET")
    return jsonify(response), status_code