[![Docker Image CI](https://github.com/yannoleon/helloworld_gcp_build_deploy/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yannoleon/helloworld_gcp_build_deploy/actions/workflows/docker-image.yml)

# GCP_app_CICD_sandbox

Sandbox project to do CI/CD in python and deploy flask or fastapi app on GCP.

On Github:
* Check in actions the CI with test (format, lint and pytest) runs as implemented in the yml file.

On GCP:
* Manual debug deploy:
  * Clone this project in your gcp project
  * In the cloud shell vscode editor launch cloud run (deploy to cloud run) and set the build to the docker file
  
* Automatic deploy:
  * From the cloud run interface, link your repo and set the build to your Docker file
  * Set the Continuous Integration so that the deployment is automatic given a trigger (like a new push on the repo)
  
* Once the app is deployed run the request_remote.py file to check you can access the api remotely 
