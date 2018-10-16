import unittest
import identidock
class TestCase(unittest.TestCase):
  def setUp(self):
    print ("test setup", flush=True)
    identidock.app.config["TESTING"] = True
    self.app = identidock.app.test_client()
  def test_get_mainpage(self):
    print ("test getmain", flush=True)
    page = self.app.post("/", data=dict(name="Moby Dock"))
    assert page.status_code == 200
    assert 'Hello' in str(page.data)
    assert 'Moby Dock' in str(page.data)
  def test_html_escaping(self):
    print ("test escape", flush=True)
    page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
    assert '<b>' not in str(page.data)
if __name__ == '__main__':
  unittest.main()
