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
