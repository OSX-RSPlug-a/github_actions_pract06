import jwt
import time

# Substitua pelos seus valores
app_id = '<APPID>'
private_key = """-----BEGIN RSA PRIVATE KEY-----

-----END RSA PRIVATE KEY-----"""

# Gerar o token JWT
payload = {
    # Emitido em (iat) e expiração (exp) em segundos desde a época Unix
    'iat': int(time.time()) - 60,
    'exp': int(time.time()) + (10 * 60),
    'iss': app_id
}

jwt_token = jwt.encode(payload, private_key, algorithm='RS256')

print(jwt_token)
