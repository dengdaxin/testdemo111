import unittest
import HTMLTestRunner
import os
import time
from BeautifulReport import BeautifulReport
current = os.path.dirname(__file__)
report_path = os.path.join(current,'report')
suite = unittest.defaultTestLoader.discover(start_dir='testcase',
                                            pattern='test_*.py',
                                            top_level_dir='testcase')
main_suite = unittest.TestSuite()
main_suite.addTest(suite)
now = time.strftime('%Y_%m_%d_%H_%M_%S')
# file = open(report_path + '/report'+ now +'.html','wb')
# html = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                      title='禅道ui自动化测试',
#                                      description='随意写点描述')
# html.run(main_suite)
# file.close()
filename = 'report'+ now
runner = BeautifulReport(main_suite)
runner.report(filename=filename,description='禅道UI自动化测试',report_dir=report_path,theme='theme_memories')
#默认样式theme_default