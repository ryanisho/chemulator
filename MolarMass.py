from FindElem import FindElem
import re

class MolarMass:
	def calcMass(compound):
		total = 0

		ele = []
		nums = []

		i = 0
		while i < len(compound):
			if ((compound[i] >= 'A' and compound[i] <= 'Z') and (compound[i + 1] >= 'a' and compound[i + 1] <= 'z')):
				ele.append(compound[i:i+2])
				i += 1
			elif (compound[i] >= 'A' and compound[i] <= 'Z'):
				ele.append(compound[i:i+1])
			elif (compound[i] >= '1' and compound[i] <= '9'):
				nums.append(int(re.search(r'\d+', compound[i]).group()))
			i += 1

		j = 0
		while j < len(nums):
			total += FindElem.findMass(ele[j]) * nums[j]
			j += 1

		return(total)