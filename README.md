
## Run with virtualenv
- Create a virtualenv folder `virtualenv -p python3 venv`
- Activate `source venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Run gunicorn `gunicorn app:app --bind 0.0.0.0:5000 --reload`

## Run with Docker
- Build the image with `docker build -t project_dep .`
- Run the container with `docker run -d -p 5000:5000 -e PORT=5000 --name project-server project_dep`
- Check that the container is running
- Go to `localhost:5000`. Ready!!!! )

gcloud app deploy app.yaml    - deploy on google cloud
