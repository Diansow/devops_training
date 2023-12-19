mongo-run:
	docker run --name some-mongo --network some-network -d mongo:7.0.3 
	docker run --network some-network -e ME_CONFIG_MONGODB_SERVER=some-mongo -p 8081:8081 mongo-express:1.0.0-20