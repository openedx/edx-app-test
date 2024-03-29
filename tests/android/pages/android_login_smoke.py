"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import strings
from tests.common.globals import Globals


class AndroidLoginSmoke:
    """
    Login Smoke Test cases

    """

    def test_check_login_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login

        Arguments:
            set_capabilities: it will setup environment capabilities based on
            environment given, and return driver object accessible in all Tests
            setup_logging (logger): logger object
        """

        global_contents = Globals(setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        setup_logging.info(f'Starting {AndroidLoginSmoke.__name__} Test Case')
        if login and global_contents.whats_new_enable:
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        else:
            android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')
