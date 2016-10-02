# Example Gauge Python Scenario/Rest API Test of Magento

This is an example of using [Gauge](https://github.com/getgauge/gauge) for testing Magento.
Uses Selenium and Magento Rest APIs (to simulate a mobile appliation)

## Prerequisites
- Python 3
Install dependencies
````
pip install -r requirements.txt
````
- Install Gauge
- Install Gauge-Python plugin
````
  gauge --install python
````
- Install chromedriver

## Magento Test System setup

Use magento in docker as described [here] (https://alankent.me/gsd/introduction-to-docker/)

Or from cmd line run:
docker run -d -i -t -p 80:80 -p 3000:3000 -p 3001:3001 -p 2222:22 --name gsd alankent/gsd

Magento mobile application uses token authentication:
http://devdocs.magento.com/guides/v2.0/get-started/authentication/gs-authentication-token.htm

## Run
````
gauge specs
````