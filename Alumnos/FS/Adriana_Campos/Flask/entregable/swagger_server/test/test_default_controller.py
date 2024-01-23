# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_last_meassure_by_sensor_sensor_get(self):
        """Test case for get_last_meassure_by_sensor_sensor_get

        Obtener la última medición de temperatura para un sensor específico.
        """
        response = self.client.open(
            '/getLastMeassureBySensor/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
