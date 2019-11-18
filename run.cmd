set PROJECTNAME="projectname"
set GCP-PROJECT-ID="gcp-project-id"
set SERVICE="service"
docker build --rm -f "Dockerfile" -t %PROJECTNAME%:dev .
docker run -it -v %CD%\code:/code -p 8080:8080 --name %PROJECTNAME% %PROJECTNAME%:dev
docker exec -it %PROJECTNAME% /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
docker build --rm -f "Dockerfile.production" -t %PROJECTNAME%:prod .
docker tag %PROJECTNAME%:prod gcr.io/%GCP-PROJECT-ID%/%SERVICE%
docker push gcr.io/gcr.io/%GCP-PROJECT-ID%/%SERVICE%