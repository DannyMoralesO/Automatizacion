from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from Prueba import PruebaTest

prueba_test = TestLoader().loadTestsFromTestCase(PruebaTest)
testList = TestSuite([prueba_test])

kwargs = {
    "output" : '',
    "report_name": '',
    'failfast': 'true'
}

runner = HTMLTestRunner(**kwargs) 
runner.run(testList) 