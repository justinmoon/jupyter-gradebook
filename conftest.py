"""
This is the pytest configuration file.

TODO:
* Collect all tests and write Row #1 to the spreadsheet
* Grab just the test name from the nodeid
* Is "when == 'call'" really the right condition?
"""
import pytest

from sheets import record_in_google_sheets

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield

    rep = outcome.get_result()
    if call.when == 'call':
        record_in_google_sheets(rep.nodeid, rep.outcome)
