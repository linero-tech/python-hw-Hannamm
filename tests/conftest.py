from _pytest.config import Config
from _pytest.terminal import TerminalReporter


def color(percentage: int) -> str:
    red = "D53644"
    green = "31C452"
    yellow = "E47202"

    if percentage == 0:
        return red
    elif percentage == 100:
        return green
    else:
        return yellow


def badge_metadata(test_count: int, success_test_count: int):
    filename = "badge.txt"
    completion_percentage = int((success_test_count / test_count) * 100)

    f = open(filename, "w")
    f.write(f"{completion_percentage}\n{color(completion_percentage)}")
    f.close()


def pytest_terminal_summary(
    terminalreporter: TerminalReporter, exitstatus: int, config: Config
):
    passed_tests = len(terminalreporter.stats.get("passed", []))
    failed_tests = len(terminalreporter.stats.get("failed", []))
    total_tests = passed_tests + failed_tests
    errors = len(terminalreporter.stats.get("error", []))

    if errors > 0:
        print("Badge file not created")
        return
    else:
        badge_metadata(test_count=total_tests, success_test_count=passed_tests)
