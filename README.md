# study-meetup
Aplikacja webowa pozwalająca na umawianie się na wspólne odrabianie zadań i uczenie przed egzaminami i kolokwiami. Użytkownicy dołączają do grup np rocznikowej wybierają przedmioty. Można dodawać wydarzenia np kolokwia a następnie proponowane terminy spotkań. Użytkownicy mogą oznaczać że dany termin im pasuje.

Technologie:
Django
Postgres
Bootstrap
VPS

Mateusz Furga
Błażej Nowicki

## Setup
```
docker-compose up
```

```
docker-compose run web python3 manage.py makemigrations catalog event
```

```
docker-compose run web python3 manage.py migrate
```

(optional) Adding mock data
```
docker-compose run web python ./add_mock_data.py
```

(optional) Creating superuser (admin panel available at /admin)
```
docker-compose run web python manage.py createsuperuser
```
