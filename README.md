## Table of Contents

- [LoginAPI](#LoginAPI)
- [RegisterAPI](#RegisterAPI)
- [TokenRefreshView](#TokenRefreshView)
- [CreateMobileSubscriberAPI](#CreateMobileSubscriberAPI)
- [UpdateMobileSubscriberAPI](#UpdateMobileSubscriberAPI)
- [ListMobileSubscriberAPI](#ListMobileSubscriberAPI)

<a name="LoginAPI">User Account Signin API</a>
This API returns the details of an authenticated user after the appropriate credentials 
have been provided.

## User Account Signin API

\_Django Api / RegisterAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type  | URL                 |
| ----  | ------------------- |
| POST  | api/account/signin  |

### Header

| Type             | Property name      |
| ---------------- | -----------------  |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name   | type      | required | Description                       |
| --------------- | --------- | -------- | ----------------------------------|
| email           | String    | true     | The email of the user account     |
| password        | String    | true     | The password of thr user account  |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |
| 401  | "Invalid Credentials, try again"                |

### Successful Response Example

```
{
    "id": 1,
    "firstname": Moses,
    "othernames": Wuniche,
    "email": "moses@gmail.com",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1vc2VzQGdtYWlsLmNvbSIsImV4cCI6MTY0ODQwODAzOH0.6A1g_rcjVynEYM4OlvJyIt0ips1-U6Pi7LWHeIcrcdM"
}
```

<a name="RegisterAPI">User Account Registration API</a>

The RegisterAPI will accept the following data and return newly
created user details:
firstname, othernames, email, password 

## User Account Registration API

_Django Api / RegisterAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type  | URL                 |
| ----  | ------------------- |
| POST  | api/account/signup  |

### Header

| Type             | Property name      |
| ---------------- | -----------------  |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name   | type      | required | Description                        |
| --------------- | --------- | -------- | ---------------------------------- |
| email           | String    | true     | The email of the account user      |
| password        | String    | true     | The password of the account user   |
| firstname       | String    | false    | The firstname of the account user  |
| othername       | String    | false    | The othernames of the account user |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "This field may not be blank."                  |
| 403  | "User with this email already exits"            |

### Successful Response Example

```
{
    "id": 1,
    "firstname": Moses,
    "othernames": Wuniche,
    "email": "moses@gmail.com",
}
```

<a name="TokenRefreshView">Token Refresh API</a>

The TokenRefreshView accepts a refresh token and return a new
access token

## Tokin Refresh API

_Django Api / RegisterAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type  | URL                 |
| ----  | ------------------- |
| POST  | api/token/refresh/  |

### Header

| Type             | Property name      |
| ---------------- | -----------------  |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name   | type      | required | Description                        |
| --------------- | --------- | -------- | ---------------------------------- |
| refresh         | String    | true     | The refresh token provided on login| 
<!-- Refresh token is currently obmitted from the login response due to time constraints  -->


### Error Responses

| Code | Message                            |
| ---- | ---------------------------------- |
| 400  | "This field may not be blank."     |
| 401  | "Token is invalid or expired"      |

### Successful Response Example

```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ4NDIzNzM2LCJpYXQiOjE2NDg0MTY0OTYsImp0aSI6ImZjNzM3NTE5MmQ5YjRlZjhhNTNiNzUyNzBiNjhmYjRkIiwidXNlcl9pZCI6MX0.N6LkRc2rinV5u55RreyIU4MEgBxvmppaNTQIKtsoBLA"
}
```

<a name="CreateMobileSubscriberAPI">Mobile Subscription Creation/Details-Retrieval/Deletion API</a>

The CreateMobileSubscriberAPI accepts the following field data and returns
the details on a newly created Mobile Subcription object:
msisdn, customer_id_owner, customer_id_user, service_type

## Mobile Subscription Create/Retrieve/Delete API

_Django Api / CreateMobileSubscriberAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type    | URL                       |
| ----    | -----------------------   |
| POST    | api/sub/create            |
| GET     | api/sub/<sub_id>          | 
| DELETE  | api/sub/<sub_id>/delete   | 

### Header

| Type             | Property name      |
| ---------------- | -----------------  |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

**GET and DELETE -> No JSON Props**

| Property Name     | type         | required | Description                          |
| ---------------   | ---------    | -------  | ----------------------------------   |
| msisdn            | String(E164) | true     | E164 Formatted Mobile number         |
| customer_id_owner | Integer      | true     | The owner of the subscription number |
| customer_id_user  | Integer      | true     | The user of the subscription         |
| service_type      | String(Enum) | true     | The user's service choice            |


### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "This field may not be blank."                  |
| 400  | "This field must be unique."                    |
| 401  | "Authentication credentials were not provided." |

### Successful Response Example

```
{
    "id": 1,
    "msisdn": "+233549124145",
    "customer_id_owner": 1,
    "customer_id_user": 1,
    "service_type": "MOBILE_PREPAID",
    "service_start_date": 1648417612.292439
}
```

<a name="UpdateMobileSubscriberAPI">Mobile Subscription Update API</a>

The CreateMobileSubscriberAPI accepts the following field data and returns
an updated instance of a Mobile Subscription:
service_type

An admin view will be created to allow admins the permission
to edit any field of choice. 

## Mobile Subscription-Details Update API

_Django Api / UpdateMobileSubscriberAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type    | URL                       |
| ----    | -----------------------   |
| PUT     | api/sub/<sub_id>/update   |

### Header

| Type             | Property name        |
| ---------------- | -----------------    |
| Allow            | PUT,PATCH , OPTIONS  |
| Content-Type     | application/json     |
| Vary             | Accept               |
| WWW-Authenticate | Bearer realm="api"   |

### JSON Body

| Property Name     | type         | required | Description                          |
| ---------------   | ---------    | -------  | ----------------------------------   |
| service_type      | String(Enum) | true     | The user's service choice            |


### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "This field may not be blank."                  |
| 401  | "Authentication credentials were not provided." |

### Successful Response Example

```
{
    "id": 1,
    "msisdn": "+233549124145",
    "customer_id_owner": 1,
    "customer_id_user": 1,
    "service_type": "MOBILE_POSTPAID",
    "service_start_date": 1648417612.292439
}
```

<a name="ListMobileSubscriberAPI">Mobile Subscriptions/Numbers List API</a>

These endpoints take no JSON data

## Mobile Subscribers/Numbers List API

_Django Api / ListMobileSubscriberAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type    | URL                    |
| ----    | ---------------------  |
| GET     | api/sub/list           | 
| GET     | api/sub/numbers/list   | 


### Header

| Type             | Property name      |
| ---------------- | -----------------  |
| Allow            | GET, OPTIONS       |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name     | type         | required | Description                          |
| ---------------   | ---------    | -------  | ----------------------------------   |

### Search Params

| Property Name             | type       | Accuracy                  | 
| -----------------------   | ---------  | ------------------------  | 
| msisdn                    | String     | Starts-with/ Includes     |
| customer_id_owner__email  | String     | Starts-with/ Includes     |
| customer_id_user__email   | String     | Starts-with/ Includes     |
| service_type              | String     | Exact-Match               |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |

### Successful Response Example [ Mobile subscribers ]:

```

[
    {
        "id": 1,
        "msisdn": "+233549124145",
        "customer_id_owner": 1,
        "customer_id_user": 1,
        "service_type": "MOBILE_PREPAID",
        "service_start_date": 1648417612.292439
    },
    {
    "id": 2,
    "msisdn": "+233549124155",
    "customer_id_owner": 2,
    "customer_id_user": 1,
    "service_type": "MOBILE_POSTPAID",
    "service_start_date": 1648420085.755655
}
]
```

### Successful Response Example [ Numbers ]:

```
[
    {
        "msisdn": "+233549124155"
    },
    {
        "msisdn": "+233549124145"
    }
]
```