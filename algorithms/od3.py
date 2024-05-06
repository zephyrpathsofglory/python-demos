"""
某公司组织一场公开招聘活动，假设由于人数和场地的限制，每人每次面试的时长不等， 并已经安排给定，用
(S1,E1)、(S2,E2)(Sj,Ej)...(Si< Ei，均为非负整数)表示每场面试的开始和结 束时间。

面试采用一对一的方式，即一名面试官同时只能面试一名应试者，一名面试官完成一次 面试后可以立即进行下一
场面试，且每个面试官的面试人次不超过 m。 为了支撑招聘活动高效顺利进行，请你计算至少需要多少名面试
官。

输入描述

输入的第一行为面试官的最多面试人次 m，第二行为当天总的面试场次 n

接下来的 n 行为每场面试的起始时间和结束时间，起始时间和结束时间用空格分隔.

其中，1 <= n,m <= 500

输出描述

输出一个整数，表示至少需要的面试官数量

输入处理
"""

from typing import List


class Solution:
    def least_interviewer(
        self,
        interview_schedule: List[List[int]],
        max_interview: int,
        interview_count: int,
    ) -> int:
        interview_schedule.sort(key=lambda x: x[0])

        buckets = [[] for _ in range(interview_count)]
        for start_time, end_time in interview_schedule:
            for bucket in buckets:
                if len(bucket) == 0 or (
                    len(bucket) < max_interview and bucket[-1] <= start_time
                ):
                    bucket.append(end_time)
                    break
        return len(list(filter(lambda b: len(b) > 0, buckets)))

    def least_interviewer2(
        self,
        interview_schedule: List[List[int]],
        max_interview: int,
        interview_count: int,
    ) -> int:
        interview_schedule.sort(key=lambda x: x[1])

        buckets = [[] for _ in range(interview_count)]
        for start_time, end_time in interview_schedule:
            for bucket in buckets:
                if len(bucket) == 0 or (
                    len(bucket) < max_interview and bucket[-1] <= start_time
                ):
                    bucket.append(end_time)
                    break
        return len(list(filter(lambda b: len(b) > 0, buckets)))


sol = Solution()
assert sol.least_interviewer([[1, 3], [2, 5], [3, 9], [2, 8]], 4, 4) == 3
assert sol.least_interviewer2([[1, 3], [2, 5], [3, 9], [2, 8]], 4, 4) == 3

assert sol.least_interviewer([[1, 7], [3, 10], [2, 5], [4, 6]], 3, 4) == 4
assert sol.least_interviewer2([[1, 7], [3, 10], [2, 5], [4, 6]], 3, 4) == 4

assert sol.least_interviewer([[1, 3], [2, 5]], 2, 2) == 2
assert sol.least_interviewer2([[1, 3], [2, 5]], 2, 2) == 2
