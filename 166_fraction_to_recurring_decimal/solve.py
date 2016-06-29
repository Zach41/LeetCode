#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""
        result = ""
        if float(numerator) / denominator < 0:
            result += "-"
        num1, num2 = abs(numerator), abs(denominator)

        r = num1 % num2
        result += str(num1/num2)
        if (r==0):
            return result
        result += "."

        pos_map = {}
        pos = 0
        while r != 0:
            if pos_map.has_key(r):
                p = pos_map[r]
                temp = result.split(".")
                result = temp[0] + "."+ temp[1][:p] + "(" + temp[1][p:] + ")"
                break
            pos_map[r] = pos
            pos += 1
            result += str(r*10/num2)
            r= (r*10) % num2
        return result

s = Solution()
print s.fractionToDecimal(1, 2)
print s.fractionToDecimal(2, 1)
print s.fractionToDecimal(2, 3)
print s.fractionToDecimal(9, 17)
print s.fractionToDecimal(1, 6)
        
