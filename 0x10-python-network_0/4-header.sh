#!/bin/bash
# This script that takes in a URL, sends a GET request to the URL, and displays the body of the response with a custom header
curl -sH "X-School-User-Id: 98" "$1"
