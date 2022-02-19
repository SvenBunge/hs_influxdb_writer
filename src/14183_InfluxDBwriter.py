# coding: utf-8

import urllib2
import ssl
import time


##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class InfluxDBwriter14183(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "InfluxDBwriter14183")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_INTERVAL_FREQUENCY=1
        self.PIN_I_UPDATE_WRITES=2
        self.PIN_I_INFLUXDB_URL=3
        self.PIN_I_INFLUXDB_TOKEN=4
        self.PIN_I_INFLUXDB_ORG=5
        self.PIN_I_BUCKET=6
        self.PIN_I_MEASUREMENT=7
        self.PIN_I_TAG_NAME=8
        self.PIN_I_TAG_VALUE=9
        self.PIN_I_VALUE1_NAME=10
        self.PIN_I_VALUE1_VAL=11
        self.PIN_I_VALUE2_NAME=12
        self.PIN_I_VALUE2_VAL=13
        self.PIN_I_VALUE3_NAME=14
        self.PIN_I_VALUE3_VAL=15
        self.PIN_I_VALUE4_NAME=16
        self.PIN_I_VALUE4_VAL=17
        self.PIN_I_VALUE5_NAME=18
        self.PIN_I_VALUE5_VAL=19
        self.PIN_I_VALUE6_NAME=20
        self.PIN_I_VALUE6_VAL=21
        self.PIN_I_VALUE7_NAME=22
        self.PIN_I_VALUE7_VAL=23
        self.PIN_I_VALUE8_NAME=24
        self.PIN_I_VALUE8_VAL=25
        self.PIN_O_SEND_COUNTER=1
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.interval = None
        self.DEBUG = self.FRAMEWORK.create_debug_section()
        self.counter = 0

    def on_init(self):
        self.interval = self.FRAMEWORK.create_interval()
        if self._get_input_value(self.PIN_I_INTERVAL_FREQUENCY) != -1:
            self.interval.set_interval(self._get_input_value(self.PIN_I_INTERVAL_FREQUENCY) * 1000, self.on_interval)
            self.interval.start()

    def on_input_value(self, index, value):
        if index == self.PIN_I_INTERVAL_FREQUENCY:
            self.interval.stop()
            if value != -1:
                self.interval.set_interval(value * 1000, self.on_interval)
                self.interval.start()
        elif index in [self.PIN_I_VALUE1_VAL, self.PIN_I_VALUE2_VAL, self.PIN_I_VALUE3_VAL, self.PIN_I_VALUE4_VAL,
                       self.PIN_I_VALUE5_VAL, self.PIN_I_VALUE6_VAL, self.PIN_I_VALUE7_VAL, self.PIN_I_VALUE8_VAL] \
                and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 1:
            self.send_values(self.build_value_lines())
        elif index == self.PIN_I_VALUE1_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE1_NAME), value))
        elif index == self.PIN_I_VALUE2_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE2_NAME), value))
        elif index == self.PIN_I_VALUE3_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE3_NAME), value))
        elif index == self.PIN_I_VALUE4_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE4_NAME), value))
        elif index == self.PIN_I_VALUE5_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE5_NAME), value))
        elif index == self.PIN_I_VALUE6_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE6_NAME), value))
        elif index == self.PIN_I_VALUE7_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE7_NAME), value))
        elif index == self.PIN_I_VALUE8_VAL and self._get_input_value(self.PIN_I_UPDATE_WRITES) == 2:
            self.send_values(self.add_value_line([], self._get_input_value(self.PIN_I_VALUE8_NAME), value))

    def on_interval(self):
        self.send_values(self.build_value_lines())

    def build_value_lines(self):
        value1_name = self._get_input_value(self.PIN_I_VALUE1_NAME)
        value1_val = self._get_input_value(self.PIN_I_VALUE1_VAL)
        value2_name = self._get_input_value(self.PIN_I_VALUE2_NAME)
        value2_val = self._get_input_value(self.PIN_I_VALUE2_VAL)
        value3_name = self._get_input_value(self.PIN_I_VALUE3_NAME)
        value3_val = self._get_input_value(self.PIN_I_VALUE3_VAL)
        value4_name = self._get_input_value(self.PIN_I_VALUE4_NAME)
        value4_val = self._get_input_value(self.PIN_I_VALUE4_VAL)
        value5_name = self._get_input_value(self.PIN_I_VALUE5_NAME)
        value5_val = self._get_input_value(self.PIN_I_VALUE5_VAL)
        value6_name = self._get_input_value(self.PIN_I_VALUE6_NAME)
        value6_val = self._get_input_value(self.PIN_I_VALUE6_VAL)
        value7_name = self._get_input_value(self.PIN_I_VALUE7_NAME)
        value7_val = self._get_input_value(self.PIN_I_VALUE7_VAL)
        value8_name = self._get_input_value(self.PIN_I_VALUE8_NAME)
        value8_val = self._get_input_value(self.PIN_I_VALUE8_VAL)

        valuelines = []
        self.add_value_line(valuelines, value1_name, value1_val)
        self.add_value_line(valuelines, value2_name, value2_val)
        self.add_value_line(valuelines, value3_name, value3_val)
        self.add_value_line(valuelines, value4_name, value4_val)
        self.add_value_line(valuelines, value5_name, value5_val)
        self.add_value_line(valuelines, value6_name, value6_val)
        self.add_value_line(valuelines, value7_name, value7_val)
        self.add_value_line(valuelines, value8_name, value8_val)

        valuelines.sort()  # https://docs.influxdata.com/influxdb/cloud/write-data/best-practices/optimize-writes/

        return valuelines

    def add_value_line(self, valuelines, value_name, value_val):
        if value_name != "" and value_val != -99999.99:  # fieldname must be set and initial value changed
            valuelines.append(value_name + "=" + str(value_val))

        return valuelines

    def send_values(self, valuelines):
        try:
            influx_url = self._get_input_value(self.PIN_I_INFLUXDB_URL)
            influx_token = str(self._get_input_value(self.PIN_I_INFLUXDB_TOKEN))
            influx_org = self._get_input_value(self.PIN_I_INFLUXDB_ORG)
            influx_bucket = self._get_input_value(self.PIN_I_BUCKET)
            influx_measurement = self._get_input_value(self.PIN_I_MEASUREMENT)

            # Build body
            epoch_time = int(time.time())
            post_body = influx_measurement
            if self._get_input_value(self.PIN_I_TAG_NAME) != "" and self._get_input_value(self.PIN_I_TAG_VALUE) != "":
                post_body += "," + self._get_input_value(self.PIN_I_TAG_NAME) + "=" + \
                            self._get_input_value(self.PIN_I_TAG_VALUE)
            post_body += " " + ",".join(valuelines) + " " + str(epoch_time)

            self.DEBUG.set_value("Last body", post_body)

            # URL
            url = influx_url + "/api/v2/write?bucket=" + influx_bucket + "&org=" + influx_org + "&precision=s"
            self.DEBUG.set_value("Last url", url)

            # Auth & URL
            auth_header_str = "Token " + influx_token
            headers = {'Authorization': auth_header_str, 'Content-Type': "text/plain; charset=utf-8"}

            # Build a SSL Context to disable certificate verification.
            ctx = ssl._create_unverified_context()
            # Open the URL and read the response.
            response = urllib2.urlopen(urllib2.Request(url, data=post_body, headers=headers), context=ctx)
            response_data = response.read()
            self.DEBUG.set_value("Last response", response_data)
            self.counter += 1
            self._set_output_value(self.PIN_O_SEND_COUNTER, self.counter)

        except Exception as err:
            self.DEBUG.set_value("Last exception msg logged", err)
