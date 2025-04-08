#!/usr/bin/env python3

def is_continuous_sequence(seq):
    if (
        not isinstance(seq, list)
        or len(seq) < 2
        or not all(isinstance(x, int) and not isinstance(x, bool) for x in seq)
    ):
        return False

    sorted_seq = sorted(seq)
    for i in range(1, len(sorted_seq)):
        if sorted_seq[i] - sorted_seq[i - 1] != 1:
            return False
    return True

def main():
    print(is_continuous_sequence([4, 5, 6, 7]))     # True
    print(is_continuous_sequence([1, 2, 4]))        # False
    print(is_continuous_sequence(["a", "b", "c"]))  # False

if __name__ == "__main__":
    main()
