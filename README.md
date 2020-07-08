# Flask Customers API 

## Requirements:

- [x] Create a simple customer data model,
- [x] Implement an API that will perform CRUD operations on the customer data model, and
- [x] Prepare documentation to guide a user on how to get the above running, and how to use it
- [x] List Action - Youngest N Customers
- [x] JWT Authentication 

### Optional Requirements
- [x] Design against Replay Attack
- [x] Dockerize

## Specifications

### Model
CUSTOMER :
Customers (
id,
name,
dob,
updated_at
)

### API
Create RESTful API endpoints returning JSON so that a user can perform CRUD (create, read, update, delete) actions to the customers table. In addition, also implement a list action. List should take in a number n as a GET parameter that returns n youngest customers ordered by date of birth.


### Authentication
The API endpoints should not be publicly accessible, use JWT to implement authentication.


## Additional Bonus requirements

### Authentication
Replay attacks are possible with JWT since the auth data is stored client-side. Implement a simple method to block the recycling (replays) of old sessions. This process need not be comprehensive, just share an explanation of the potential pitfalls of what you’ve designed.

**Solution :** 

To prevent replay attacks, we have taken the following steps
1. Short expiration time for each access token, currently set to 10 minutes
2. Use of Refresh Token to refresh the access token, this reduces the chances of continuation fo the replay attack
3. Blacklist Token once Logout is performed


### Deployment or packaging
Prepare a docker image or docker-compose file that provides a means of easy deployment.
The build process should include the necessary initialization of Postgres and any misc. configuration.

# Docker Demo Process

## Building Images

`docker-compose -f docker-compose.yml build`

## Starting Docker Services

`docker-compose -f docker-compose.yml up -d`

## Testing API

1. Open Browser
2. Go to localhost
3. Test APIs on the swagger interface

### Workflow

#### Login

User should get the JWT token at 

`http://localhost/api/v1/authentication/login`

METHOD : POST 

Access Credentials

```
username : test
password : test
```

RESPONSE : 

```
{
    access_token : {token},
    refresh_token : {token}
}
```

#### Refresh Token

User should get the JWT token at 

`http://localhost/api/v1/authentication/refresh`

METHOD : POST 

AUTHORIZATION : Bearer Token 

RESPONSE : 

```
{
    access_token : {token},
    refresh_token : {token}
}
```

#### Get Customers

`http://localhost/api/v1/customers/customers`

METHOD : GET

AUTHORIZATION : Bearer Token 

#### Create Customers

`http://localhost/api/v1/customers/customers`

METHOD : POST

AUTHORIZATION : Bearer Token 

BODY :

```
{
  "updated_at": "2020-07-08T12:55:49.930Z",
  "name": "string",
  "dob": "2020-07-08"
}
```

#### Get N Youngest

`http://localhost/api/v1/customers/nyoungest?n=1`

METHOD : GET

PARAMS : n -> int

AUTHORIZATION : Bearer Token 

#### Update Customer

`http://localhost/api/v1/customers/customers/{customer_id}`

METHOD : PUT

AUTHORIZATION : Bearer Token 

BODY :

```
{
  "updated_at": "2020-07-08T12:55:49.930Z",
  "name": "string",
  "dob": "2020-07-08"
}
```

#### Delete Customer

`http://localhost/api/v1/customers/customers/{customer_id}`

METHOD : DELETE

AUTHORIZATION : Bearer Token 

### Postman Collection

Use the following postman collection to test the API. All the requests are given the pre-request scripts to fetch the 
access token

Postman Collection Link : https://documenter.getpostman.com/view/892323/T17Kbkus





