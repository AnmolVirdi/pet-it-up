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



def update(email):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )
    try:
        with conn.cursor() as curr:
            sql="update usermaster set email_confirmation=(%s) where email=(%s)"
            temp=2
            curr.execute(sql,(temp,email))
            conn.commit()
    except Exception as e:
        print(e)     

def mail_confirm(email):     
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql="select email_confirmation from usermaster where email=(%s)"
            curr.execute(sql,(email))
            output=curr.fetchone()
            if(output[0]=="2"): return True
            return False
            # conn.commit()
    except Exception as e:
        print(e)     

def delete(email):
    conn=pymysql.connect(
        host=credential.host,
        port=credential.port,
        user=credential.user,
        password=credential.password,
        db=credential.databasename
    )   
    try:
        with conn.cursor() as curr:
            sql="delete from usermaster where email=(%s)"
            curr.execute(sql,(email))
            conn.commit()
    except Exception as e:
        print(e)