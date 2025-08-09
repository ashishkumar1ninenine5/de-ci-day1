def clean_sum(nums):
    return sum(x for x in nums if x is not None)


def main():
    print("✅ sum =", clean_sum([1, None, 2, 3]))


if __name__ == "__main__":
    main()
