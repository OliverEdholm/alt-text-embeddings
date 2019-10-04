import re


def _get_n_digits(alt_text):
    digits = list('0123456789')
    return sum([int(c in digits)
                for c in alt_text])


def _get_n_special_chars(alt_text):
    special_chars = list('!"#€%&/()=+?^.,;:-_@')
    return sum([int(c in special_chars)
                for c in alt_text])


def _get_n_chinese_chars(alt_text):
    return sum([len(section)
                for section in re.findall(r'[\u4e00-\u9fff]+', alt_text)])


def is_valid(alt_text):
    if _get_n_digits(alt_text) > 4:
        return False
    elif _get_n_special_chars(alt_text) > 3:
        return False
    elif _get_n_chinese_chars(alt_text) > 1:
        return False
    elif len(alt_text) > 75:
        return False
    elif len(alt_text) < 3:
        return False
    
    return True