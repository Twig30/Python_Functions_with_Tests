import sys

from module import two_sum  # Change this import
FUNCTION_TO_TEST = two_sum  # Change this function name

TESTS = [
    # Format:
    # ( (arguments as tuple), expected_output )
    ((2, 3), 5),
    ((-1, 1), 0),
    ((0, 0), 0),
    ((10000, 2345), 12345),
    ((-24, -12), -36)
]

# ==========================================
# 🚫 DO NOT EDIT BELOW THIS LINE
# ==========================================


def run_all_tests():
    one_or_more_failures = False

    for i, (inputs, expected) in enumerate(TESTS):
        if one_test_success(inputs, expected):
            print(f"Test {i}: Pass!")
        else:
            print(f"Test {i}: Fail")
            one_or_more_failures = True
        print()

    print("\n-------------------------")

    if one_or_more_failures:
        print("❌ One or more tests failed.")
    else:
        print("✅ All tests passed!")


def one_test_success(inputs, expected):
    try:
        actual = FUNCTION_TO_TEST(*inputs)
        print(f"Expected: {expected}, Got: {actual}")
        assert actual == expected
        return True
    except Exception as e:
        # print(f"Error: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)