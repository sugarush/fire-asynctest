import unittest
import asyncio


class AsyncTestCase(unittest.TestCase):
    '''
    An asynchronous TestCase class.
    '''

    default_loop = False
    '''
    If set to `True`, the default event loop will be used, otherwise
    a new event loop is created for each test.
    '''

    def setUpEventLoop(self):
        '''
        Either creates a new event loop for each test or uses the
        default event loop.
        '''
        if self.default_loop:
            if not hasattr(self, 'loop'):
                self.loop = asyncio.get_event_loop()
        else:
            if asyncio.get_event_loop().is_running():
                asyncio.get_event_loop().close()
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

    def tearDownEventLoop(self):
        '''
        If we are using the default event loop, close it when tearing
        down.
        '''
        if not self.default_loop:
            self.loop.close()

    async def asyncSetUp(self):
        '''
        Called before each async test is executed.
        '''
        pass

    async def asyncTearDown(self):
        '''
        Called after each async test is executed.
        '''
        pass

    def asyncWrapper(self, func):
        '''
        Sets up the test's event loop, calls `asyncSetUp`, runs the test
        and finally calls `asyncTearDown`.
        '''
        def wrapper():
            self.setUpEventLoop()
            self.loop.run_until_complete(self.asyncSetUp())
            self.loop.run_until_complete(func())
            self.loop.run_until_complete(self.asyncTearDown())
            self.tearDownEventLoop()
        return wrapper

    def __getattribute__(self, name):
        '''
        Allows asynchronous functions to be executed.
        '''
        attr = super(AsyncTestCase, self).__getattribute__(name)
        if name.startswith('test_') and asyncio.iscoroutinefunction(attr):
            return self.asyncWrapper(attr)
        return attr
