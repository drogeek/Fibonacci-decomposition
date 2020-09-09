# Fibonacci decomposition 
Start a service that allows to decompose numbers into sum of fibonacci terms

# How to build&run
* Install Docker
* Install docker-compose
* (Optional) edit .env to specify on which address/port to listen
* run *docker-compose up* in the project directory

# How to use
* contact the server on IP_ADRR:PORT, as specified in .env
* the API is the following
    * **fib/<number>**: returns the decomposition of the number
    * **health**: returns the "health" of the service, represented by the max number that was cached in the underlying database

# More information
The recursive function called **fib_decompose** located in **fib_decomp.py** is the one that give the end result
In order not to recompute things already computed, a Postgres database is used, that stores results in json format
A caching of the database requests and of the computed fibonacci sequences is made.
