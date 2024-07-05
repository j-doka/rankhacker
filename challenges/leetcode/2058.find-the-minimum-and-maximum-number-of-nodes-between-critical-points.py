#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
#
# algorithms
# Medium (58.64%)
# Likes:    873
# Dislikes: 41
# Total Accepted:    76.7K
# Total Submissions: 117.5K
# Testcase Example:  '[3,1]'
#
# A critical point in a linked list is defined as either a local maxima or a
# local minima.
# 
# A node is a local maxima if the current node has a value strictly greater
# than the previous node and the next node.
# 
# A node is a local minima if the current node has a value strictly smaller
# than the previous node and the next node.
# 
# Note that a node can only be a local maxima/minima if there exists both a
# previous node and a next node.
# 
# Given a linked list head, return an array of length 2 containing
# [minDistance, maxDistance] where minDistance is the minimum distance between
# any two distinct critical points and maxDistance is the maximum distance
# between any two distinct critical points. If there are fewer than two
# critical points, return [-1, -1].
# 
# 
# Example 1:
# 
# 
# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].
# 
# 
# Example 2:
# 
# 
# Input: head = [5,3,1,2,5,1,2]
# Output: [1,3]
# Explanation: There are three critical points:
# - [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3
# and 2.
# - [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than
# 2 and 1.
# - [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5
# and 2.
# The minimum distance is between the fifth and the sixth node. minDistance = 6
# - 5 = 1.
# The maximum distance is between the third and the sixth node. maxDistance = 6
# - 3 = 3.
# 
# 
# Example 3:
# 
# 
# Input: head = [1,3,2,2,3,2,2,2,7]
# Output: [3,3]
# Explanation: There are two critical points:
# - [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater
# than 1 and 2.
# - [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater
# than 2 and 2.
# Both the minimum and maximum distances are between the second and the fifth
# node.
# Thus, minDistance and maxDistance is 5 - 2 = 3.
# Note that the last node is not considered a local maxima because it does not
# have a next node.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [2, 10^5].
# 1 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        node = head
        idx = 2

        while node and node.next and node.next.next:
            if (node.next.val > node.val and node.next.val > node.next.next.val) or (node.next.val < node.val and node.next.val < node.next.next.val):
                critical_points.append([node.next, idx])
                
            idx += 1
            node = node.next

        if len(critical_points) < 2:
            return [-1, -1]

        if len(critical_points) == 2:
            distance = critical_points[0][1] - critical_points[1][1]
            return [distance, distance]
        else:
            # max distance fist and last critical points
            max_distance = critical_points[-1][1] - critical_points[0][1]

            # for each critical point, calculate the distance to the next critical point

            min_distance = float('inf')
            for i in range(len(critical_points) - 1):
                distance = critical_points[i + 1][1] - critical_points[i][1]
                min_distance = min(min_distance, distance)

        return [min_distance, max_distance]
# @lc code=end

