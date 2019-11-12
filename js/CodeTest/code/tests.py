from input_code import solution

def get_test_cases():
    return {
        "SMALL_INPUT": [1, 2, 3],
        "LARGE_INPUT": [1, 2, 3] * 1000 + [4],
    }

def get_expected_outputs():
    return {
        "SMALL_INPUT": 3,
        "LARGE_INPUT": 4,
    }

def test_code():
    test_cases = get_test_cases()
    expected = get_expected_outputs()
    test_cases_count = len(test_cases)
    passed_test_cases = 0
    failed_test_cases = []

    for label in test_cases.keys():
        code_result = solution(test_cases[label])
        if code_result == expected[label]:
            passed_test_cases += 1
        else:
            failed_test_cases.append(label)

    print("Passed", passed_test_cases, "out of", test_cases_count, "test cases.")
    
    if len(failed_test_cases) > 0:
        print("Test cases not passed:", ", ".join(failed_test_cases))

test_code()