import pymysql
import credential


def user_signup(user_name,email,password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "insert into usermaster (user_name,email,user_password,user_confirmation) value (%s,%s,%s,%s)"
            curr.execute(sql,(user_name,email,password,"1"))
            conn.commit()
    except Exception as e:
        print(e)



def login(email,password):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql = "select user_password from usermaster where email=(%s)"
            curr.execute(sql,email)
            output = curr.fetchone()
            if (output):
                if password==output[0]:
                    return "correct_password"
                else:
                    return "wrong_password"
            return 'username_dosenot_exist'    
    except Exception as e:
        print(e)