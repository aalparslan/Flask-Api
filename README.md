# Partial API Task

## Goal

Missing parts in the `api.py` file are completed. 
- PEP-8 conventions are followed.
- Unit tests are included. 
- Application is containerized with Docker.



## Task description

There are three API endpoints

1. `/user_status`

Description:

On this endpoint please provide an implementation that searches the records and
returns the correct `user_status` at the given date. You can imagine the
records as single events which get fired on a user status change. If a user
starts paying, there will be one record stored with status `paying`, whereas if
this user finishes paying, there will be another record added with status
`completed`. Consequently, a user remains in status `paying` until the next
`completed` event. In case there is no status available for a specific date,
simply return `non-paying`. The valid responses that should be provided are:
`paying`, `completed` or `non-paying`.

Required GET parameters:
- `user_id` (int)
- `date` (datetime)

Example request:

`/user_status?user_id=1&date=2017-01-01T10:00:00`

Example response:

```json
{
  "user_status": "paying"
}
```

2. `/ip_city`

Description:

On this endpoint please provide an implementation that searches the provided IP
ranges and returns the correct city based on the IP. In case the IP range is
not within any of the provided cities, `unknown` should be returned.

Required GET parameters:
- `ip` (str)

Example request:

`/ip_city?ip=10.12.0.100`

Example response:

```json
{
  "city": "Munich"
}
```

3. `/user_city`

Description:

Please read the `transactions.json` file and enrich it with the data given by
the API. This endpoint should provide an aggregate containing the
sum of `product_price` grouped by the given `user_status` and `city`.

Required GET parameters:
- `user_status` (string)
- `city` (string)

Example request:

`/user_city?user_status=paying&city=Munich`

Example response:

```json
{
  "product_price": 123456 
}
```

Note that this is just an example and not a real answer from API.

## Setup

1. Open a terminal and `cd` to the project
2. Build the docker image by typing
`docker image build -t flask-web-test .`
3. Run the dockerized flask app by typing
 `docker image build -t flask-web-test .`
4. Test the application by requesting the `http://localhost:5000` with the endpoints mentioned in previous sections.
