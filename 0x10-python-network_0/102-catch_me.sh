#!/bin/bash
# a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response. 
link="0.0.0.0:5000/catch_me"; curl -o /dev/null -sw "You got me!" $link
