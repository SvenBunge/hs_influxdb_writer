#!/bin/bash
(cd ../../; python2 ./generator.pyc hs_influxdb_writer utf-8)
markdown2 --extras tables,fenced-code-blocks,strike,target-blank-links doc/log14183.md > release/log14183.html
(cd release; zip -r 14183_hs_influxdb_writer.hslz *)
