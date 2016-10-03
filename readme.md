# Example Gauge Python Scenario/Rest API Test of Magento

This is an example of using [Gauge](https://github.com/getgauge/gauge) for testing Magento.
Uses Selenium and Magento Rest APIs (to simulate a mobile application)

## Prerequisites
- Install Python 3
- Install pip
- Install Gauge  http://getgauge.io/documentation/user/current/installations/
- Install Gauge-Python plugin  https://gauge-python.readthedocs.io/en/latest/installation.html
````
  gauge --install python
````
- Install chromedriver https://sites.google.com/a/chromium.org/chromedriver/downloads

## Magento Test System setup

Use magento in docker as described [here] (https://alankent.me/gsd/introduction-to-docker/)

Or from cmd line run:
docker run -d -i -t -p 80:80 -p 3000:3000 -p 3001:3001 -p 2222:22 --name gsd alankent/gsd


## Execute tests
Install dependencies
````
pip install -r requirements.txt
````
Add Magento host IP to env/default/default.properties

Run Test:
````
gauge specs
````