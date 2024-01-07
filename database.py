from sqlalchemy import create_engine,text

db_connection_string = "mysql+pymysql://dq52is35mfvpow3uvjas:pscale_pw_aUfz2Vw4e0Daklh1PZ5fkqhcTcQrsLXBiLG6OEe5mBY@aws.connect.psdb.cloud/career-project?charset=utf8mb4"

engine = create_engine(
db_connection_string, 
connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})




def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

