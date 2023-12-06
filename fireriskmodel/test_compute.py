import os
import sys

import unittest
import datetime

import compute
import test_testdata

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import datamodel.utils as dmutils
import datamodel.model as dm
import weatherdata.utils as wdutils

class TestUtil(unittest.TestCase):

    def setUp(self):

        self.observations_wdps = wdutils.interpolate_wdps(dmutils.list_to_wdps(test_testdata.frost_sample_weatherdatapoints),720)

        self.forecast_wdps = wdutils.interpolate_wdps(dmutils.list_to_wdps(test_testdata.met_sample_weatherdatapoints),720)

        self.location = dm.Location(latitude=60.383, longitude=5.3327)

#        print(self.observations_wdps)

    def test_compute_obs(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=self.location,
            data=list())

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)

    def test_compute_fct(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=list())

        forecast = dm.Forecast(
            location=self.location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)

    def test_compute(self):

        observations = dm.Observations(
            source="testdata",
            location=self.location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=self.location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        firerisks = compute.compute(weatherdata)

        print(firerisks)

if __name__ == '__main__':
    unittest.main()