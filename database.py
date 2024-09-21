from sqlalchemy import create_engine,text
import os 
# from dotenv import load_dotenv
# load_dotenv()

# passkey = os.environ["CLOUD_PASSWORD"]
# db_cred=f"mysql+mysqlconnector://avnadmin:{passkey}@mysql-3fe3b451-learning-flask.j.aivencloud.com:14195/defaultdb?charset=utf8mb4"
db_cred  =f"mysql+mysqlconnector://root:Ansh_kesari321@localhost:3306/doctor?charset=utf8mb4"
engine = create_engine(db_cred,echo=True)

def load_doctor_details():
    with engine.connect() as conn:
        result = conn.execute(text("select * from doctor_availability"))
        rows = result.fetchall()
        res=[]
        print(rows)
        for row in rows:
            res.append(row._mapping)
        print(res)
        return res
def load_queries():
    with engine.connect() as conn:
        result = conn.execute(text("select * from issues"))
        rows = result.fetchall()
        res=[]
        for row in rows:
            res.append(row._mapping)
        return res
# print(load_admin_details())
# def send_query_to_list(name,email,number,subject,issue,link):
        