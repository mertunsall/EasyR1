import re

def exact_match_format_reward(predict_str: str) -> float:
    pattern = re.compile(r"<think>.*?</think>\s*<answer>.*?</answer>", re.DOTALL)
    format_match = re.fullmatch(pattern, predict_str)
    return 1.0 if format_match else 0.0

def exact_match_accuracy_reward(predict_str: str, ground_truth: str) -> float:
    try:
        ground_truth = ground_truth.strip('\n').lower()
        content_match = re.search(r"<answer>(.*?)</answer>", predict_str)
        given_answer = content_match.group(1).strip('\n').lower() if content_match else predict_str.strip()
        if ground_truth == given_answer:
            return 1.0
    except Exception:
        pass

    return 0.0

def exact_match_compute_score(predict_str: str, ground_truth: str) -> float:
    return 0.5 * exact_match_accuracy_reward(predict_str, ground_truth) + 0.5 * exact_match_format_reward(predict_str)