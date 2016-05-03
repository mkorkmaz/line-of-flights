# Line of Flights
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mkorkmaz/line-of-flights/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mkorkmaz/line-of-flights/?branch=master) [![Build Status](https://scrutinizer-ci.com/g/mkorkmaz/line-of-flights/badges/build.png?b=master)](https://scrutinizer-ci.com/g/mkorkmaz/line-of-flights/build-status/master)
FlightRadar24 data collector service script written in Python.

"[Flightradar24](https://www.flightradar24.com) is a flight tracker that shows live air traffic from around the world. Flightradar24 combines data from several data sources including ADS-B, MLAT and radar data. The ADS-B, MLAT and radar data is aggregated together with schedule and flight status data from airlines and airports." <sup>[*](https://www.flightradar24.com/how-it-works)</sup>

### Installation and usage

You will need an Elasticsearch instance installed and running.
Let's say your Elasticsearch runs on 127.0.0.1,
your index will be named as "radar", type will be named as "logs"
and you wanna "live track" Turkish Airlines flights.

```
git clone https://github.com/mkorkmaz/line-of-flights.git
cd line-of-flights
chmod u+rwx mappings.sh
./mappings.sh 127.0.0.1 radar logs
pip3 install -r pip.install
cp config.sample.ini config.ini
```

Edit config.ini according to your setup and your needs. Then run:
```
python3 ./radar.py
```

If you want to collect data continuously, use cron jobs.
You can get the data at least every minute. Never try to get the data more frequently.

**Cron job command**

```
* * * * * python3 /path/to/radar.py
```