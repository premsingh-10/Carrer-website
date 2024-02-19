from sqlalchemy import create_engine,text
from sqlalchemy import text
import os


db_connection_string = os.environ['DB_CONNECTION_STRING']

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
    query = text("select * from application")
    result = conn.execute(query)
    application = []
    for row in result.all():
      application.append(row._asdict())
    return application
  