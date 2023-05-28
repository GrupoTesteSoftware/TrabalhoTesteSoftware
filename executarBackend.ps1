$containerName = "flaskcontainer"

docker stop $containerName
docker rm $containerName
docker build -t flaskimage .
docker run --name $containerName -p 5000:5000 flaskimage
