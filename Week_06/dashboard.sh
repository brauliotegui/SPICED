wget https://downloads.metabase.com/v0.36.4/metabase.jar
sudo yum install java-1.8.0
screen
sudo java -jar -DMB_JETTY_PORT=80 metabase.jar
