# Trevor Bentley        8-3-2025
# Lab 11: Two sum

# This code solves and optomises the two sum function


# ----- Two Loops -----
def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# ----- Two Dictionary -----
def twoSumDict(nums, target):
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# ----- Two all index, native ----- 
def twoSumLoopsAll(nums, target):
    results = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                results.append([i, j])
    return results

# ----- Two all index, optomized -----
def twoSumDictAll(nums, target):
    results = []
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        needed_value = target - num
        if needed_value in seen:
            for idx in seen[needed_value]:
                results.append([idx, i])
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    return results
# ----- Lobotomizing Main FXN -----
def main():
    numbies = [2, 7, 11, 15, 3, 6, 1, 5]
    target = 8

    print("twoSumLoops:", twoSumLoops(numbies, target))
    print("twoSumDict:", twoSumDict(numbies, target))
    print("twoSumLoopsAll:", twoSumLoopsAll(numbies, target))
    print("twoSumDictAll:", twoSumDictAll(numbies, target))
# ----- Main callback -----
if __name__ == "__main__":
    main()