# anna-api
**RESTful API for [anna](https://github.com/patrikpihlstrom/anna)**

## usage


### ```GET /v1.0/get```
*Get job(s)*


| parameter | type                        | description           | required |
|-----------|-----------------------------|-----------------------|----------|
| id        | integer or list of integers | possible id(s)        | no       |
| name      | string or list of strings   | possible name(s)      | no       |
| status    | string or list of strings   | possible status(es)   | no       |
| driver    | string or list of strings   | possible driver(s)    | no       |
| container | string or list of strings   | possible container(s) | no       |
| sites     | string or list of strings   | possible site(s)      | no       |

```$ curl -H "Content-Type: application/json" -X GET --data '{"id": [1, 2, 3]}' http://localhost:5000/v1.0/get```


### ```POST /v1.0/push```
*Push a new job to the end of the queue*


| parameter | type            | description       | required |
|-----------|-----------------|-------------------|----------|
| drivers   | list of strings | driver(s) to test | yes      |
| sites     | list of strings | site(s) to test   | yes      |

```$ curl -H "Content-Type: application/json" -X POST --data '{"drivers": ["chrome", "firefox"], "sites": ["somesite"]}' http://localhost:5000/v1.0/push```




### ```POST /v1.0/clear```
*Stop & remove all running jobs and their corresponding containers*


| parameter | type | description | required |
|-----------|------|-------------|----------|

```$ curl -H "Content-Type: application/json" -X POST --data '{}' http://localhost:5000/v1.0/clear```




### ```POST /v1.0/rm```
*Stop & remove the matching jobs and their corresponding containers*


| parameter | type                        | description           | required |
|-----------|-----------------------------|-----------------------|----------|
| id        | integer or list of integers | possible id(s)        | no       |
| name      | string or list of strings   | possible name(s)      | no       |
| status    | string or list of strings   | possible status(es)   | no       |
| driver    | string or list of strings   | possible driver(s)    | no       |
| container | string or list of strings   | possible container(s) | no       |
| sites     | string or list of strings   | possible site(s)      | no       |

```$ curl -H "Content-Type: application/json" -X POST --data '{"id": [1, 2, 3]}' http://localhost:5000/v1.0/rm```
