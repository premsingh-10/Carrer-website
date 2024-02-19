from sqlalchemy import create_engine,text
from sqlalchemy import text
import os

# export DB_CONNECTION_STRING="mysql+pymysql://msoo10ziruq0f80en0wf:pscale_pw_z1diBkSynlj5s4v1KvB2FzlMeP7iQP1f5G27zEZ01Vd@aws.connect.psdb.cloud/careerproject?charset=utf8mb4"
db_connection_string = "mysql+pymysql://msoo10ziruq0f80en0wf:pscale_pw_z1diBkSynlj5s4v1KvB2FzlMeP7iQP1f5G27zEZ01Vd@aws.connect.psdb.cloud/careerproject?charset=utf8mb4"


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


def load_job_from_db(id):
  with engine.connect() as conn:
      query = text("select * from jobs where id = :val").bindparams(val=id)
      result = conn.execute(query)
      row = result.first()

      if row is None:
          return None
      else:
          return row._asdict()



def add_application_to_db(job_id, data):
  with engine.connect() as conn:
      query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

      # Use a dictionary to pass parameters to the execute method.
      params = {
          'job_id': job_id,
          'full_name': data['full_name'],
          'email': data['email'],
          'linkedin_url': data['linkedin_url'],
          'education': data['education'],
          'work_experience': data['work_experience'],
          'resume_url': data['resume_url']
      }

      # Bind the parameters using bindparams()
      query = query.bindparams(**params)

      conn.execute(query)



def adminData():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications,jobs"))
        applications = [row._asdict() for row in result.all()]
    return applications