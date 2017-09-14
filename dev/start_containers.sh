docker pull neo4j
docker run --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data neo4j &
docker build -t level-15-dev .
docker run -d --name level-15 -p 80:80 level-15-dev
