pg-notify-webhook
=================

Implements a simple server process that listens to Postgres
notifications, then fires off a webhook in response.

The content of the message is sent as the JSON payload to the webhook.

You can use this to invoke AWS Lambda functions (fronted by API gateway)
or any other system that receives HTTP requests.

Install it as follows:

``pip install pg-notify-webhook``

You simply set up a ``config.yaml`` with the database connection string
and define one or more channels and webhooks. Then start the server as
follows:

``pg-notify-webhook``

Once the server is running, you can send notifications from Postgres:

``NOTIFY one, '{"name": "Vijay"}'``

config.yaml
'''''''''''

.. code:: yaml

    DSN: postgresql://user:password@hostname:5432/database
    channels:
      - one
      - two
    webhooks: 
      one: https://postman-echo.com/get?foo1=bar1&foo2=bar2
      two: https://example.com

