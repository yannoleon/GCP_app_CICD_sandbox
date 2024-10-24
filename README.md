[![Docker Image CI](https://github.com/yannoleon/helloworld_gcp_build_deploy/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yannoleon/helloworld_gcp_build_deploy/actions/workflows/docker-image.yml)

# helloworld_gcp_build_deploy

Sandbox project to deploy flask of fastapi python api on gcp.

Manual debug deploy:
* Clone this project in your gcp project
* In the cloud shell vscode editor launch cloud run (deploy to cloud run) and set the build to the docker file
  Automatic deploy:
* From the cloud run interface, link your repo and set the build to your Docker file
* Set the Continuous Integration so that the deployment is automatic given a trigger (like a new push on the repo)
  
* Once the app is deployed run the request_remote.py file to check you can access the api remotely 
