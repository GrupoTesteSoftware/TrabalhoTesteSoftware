$containerName = "flaskcontainer"

docker stop $containerName
docker rm $containerName
docker build -t flaskimage .
docker run --name $containerName -p 7776:7776 flaskimage
