class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        no_of_employees = 0
        for i in hours:
            if i >= target:
                no_of_employees += 1
        return no_of_employees


s = Solution()
print(s.numberOfEmployeesWhoMetTarget([0,1,2,3,4],2))
