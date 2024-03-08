class Solution:
  def find_digital_root(self, A):
      if A // 10 == 0:
          return A
      temp = 0
      while A > 0:
          temp += A % 10
          A = A // 10
      return self.find_digital_root(temp)

  def solve(self, A):
      ans = self.find_digital_root(A)
      return ans

# Get input from the user
A = int(input("Enter a number: "))

# Create an instance of the Solution class
solution = Solution()

# Call the solve method and print the result
print(solution.solve(A))