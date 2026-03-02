import sys

from module import listify  # Change this import
FUNCTION_TO_TEST = listify  # Change this function name

TESTS = [
    ("cat", ["c", "a", "t"]),
    ("", []),
    ("A", ["A"]),
    ("123", ["1", "2", "3"]),
    ("Hi!", ["H", "i", "!"])
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
        actual = FUNCTION_TO_TEST(inputs)
        print(f"Expected: {expected}, Got: {actual}")
        assert actual == expected
        return True
    except Exception as e:
        # print(f"Error: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)