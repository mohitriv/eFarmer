# eFarmer
This is a server app, developed using Django framework and deployed on Heroku. The idea is to create a platform that will help farmers to sell their grains online directly to customers.

## API endpoints
Test these APIs with any rest client

### POST /crop/users – This will create a new user
```
https://efarmer.herokuapp.com/crop/users/ 
```

#### Body:
```
{
"password":‘String’,
"email": ‘String’,
"category": ‘String’, // ‘Seller’ or ‘Buyer’
"name": ‘String’,
"gender": ‘String’, // ‘Male’ or ‘Female’
"identificationNumber": ‘String’, // Driving license or any valid id number
"address": ‘String’, // Full address
"phone": ‘String’,
"date_of_birth": ‘String’ // Format - "1990-01-01"
}
```
#### Response:
```
User object or errors
```

### POST /login/ – login into the system
```
https://efarmer.herokuapp.com/login/
```
#### Body:
```
{
"password":’ String’, // Valid password
"email": ‘String’ // Valid email
}
```
#### Response:
```
Token or errors
```

### GET /crop/users – Get the current User
```
https://efarmer.herokuapp.com/crop/users
```
Authorization: JWT ‘Token’

#### Response:
```
Current User object
```

### GET /crop – Get all the crops
```
https://efarmer.herokuapp.com/crop 
```
Authorization: JWT ‘Token’

#### Response:
```
Crop array
```


### GET /crop?category={type} – Search using ‘category’
```
https://efarmer.herokuapp.com/crop?category=Wheat 
```
Authorization: JWT ‘Token’

#### Response:
```
Crop array
```

### GET /crop/{id} – Crop with id
```
https://efarmer.herokuapp.com/crop/1 
```
Authorization: JWT ‘Token’

#### Response:
```
Crop object
```


### GET /crop/detail/{id} – Crop detail with id
```
https://efarmer.herokuapp.com/crop/detail/1 
```
Authorization: JWT ‘Token’

#### Response:
```
CropDetail object
```

### License:
This project is licensed under the [MIT License](https://github.com/mohitriv/eFarmer/blob/master/LICENSE)
