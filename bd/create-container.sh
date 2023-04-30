sudo docker stop ct-kallistra-db
sudo docker rm ct-kallistra-db
sudo docker rmi kallistra/db

sudo docker build -t kallistra/db .
sudo docker run --name ct-kallistra-db -d -p 3306:3306 --network kallistra-network -e MYSQL_ROOT_PASSWORD=urubu100 -e MYSQL_DATABASE=kallistra kallistra/db
