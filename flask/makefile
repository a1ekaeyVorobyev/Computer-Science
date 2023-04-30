all:
	flask run --host=0.0.0.0
dockerbuild:
	sudo docker image build -t flask_docker .
dockerrun:
	 sudo docker run -p 5000:5000 -d flask_docker
compose:
	docker compose up -d
dockerstop:
	docker ps -q --filter ancestor=flask_docker | xargs docker stop