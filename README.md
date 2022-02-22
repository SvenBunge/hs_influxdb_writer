# InfluxDB Writer (14183)
Gira Homeserver 4 Logikmodule to write values to the timeseries database *InfluxDB*

## Developer Notes

Developed for the GIRA HomeServer 4.11 (Should work >4.7)
Licensed under the LGPL to keep all copies & forks free!

:exclamation: **If you fork this project and distribute the module by your own CHANGE the Logikbaustein-ID because 14183 is only for this one and registered to @SvenBunge !!** :exclamation:

If something doesn't work like expected: Just open an issue. Even better: Fix the issue and fill a pull request.

## Installation

Download a [release](https://github.com/SvenBunge/hs_influxdb_writer/releases) and install the module / Logikbaustein like others in Experte.
You find the module in the category "Datenaustausch".

The latest version of the module is also available in the [KNX-User Forum Download Section](https://service.knx-user-forum.de/?comm=download&id=14183)

## Documentation

This module writes values (per interval or on update) to InfluxDB. Make timeseries data available fe. for Grafana observations / visualization.
Works with InfluxDB >1.8 

More [detailed documentation](doc/log14183.md)

## Build from scratch

1. Download [Schnittstelleninformation](http://www.hs-help.net/hshelp/gira/other_documentation/Schnittstelleninformationen.zip) from GIRA Homepage
2. Decompress zip, use `HSL SDK/2-0/framework` Folder for development.
3. Checkout this repo to the `projects/hs_influxdb_writer` folder
4. Run the generator.pyc (`python2 ./generator.pyc hs_influxdb_writer`)
5. Import the module `release/14183_hs_influxdb_writer.hsl` into the Experte Software
6. Use the module in your logic editor

You can replace step 4 with the `./buildRelease.sh` script. With the help of the markdown2 python module (`pip install markdown2`) it creates the documentation and packages the `.hslz` file. This file is also installable in step 5 and adds the module documentation into the Experte-Tool.  
 
## Libraries

* Only python shiped libraries used.

The shipped libraries may distributed under a different license conditions. Respect those licenses as well!
