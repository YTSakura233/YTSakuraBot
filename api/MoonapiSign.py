import hashlib
import hmac
from hashlib import sha1

def generateHmacSHA1Signature(parameters, accessKeySecret):
    signString = generateSignString(parameters, accessKeySecret)

    hmac_code = hmac.new(accessKeySecret.encode(), signString.encode(), sha1)
    
    return hmac_code.hexdigest()
    
def generateMd5Signature(parameters, accessKeySecret):
    signString = generateSignString(parameters, accessKeySecret)

    m = hashlib.md5()
    m.update(signString.encode())
    
    return m.hexdigest()

def generateSignString(parameters, accessKeySecret):
    arrString = []

    for (key,value) in parameters.items():
        arrString.append(key + "=" + str(value))

    arrString.sort()

    return "&".join(arrString) + ":" + accessKeySecret

def getUrlQueryFromParams(parameters):
    arrString = []

    for (key,value) in parameters.items():
        arrString.append(key + "=" + str(value))

    return "&".join(arrString)