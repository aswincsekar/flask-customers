# Klinify Backend Developer Submission

This project is a submission to klinify for the role of Backend Developer

## Requirements:

- [ ] Create a simple customer data model,
- [ ] Implement an API that will perform CRUD operations on the customer data model, and
- [ ] Prepare documentation to guide a user on how to get the above running, and how to use it
- [ ] List Action - Youngest N Customers
- [ ] JWT Authentication 

### Optional Requirements
- [ ] Design against Replay Attack
- [ ] Dockerize

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


