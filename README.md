# lti-k3s-python

**⚠️ Warning:** This code is an academic project and is not intended for production use.

A Flask-based backend/middleware to control and interact with a Kubernetes (K3s) cluster via a REST API.

**Note:** This backend is designed to be used together with the [lti-k3s frontend](https://github.com/rodrigo-gom3s/lti-k3s) project.

## Features

- Cluster authentication with encrypted tokens
- CRUD operations for Kubernetes resources:
  - Nodes (list, metrics)
  - Namespaces
  - Pods
  - Deployments
  - Services
  - Ingresses
- Auto-login and token management
- SQLite database for token storage


## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/lti-k3s-python.git
   cd lti-k3s-python
   ```

2. **Install dependencies:**
   - With virtualenv:
     ```sh
     python3 -m venv venv
     source venv/bin/ctivate
     pip install -r requirements.txt
     ```
   - Or with Nix:
     ```sh
     nix-shell
     ```

3. **Set environment variables:**
   - Create a [`.env`](.env ) file with:
     ```
     SECRETKEY=your_fernet_key
     ```
   - Generate a Fernet key with:
     ```python
     from cryptography.fernet import Fernet
     print(Fernet.generate_key().decode())
     ```

4. **Run the application:**
   ```sh
   flask run
   ```

## API Endpoints

- **Authentication**
  - `POST /api/login` — Login with cluster IP and token
  - `POST /api/autoLogin` — Auto-login with stored token
  - `GET /api/logout` — Logout
  - `GET /api/users` — List users

- **Kubernetes Resources**
  - `GET /api/v1/nodes` — List nodes
  - `GET /api/v1/nodes/metrics` — Node metrics
  - `GET /api/v1/namespaces` — List namespaces
  - `POST /api/v1/namespaces` — Create namespace
  - `DELETE /api/v1/namespaces/<namespace_name>` — Delete namespace
  - ...and more for pods, deployments, services, ingress

See [app/api/main.py](app/api/main.py) and [app/api/auth.py](app/api/auth.py) for full details.

## License

MIT License — see [LICENSE](LICENSE) for details.