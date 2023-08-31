#!/bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response. 
<<<<<<< HEAD
link="0.0.0.0:5000/catch_me"; curl -sw "You got me!" $link
=======
curl -sX GET http://0.0.0.0:5000/catch_me
>>>>>>> 9dfa2bcea7ae8ee2a98f843c6e4dd65ca8ea726a
