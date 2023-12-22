import psycopg2
from . import render_password as rpw
from werkzeug.security import check_password_hash

#因為Email是唯一值，所以當使用者輸入已經申請過的Email註冊時，就會出現錯誤
#在insert前寫入try的檢查設定(優雅的錯誤)，不要讓整個程式因為這樣而crush
#使用Class Invold自訂錯誤

class InvolidEmailException(Exception):
    #繼承內建的Exception
    pass


#將使用者註冊資料存入資料庫(可以傳入任何內容型別的list，預設是None)
def insert_data(value:list[any] | None=None) -> None:
    conn = psycopg2.connect(database=rpw.DATABASE, 
                                user=rpw.USER, 
                                password=rpw.PASSWORD, 
                                host=rpw.HOST, 
                                port="5432") 
    cursor = conn.cursor()
    insert_sql='''
        INSERT INTO 使用者(
            "姓名", 
            "性別", 
            "聯絡電話", 
            "電子郵件", 
            "isGetEmail",
            "出生年月日", 
            "自我介紹", 
            "密碼", 
            "連線密碼"
        ) 
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
            )
                '''
    try:
        cursor.execute(insert_sql,value)
    except psycopg2.errors.UniqueViolation:
        raise InvolidEmailException
    except:
        raise RuntimeError
    conn.commit()
    cursor.close()
    conn.close()
    
def validateUser(email:str, password:str) -> tuple[bool,str]:
    conn = psycopg2.connect(database=rpw.DATABASE,
                                user=rpw.USER, 
                                password=rpw.PASSWORD,
                                host=rpw.HOST, 
                                port="5432")
    cursor = conn.cursor()
    sql = '''
        select 密碼,姓名
        from 使用者
        where 電子郵件 = %s
            '''
    cursor.execute(sql,[email])
    searchData:tuple[str, str]= cursor.fetchone() #傳出tuple(hash_password,name)
    hash_password, username = searchData
    is_ok:bool = check_password_hash(hash_password, password)
    cursor.close()
    conn.close()
    return (is_ok, username)