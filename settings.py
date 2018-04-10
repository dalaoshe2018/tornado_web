settings = {
    "debug":True,  # open debug mode
    "mysql_config": dict( # mysql conn config
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        passwd='dalaoshe', 
        db='TEST'),
    "mysql_max_idle_connections": 1, # mysql conn config
    "mysql_max_recycle_sec":3,       # mysql conn config
    "jwt_token_config": dict(        # jwt encode/decode config
        key="qwertyuio..pl,;;0.1a",
        algorithm="HS256",
        ),
    "wx_login_config": dict(         # wx login config
            appid = "wx2f15bf881450b55a",
            secret = "17009cdbf79c0262a41faf43233a4bb1",
            grant_type = "authorization_code",
        ),
    "password_encode_key": '65555551-1111-1111-1111-111111111111', # password encode config 
    "jwt_iss": 'chaomy.auth', # password encode config 
}



