from sugar_asynctest import AsyncTestCase

class TestAsyncTestCase(AsyncTestCase):

    async def test_blank(self):
        assert True == True

class TestAsyncTestCaseDefaultLoop(AsyncTestCase):

    default_loop = True

    async def test_blank(self):
        assert True == True
