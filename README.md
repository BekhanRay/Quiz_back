Hello talents !
Let me show my Quiz project
First of all you need to lounch project 
if you have Linux/Mac :
```
docker compose -f docker/docker-compose.yaml -f docker/dev/docker-compose-dev.yaml up —build -d
```
this method match you if you have Windows with downloaded Docker engine
If you were not downloaded yet i beg to get it.
Also command for admin creation (only if you lounched app via docker-compose) :
```
 docker exec -it backend python3 manage.py createsuperuser
```
and put your data

I wish it was helpful 
