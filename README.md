# MetadataGen
This is a generator for metadata according to the MOOChub format.

## Install

### Prerequisites

The application is made to be run un Ubuntu 22.04.
Make sure the system is up-to-date.

```
sudo apt update && sudo apt upgrade
```

The source code can be cloned using Git.

```
sudo apt install git
```

The application is a Docker image. 
Docker can be installed via snap.

```
sudo snap install docker
```

### Get data from source

Get the data from the GitHub repository:


```
git clone https://github.com/MaxThomasHPI/MetadataGen.git
```

### Set environment variables

Make sure to set all environment variables in the .env file before build/start the docker containers.
 
#### Gemini key

Since the program uses the Gemini-API from Google, a valid key for this application needs to be provided.
It needs to be stored in an environment variable called "GEMINI_KEY".
The key has to work with the gemini-2.5-flash model.
Add the key in the .env variable at the root level.

```
# .env
GEMINI_KEY=<Your Gemini-API key>
```

#### Postgres

There is a database running in the background to log input data and the suggestions made.
The database is set up in a local bind and will take environment variables as provided in the .env file.
This includes a username for the database as well as a password.
A default database called "suggestions" will be set up as well. 
Please do not change the name of the database.

````
# .env
POSTGRES_USER=<your-psql-username>
POSTGRES_PASSWORD=<your-psql-password>
POSTGRES_DB=suggestions  # the default database to be created at startup, do not change!
````

### Setup and run docker container

The repository contains a Dockerfile and a docker-compose.yml for setting up an image.
Go to the directory containing the Dockerfile/docker-compose.yml and run:

```
sudo docker compose up --build
```

The application should start but can also be started with:

```
sudo docker compose up
```

after successfully building the image.


### Configuration

The application will run by default on Port 5000 (default Flask).
Port 80 will be exposed as stated in the Dockerfile.
In the docker-compose.yml the mapping (80:5000) is configured.
Also, the nginx.conf contains the mapping.
If you prefer another configuration make sure to update these files accordingly.
With this setup the application frontend can be reached via accessing http://localhost in the browser.


### Supported frameworks

The selection of frameworks for recommendations is currently limited.
Frameworks were selected after careful investigations and evaluations.
This effects the following attributes (the supported frameworks are given in brackets):
- educationalAlignment (ISCED-F)
- teaches (ESCO)
- educationalLevel (DigComp)


## Working with the API

The MetadataGenerator is meant to be used via its API.
The following parts show examples for API calls.

### Input data for receiving full metadata including suggestions

