let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.requests
      python-pkgs.flask
      python-pkgs.flask-cors
      python-pkgs.flask-sqlalchemy
      python-pkgs.flask-login
      python-pkgs.cryptography
      python-pkgs.python-dotenv
    ]))
    pkgs.openssl
  ];
}

