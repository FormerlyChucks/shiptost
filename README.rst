shiptost
========

**Shiptost.com API Wrapper**

Lightweigt API wrapper, made for `Shiptost <https://shiptost.com>`_. Allows access to API endpoints and returns a JSON result.

Installation
------------

.. code-block:: bash

   pip3 install shiptost

How to use
----------

Initialize your API instance:

.. code-block:: python

    from shiptost import Shiptost
    
    shiptost = Shiptost(client_id='client_id',
                        client_secret='client_secret',
                        user_agent='user_agent',
                        access_token='access_token',
                        refresh_token='refresh_token')

Sending a get request:

.. code-block:: python

    me = shiptost.get('/api/v1/identity')
    print(me)
    
Sending a post request:

.. code-block:: python

    title = 'API TESTING'
    url = 'https://localhost:8000'
    parameters = {'board': 'shiptost',
                  'title': title,
                  'url' : url}
    submit = shiptost.post('/api/v1/submit', data=parameters)
    print(submit)