MetadataGen provides an API for generating suggestions for the attributes "educationalAlignment", "teaches", "keywords", "educationalLevel".
It expects an HTTP POST request with a JSON file in the body.
The JSON file must follow the following schema:

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://github.com/moochub/metadatagen/input-schemas/
    input-metadatagen.json",
    "title": "JSON schema for using the MetadataGen API",
    "description": "This schema specifies the JSON format 
    that an JSON file in the HTTP POST request body must 
    contain to use the MetadataGen. This schema describes 
    the input for a full valid metadata file according to 
    the MOOChub format.",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The title/name of the course",
            "example": "Sustainability in the Digital Age: 
            Efficient AI Techniques in the LLM Era"
        },
        "description": {
            "type": "string",
            "description": "Description of the course as an 
            HTML document",
            "example": "<h2>Welcome to the 'Sustainability 
            in the Digital Age' series</h2> <p>In an 
            era where digital technologies ..."
        },
        "publisher": {
            "type": "object",
            "description": "The publisher of the course.",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the 
                    publisher.",
                    "example": "openHPI"
                }
            },
            "required": [
                "name"
            ]
        },
        "creator": {
            "type": "array",
            "description": "The creators of the course.",
            "items": {
                "type": "object",
                "description": "A creator of the course.",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the 
                        creator.",
                        "example": "Haojin Yang"
                    }
                },
                "required": [
                    "name"
                ]
            }
        },
        "url": {
            "type": "string",
            "description": "An URI pointing at the course 
            landingpage.",
            "fromat": "IRI",
            "example": "https://open.hpi.de/courses/
            aimethods2025"
        },
        "license": {
            "type": "array",
            "description": "All license informations about 
            the course.", 
            "items": {
                "type": "object",
                "description": "The license information about 
                the course.",
                "properties": {
                    "identifier": {
                        "type": "string",
                        "description": "A license shortcode 
                        according to https://spdx.org/licenses/ 
                        or \"proprietary\".",
                        "example": "CC-BY-NC-SA-4.0"
                    },
                    "url": {
                        "type": [
                            "string",
                            "null"
                        ],
                        "format": "iri",
                        "description": "A license according to 
                        https://spdx.org/licenses/ or \"null\" 
                        if proprietary.",
                        "example": "https://spdx.org/licenses/
                        CC-BY-SA-4.0.html"
                    }
                },
                "requirements": [
                    "identifier",
                    "url"
                ]
            }
        },
        "educationalAlignment": {
            "type": "array",
            "description": "The framework to be used for
            the suggestion.",
            "items": {
                "type": "object",
                "description": "The framework name to 
                be used for the suggestion.",
                "properties": {
                    "educationalFramework": {
                        "type": "string",
                        "description": "The name of the 
                        framework to be used for the 
                        suggestion",
                        "enum": [
                           "ISCED-F"
                       ]
                    }
                },
                "required": [
                    "educationalFramework"
                ]
            }
        },
        "teaches": {
            "type": "array",
            "description": "The framework to be used for
            the suggestion.",
            "items": {
                "type": "object",
                "description": "The framework name to 
                be used for the suggestion.",
                "properties": {
                    "educationalFramework": {
                        "type": "string",
                        "description": "The name of the 
                        framework to be used for the 
                        suggestion",
                        "enum": [
                            "ESCO"
                        ]
                    }
                },
                "required": [
                    "educationalFramework"
                ]
            }
        },
        "keywords": {
            "type": "null"
        },
        "educationalLevel": {
            "type": "array",
            "description": "The framework to be used for
            the suggestion.",
            "items": {
                "type": "object",
                "description": "The framework name to 
                be used for the suggestion.",
                "properties": {
                    "educationalFramework": {
                        "type": "string",
                        "description": "The name of the 
                        framework to be used for the 
                        suggestion",
                        "enum": [
                            "DigComp"
                        ]
                    }
                },
                "required": [
                    "educationalFramework"
                ]
            }
        }
    },
    "required": [
        "name",
        "description",
        "publisher",
        "creator",
        "url",
        "license"
    ]
}
```

### Generating selected suggestions for keywords, educationalAlignment, teaches, educationalLevel

It is possible to generate and receive only the suggestions as separated metadata.
The metadata still follows the requirements of the MOOChub format but is not a full metadat file.
This simultaneously simplifies the input data since only course title and description is needed here.
An input schema is shown in the following:

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://github.com/moochub/metadatagen/input-schemas/
    input-suggestions.json",
    "title": "JSON schema for using the MetadataGen API",
    "description": "This schema specifies the JSON format that an 
    JSON file in the HTTP POST request body must contain to use 
    MetadataGen. This simplified schema can only be used with the 
    "/suggestion" route and only returns the suggestions for 
    keywords, educationalAlignment, teaches and educationalLevel 
    attribute.",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The title/name of the course",
            "example": "Sustainability in the Digital Age: 
            Efficient AI Techniques in the LLM Era"
        },
        "description": {
            "type": "string",
            "description": "Description of the course as an 
            HTML document",
            "example": "<h2>Welcome to the 'Sustainability 
            in the Digital Age' series</h2> <p>In an 
            era where digital technologies ..."
        }
    },
    "required": [
        "name",
        "description"
    ]
}
```
