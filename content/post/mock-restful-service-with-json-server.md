+++
date = "2016-05-05T00:08:24+08:00"
draft = true
title = "Mock RESTful Service with Json-server"

+++

## Introduction

Json-server is the Node application to mock RESTful service without programming. You just need to write the JSON file and it can mock the funcional RESTful service for testing or developing.

The homepage of this project is <https://github.com/typicode/json-server>.

## Installation

```
npm install -g json-server
```

## Usage

We just need to define the JSON file.

```
{
  "people": [
    "tobe",
   ]
}
```

Then run with the command.

```
json-server ./test.json
```

Open your browser and go to `http://localhost:3000" to access the service.

## Mock Request

We can also mock RESTful requests with the powerful chrome plugin, postman.
