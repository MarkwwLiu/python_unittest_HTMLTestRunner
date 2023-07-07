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

    def mmmmm(self):
        test('ttt')

    def testMMMMM(self):
        test('tttt')


def load_all_case():
    """
    將所有符合在跟目錄底下符合 *.test.py 檔案加入到 all_case 進行回傳動作
    """
    all_case = unittest.defaultTestLoader.discover(os.getcwd() + '/', pattern="*test.py")

    return all_case


if __name__ == '__main__':

    report_title = '我是一個報告標題'
    desc = '可以敘述此報告用途是做什麼'
    report_file = 'test_report.html'

#
    with open(report_file, 'wb') as report:
        """
        先取得基本資訊 名稱、敘述，接著把所有測試用例跑過一輪，儲存到對應的位置。
        """
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(load_all_case())
