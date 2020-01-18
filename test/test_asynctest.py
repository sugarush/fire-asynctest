from fire_asynctest import AsyncTestCase

class TestAsyncTestCaseDefaultLoop(AsyncTestCase):

    default_loop = True

    async def test_blank(self):
        assert True == True

class TestAsyncTestCaseNewEventLoop(AsyncTestCase):

    async def test_blank(self):
        assert True == True
