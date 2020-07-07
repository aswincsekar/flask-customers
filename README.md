# Klinify Backend Developer Submission

This project is a submission to klinify for the role of Backend Developer

## Requirements:

- [x] Create a simple customer data model,
- [x] Implement an API that will perform CRUD operations on the customer data model, and
- [x] Prepare documentation to guide a user on how to get the above running, and how to use it
- [x] List Action - Youngest N Customers
- [ ] JWT Authentication 

### Optional Requirements
- [ ] Design against Replay Attack
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


### Deployment or packaging
Prepare a docker image or docker-compose file that provides a means of easy deployment.
The build process should include the necessary initialization of Postgres and any misc. configuration.

# Demo Process

## Building Images

`docker-compose -f docker-compose.yml build`

## Starting Docker Services

`docker-compose -f docker-compose.yml up -d`

## Testing API

1. Open Browser
2. Go to localhost
3. Test APIs on the swagger interface


