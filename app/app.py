import jwt
import time

# Substitua pelos seus valores
app_id = '1028733'
private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqsPLI/hO0DanfWaX4VnGGUhs2/XAvkWRzdXkt2FHO3I4B8oI
XPjJWJmIiM1AJc9Ws/EYSRSDX7OxO/n42SfNT1/LbO8KJ8Gar74yHK0KPrOcK/VG
T+qsfHv8naxvvfGLKB8xt4XW3VjqryY0Kc/HrYzq9f0/mVIiSCFpRFA8s+Wo78KY
ldGA/llg9To5emp95+BKJJ3UIA1am/s9LRao5Bm6fajGlTxlhhhGzNdpCD9fFDRs
FYE55zsYRPZr5wGazLgsofKtsa7l8s5TjgIfTdXzfB4WmvhsSO8YgJGv1b0CJdKo
2rVOs64CfHmDC3KpuE5JVk3Ox39Fq6hveB9XrwIDAQABAoIBAQCJm7X7ioGYcDKQ
bzg9NObaQO7YYjWsHsvcH11sGUwZr3VPcZNDuIgoibDo7N2gmnC4GLUFTy5+1IMi
XdIWzGg6amu3oPmCCBXrQU2Ipjj3Ri23jrPWern8pr1vIiH54sfM0TZzObtoK9sS
waqPdwzl4gUFrcqudu2BSstVbYM9Q6eiZ0ekI5UCyBLrDBB2PT+EFVz6Erc4sZQ5
uHf2IneWuejX4j+YOnhSU+okPt2bxgZP62uixF/BwtL5LmAQ/24FrIUG2kXsvzbV
j6l4+1nGA6+hUafQRUgIrV/G677305LG2EYLL7pfnqpAjM0+c6kaneWey5Q2QhOY
t3Ol76OBAoGBANkzkA0aVD+b/QxMuXKZaTkgKUvuzL8XLDa4L68MsliJETngyALA
duUPMIf5Ef6YQq0+bd6yL4c+rDWGAfFvv6++vQUn2SphrpXXJU8fxpz7LkWYX/g4
a89T8k6sThfqFBTsj8doSV7kzj1FkTrDTnqfqQqlfOBay41wfuE+OjUxAoGBAMlE
uXKC8Em108z+cT+MV4soXgxPJBUdd54u2UFjuE0NuEo8YXSwwU+eTbtp9STQ9Lco
YtCP5UddpNTEGyeKNBkjX/KB/p2q6cjI5MLaIZdfj7SwwucEvMZ14dqoaD/4wT92
XL3yhQnj4yeK6EsE88U83rbdGJSaeDk8SqHhYqLfAoGAWK1xobffL707Gjt093Hl
APq9gY/0rgwC9DBM35Y6dmU30D6SynTT1f9WnB03mI+HoX28k9CCESCoZI3a2zz5
sQIZ4DH9uwz4n5qgU+awS0VOBgIJJKm8coBejHpSw/bAzi4rIYnVctXN0jxF6Az3
TJ9E/+DC1EKdmpiUZNfoIfECgYBXh0iy8Ri4pZePndP4U/s6bHrCFaTWffMoWq1m
z4w2DlJoDmw/iCL5khmx+HmA4lKaWLjohLusVqA5W3OHtYXErOqsFzZ4sPxsslky
GBTltMxVQ03vk9LY6Ckpo3V65J5+D+ZzQMX0sCN4beNpxKSS0U717Z8j+S1xjrPS
RKdVtwKBgCBkpzaIB1u7DBdwUkrOjh52GzWTb181C9uZvj47xVWrfE+OU5o6a8zN
RMIWWBeguUM9huIL/aFXdqg9R60rDUdYK4KLOG4ZmlkA+/Xm9FRoWitE9CprpgGL
Ao44p9DpCYfVPSCJZJjiHH8UGBDH0X7PLKsE5HF8CPqWtTVj6L1W
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