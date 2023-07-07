import unittest
import os

from HTMLTestRunner_PY3 import HTMLTestRunner

class MarkTest(unittest.TestCase):
    """
    只要class裏面 def 開頭符合 test的就會被列入到測試項目
    如果不符合就不會跑
    """

    def test1Mark(self):
        self.assertFalse(1 == 1)  # FAIL 不符合預期

    def test2Mark(self):
        self.assertFalse(1 == 2)  # PASS 符合預期

    def test3Mark(self):
        self.assertTrue(1 == 2)  # FAIL 不符合預期

    def test4Mark(self):
        self.assertTrue(3 == 3)  #  PASS 符合預期

    def test5Mark(self):
        test('测试报告.png')  # Error 錯誤


if __name__ == '__main__':

    report_title = '我是一個報告標題'
    desc = '可以敘述此報告用途是做什麼'
    report_file = 'test_report.html'

    """
    針對你要執行的TestCase加入到suite內，透過.addTest()的方法
    這裡的話，只會針對test3Mark, test4Mark, test5Mark進行執行
    """
    suite = unittest.TestSuite()
    suite.addTest(MarkTest('test3Mark'))
    suite.addTest(MarkTest('test4Mark'))
    suite.addTest(MarkTest('test5Mark'))

    with open(report_file, 'wb') as report:
        """
        先取得基本資訊 名稱、敘述，接著把所有測試用例跑過一輪，儲存到對應的位置。
        """
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)