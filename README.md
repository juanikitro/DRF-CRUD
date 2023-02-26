# DRF-CRUD Endpoints

## /register/

### POST

```json
{
    "username": String,
    "password": String,
    "password_confirm": String
}
```

## /login/

### POST

```json
{
    "username": String,
    "password": String,
}
```

## /api/projects/

### GET

```json
[
	{
		"id": Integer,
		"title": String ,
		"description": String,
		"technology": String ,
		"created_at": Date
	}
]
```

### POST

```json
{
    "title": String,
    "description": String,
    "technology": String,
}
```

## /api/projects/1

### GET

```json
{
    "id": Integer,
    "title": String ,
    "description": String,
    "technology": String ,
    "created_at": Date
}
```

### PATCH / PUT

```json
{
    "id": Integer,
    "title": String ,
    "description": String,
    "technology": String ,
    "created_at": Date
}
```

### DELETE

HTTP 204 No Content
