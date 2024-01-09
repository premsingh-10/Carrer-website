from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_World():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                jobs=jobs, 
                  company_name='Job Portal')




@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


# @app.route("/job/<id>")
# def show_job(id):
#   job = load_job_from_db(id)
#   return jsonify(job)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "Not Found", 404

  return render_template('jobpage.html', 
                         job=job)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
