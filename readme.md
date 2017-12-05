# Challenge

Create a backend API for computing the cross product of two vectors. Please lay this out like you would a large-scale enterprise deployment.

## Requirements

- MUST use Docker containers
- MUST use Python 3.6 on the backend
- MUST have a health check endpoint
- MUST have a home page to welcome a user to the site
- MUST store in a database all computed results
- MUST produce reliable validation errors. i.e. the site cannot throw any 
  500-class errors
- MUST have test coverage greater than 90%

## API Spec

```raml
/compute:
  get:
    description: |
      Shows a list of all cross products inputted and their results
    responses:
      200:
        body:
          application/json:
            example: |
              {
                "results": [
                  {
                    "id": 1,
                    "vector1": [1, 2, 3],
                    "vector2": [4, 5, 6],
                    "result": [7, 8, 9],
                    "created": "2015-12-02T12:39:25+00:00"
                  }
                ]
              }
  post:
    description: |
      Computes the cross product of two vectors.
    body:
      application/json:
        example: |
          {
            "vector1": [1, 2, 3],
            "vector2": [4, 5, 6]
          }
    responses:
      200:
        body:
          application/json:
            example: |
              {
                "id": 1,
                "vector1": [1, 2, 3],
                "vector2": [4, 5, 6],
                "result": [7, 8, 9],
                "created": "2015-12-02T12:39:25+00:00"              
              }
      400:
        body:
          application/json:
            example: |
              {
                "message": {
                  "vector1": [
                    "Missing or incorrectly formatted data supplied."
                  ]
                }
              }
/health:
  get:
    description: |
      Returns a handy message to let a backend know the server is online.
    responses:
      200:
        body:
          application/json:
            example: |
              {
                "message": "ok"
              }
```
