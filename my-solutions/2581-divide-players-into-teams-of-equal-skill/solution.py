class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        skill_length_half = len(skill) / 2
        arr = [0] * skill_length_half
        ans = 0
        arr[0] = [skill[0], skill[-1]]
        print(arr)
        for i in range(1,skill_length_half):
            print(skill[i],skill[-i-1])
            if skill[i] + skill[-i-1] == sum(arr[0]):
                print(i)
                arr[i] = [skill[i],skill[-i-1]]
            else:
                return -1

        for i in arr:
            ans += i[0] * i[1]
        print(ans,arr)
        return ans
