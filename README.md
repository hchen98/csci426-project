# CSCI 426-project

<p>
CSCI 426 - M01/ Fall 2020 - Information Retrieval Group Project

Instructor: Dr. Cao

Team Member: Michael Trzaskoma, Wentao Yang, Francis Cheng, and Hui (Henry) Chen
</p>
<br>

## Demo:
* <a href="https://youtu.be/sVifrNOppzw">Here</a>

<br>

## Requirements:

Backend:
  * Python 3.x
  * selenium 3.141 or above
  
React Native:
  * Check package.json for the dependencies and library version

<br>

## Get Start
  * Create a Google Developer API: <a href="https://console.developers.google.com/apis/dashboard"> here </a>
  * Sign up Firebase: <a href="https://console.firebase.google.com/">here</a>
  * Note: <br>
    a. Use your own API key. Never share with anyone else. <br>
    b. Use ```host.exp.exponent``` as the “Package name”(Android) or "Bundle ID"(IOS) in the Google Cloud Console, otherwise you will face ```Error 400: redirect_uri_mismatch```.<br>
    c. Use ```openssl rand -base64 32 | openssl sha1 -c``` to generate openssl key<br>
    d. Place "google-services.json" under android directory
  * Clear the Metro's cache: ```yarn start --reset-cache```
  * Project package name: ``` com.csci426.rn ```
  * AWS EC2 - SSH method: <a href="http://simp.ly/p/M2jgxM">here </a>

<br>

## Run the app
Backend
  ```
  # install dependency
  pip install -r requirements.txt
  
  # add flask app to the environment variable/ path
  export FLASK_APP=flask_app.py

  # run the flask with port 8080 publically
  flask run --host=0.0.0.0 --port=8080

  # activate environement for debugging
  source csci426/bin/activate
  ```

React Native
```
cd <directory of your project>

# install all dependencies
npm install

# start the project with expo support
expo start
```
