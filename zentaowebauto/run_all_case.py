import unittest
from common.HTMLReport import HTMLTestRunner
import os
curdir = os.path.dirname(os.path.realpath(__file__))
print(curdir)

casepath = os.path.join(curdir, "cases")
reportpath = os.path.join(curdir, "report", "resultaaaaa.html")

# 查找符合规则的
discover = unittest.defaultTestLoader.discover(start_dir=casepath ,
                                    pattern="test*.py")
print(discover)

# reportpath = "E:\\testzentaopro\\report\\result.html"
fp = open(reportpath, "wb")
runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="报告的标题",
                        description="报告的描述",
                        retry=4
)
runner.run(discover)
fp.close()




