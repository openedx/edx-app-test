"""
   Module covers iOS base page
"""

from tests.common.globals import Globals


class IosBasePage:
    """
         Base page for all iOS Pages
    """

    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.global_contents = Globals(setup_logging)
        self.log = setup_logging
        self.discovery_close_button = None
        self.textview_drawer_account_option = None
        self.account_options = None
        self.LOGOUT_OPTION = self.global_contents.fourth_existence
        self.discovery_cancel_button = None
