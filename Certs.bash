openssl req -x509 -nodes -days 365 \
  -newkey rsa:4096 \
  -keyout certs/localhost.key \
  -out certs/localhost.crt \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
