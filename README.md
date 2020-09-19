# HSNetwork REST API Documentation

HSNetwork connect you with people of similar interest

## Features

- Register User & Login
- Token Based Authentication
- Interest based User Suggestion
- Following Other User and Get Updated of User
- Post an Update


## How to install

## Clone
```
$ git clone https://github.com/rahulkhairnarr/hsnetwork.git
```

## Setup Evniroment
Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
```
$ virtualenv project-env
$ source project-env/bin/activate
```

## Install Packages

```
$ cd hsnetwork
$ pip install -r requirements.txt
```

## Run the app

```
$ python manage.py runserver
```

# REST API

The REST API to perform specific acitivity

## Register User
Register/SignUp User

### Request

`POST /register/`

```
curl --location --request POST 'http://localhost:8000/register/' \
--form 'username=testuser' \
--form 'first_name=Test' \
--form 'last_name=User' \
--form 'email=testuser@test.com' \
--form 'password=123456!23' \
--form 'password_confirm=123456!23'
```

### Response

```
HTTP/1.1 201 CREATED
Date: Sat, 19 Sep 2020 04:11:58 GMT
Status: 201 CREATED
Content-Type: application/json

{
"id": 3,
"username": "testuser2",
"first_name": "Test",
"last_name": "User",
"email": "testuser2@test.com"
}
```

## Login and Get Token
Login User and Get Token. Use "access" token in header with JWT token in header with Authorization Key

Get Access Token and Refresh Token

### Request

`POST /token/`


    curl --location --request POST 'http://localhost:8000/token/' \
    --form 'username=testuser' \
    --form 'password=123456!23'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 200 OK
    Content-Type: application/json


    {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDU3NTM2NCwianRpIjoiODc3ZTRhMGQ2Y2MyNGExYmI1MDUxNTM0NmU5OGFjNzAiLCJ1c2VyX2lkIjoyfQ.8HjjLY_jUYlMMgCA3r3O2cTTaLQOPjMSDcd3s9IjJgc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ"
    }

## Get Interest List
Get List of Interest Store in System

### Request

`GET /interest/`

    curl --location --request GET 'http://localhost:8000/interest/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDU0MzE0LCJqdGkiOiJiZTg2OGMxMTZlMGE0YmFhYTZkZDJmM2IxYmU0YmIwYSIsInVzZXJfaWQiOjF9.dmrfDj-gbkzdLzVGkcemkEcjrSfJ1PaLGUSR6hM9NpY'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 200 OK
    Content-Type: application/json

    {
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "interest_id": 1,
            "interest_name": "#reactjs"
        },
        {
            "interest_id": 2,
            "interest_name": "#django"
        },
        {
            "interest_id": 3,
            "interest_name": "#mobiledevelopment"
        },
        {
            "interest_id": 4,
            "interest_name": "#angular"
        }
        ]
    }

## Create Interest
Add new interest to system

### Request

`POST /interest/`

    curl --location --request POST 'http://localhost:8000/interest/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDU0MzE0LCJqdGkiOiJiZTg2OGMxMTZlMGE0YmFhYTZkZDJmM2IxYmU0YmIwYSIsInVzZXJfaWQiOjF9.dmrfDj-gbkzdLzVGkcemkEcjrSfJ1PaLGUSR6hM9NpY' \
    --form 'interest_name=#markdown'

### Response

    HTTP/1.1 201 CREATED
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 201 CREATED
    Content-Type: application/json

    {
    "interest_id": 5,
    "interest_name": "#markdown"
    }

## Create User Profile
Create Profile 

### Request

`POST /userprofile/`

    curl --location --request POST 'http://localhost:8000/userprofile/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDU0MzE0LCJqdGkiOiJiZTg2OGMxMTZlMGE0YmFhYTZkZDJmM2IxYmU0YmIwYSIsInVzZXJfaWQiOjF9.dmrfDj-gbkzdLzVGkcemkEcjrSfJ1PaLGUSR6hM9NpY' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "about_us":"Sr. Backend Developer",
        "user_interest":[1,2,3]
    }'

### Response

    HTTP/1.1 201 CREATED
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 201 CREATED
    Content-Type: application/json

    {
    "id": 3,
    "about_us": "Sr. Backend Developer",
    "user_interest": [
        1,
        2,
        3 ]
    }

## Get User Profile
Get User Profile

### Request

`GET /userprofile/`

    curl --location --request GET 'http://localhost:8000/userprofile/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 200 OK
    Content-Type: application/json

    {
    "id": 3,
    "about_us": "Sr. Backend Developer",
    "user": 2,
    "user_interest": [
        1,
        2,
        3 ]
    }


## Find Poeple
Get List of People based on common Interest

### Request

`GET /people-suggestion/`

    curl --location --request GET 'http://localhost:8000/people-suggestion/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 200 OK
    Content-Type: application/json

    {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "username": "admin"
        }
    ]
    }


## Follow User
Follow User using user id get in suggest people API

### Request

`POST /follow/`

    curl --location --request POST 'http://localhost:8000/follow/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ' \
    --form 'following=1'

### Response

    HTTP/1.1 201 CREATED
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 201 CREATED
    Content-Type: application/json

    {
    "id": 3,
    "following": 1
    }

## Get Following List
Get List of People you are following

### Request

`GET /get-following-list/`

    curl --location --request GET 'http://localhost:8000/get-following-list/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:11:58 GMT
    Status: 200 OK
    Content-Type: application/json

    {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "username": "admin"
        }
    ]
    }

## Create Post
Create New Post

### Request

`POST /post/`

    curl --location --request POST 'http://localhost:8000/post/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ' \
    --form 'content=Next Post'

### Response

    HTTP/1.1 201 CREATED
    Date: Sat, 19 Sep 2020 04:49:12 GMT
    Status: 201 CREATED
    Content-Type: application/json

    {
    "id": 5,
    "content": "Readme Post",
    "create_at": "2020-09-19T04:49:12.800017Z",
    "updated_at": "2020-09-19T04:49:12.801735Z"
    }

## Get All Post
Get All post you and user you following had created.

### Request

`GET /all-post/`

    curl --location --request GET 'http://localhost:8000/all-post/' \
    --header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwNDkyNTY0LCJqdGkiOiIyMWUyOTlmMzFjYTI0YTEwYTIzMmM4NzZjZTQ0YmU5YSIsInVzZXJfaWQiOjJ9.Flf-OPJQ1ktSqbUtfrz7C4H9Uj4MTDkE-IOTdeKeFLQ'

### Response

    HTTP/1.1 200 OK
    Date: Sat, 19 Sep 2020 04:49:12 GMT
    Status: 200 OK
    Content-Type: application/json

    {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "content": "First Post",
            "create_at": "2020-09-19T03:11:33.853285Z",
            "updated_at": "2020-09-19T03:11:33.853285Z",
            "user": 1
        },
        {
            "id": 3,
            "content": "Test Post",
            "create_at": "2020-09-19T03:44:37.730898Z",
            "updated_at": "2020-09-19T03:44:37.730898Z",
            "user": 1
        },
        {
            "id": 4,
            "content": "Next Post",
            "create_at": "2020-09-19T03:45:09.551314Z",
            "updated_at": "2020-09-19T03:45:09.551314Z",
            "user": 1
        }
    ]
    }