Implement the compare_version function, which compares the passed versions version1 AND version2. If version1 › version2, then the function should return 1, if version1 ‹ version2, TO -1, if version1 = version2 — 0.
A version is a string in which two numbers (major and minor versions) are separated by a period, for example: 12.11.
It is important to understand that a version is not a floating point number, but several numbers not related to each other.
The greater/less check is done by comparing each number independently. Therefore, version 0.12 is greater than version o.2.

Example:

compare_version("0.1", "0.2") # -1
compare_version("0.2", "0.1") # 1
compare_version("4.2", "4.2") # 0