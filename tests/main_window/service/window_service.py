import unittest

from main_window.repository.window_repository_impl import WindowRepositoryImpl
from main_window.service.request.window_create_request import WindowCreateRequest
from main_window.service.window_service_impl import WindowServiceImpl


class TestWindowServiceImpl(unittest.TestCase):

    def test_create_start_window(self):
        window_service = WindowServiceImpl.getInstance()
        menu_name = "TestMenu"

        window_service.createStartWindow(menu_name)

        window_service.createStartWindow(
            menu_name
        )

if __name__ == '__main__':
    unittest.main()
