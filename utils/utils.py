import jwt
import uuid
from settings import settings


def encodeJwtToken(payload):
    data = payload.copy()
    data['iss'] = settings['jwt_iss']
    encode = jwt.encode(
            payload=data,
            **settings["jwt_token_config"]
            )

    return encode

def decodeJwtToken(encoded):
    decode = jwt.decode(
            jwt=encoded,
            **settings["jwt_token_config"]
            )
    return decode


def encodeJWTSessionToken(session_type, session_id, other_info, scopes, uid):
    payload = dict(
            session_type=session_type,
            session_id=session_id,
            other_info=other_info,
            scopes=scopes,
            uid=uid
            )
    return encodeJwtToken(payload)

def decodeJWTSessionToken(encoded):
    return decodeJwtToken(encoded)


def hash_plain_pwd(pwd, key):
    return str(uuid.uuid3(uuid.UUID(key), pwd))

def get_user_uuid(data):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, name=data.encode('utf8')))

def check_user_password(request_password, storage_password):
    has_pwd = hash_plain_pwd(request_password, settings['password_encode_key'])
    if str(has_pwd) == str(storage_password):
        return True
    return False

# todo
def check_session_valid(session):
    if session['status'] == '0':
        return False
    return True


# todo
def generate_native_session_key(data):
    return "native_session_key" + data
# todo
def generate_pwd_for_wx_user(openid):
    return str(uuid.uuid1())




def get_username_by_wxopenid(openid):
    return "wx_user_"+openid
