import subprocess
import sys

python = sys.executable  # 自动获取当前Python路径

print("Part 1: The sine function")
subprocess.run([python, "part1_sincurve.py"], cwd=r"D:\CS\python_learning\Taylor_series")

input("Press Enter to continue to Part 2...")

print("Part 2: Taylor series approximation")
subprocess.run([python, "part2_approximation.py"], cwd=r"D:\CS\python_learning\Taylor_series")

input("Press Enter to continue to Part 3...")

print("Part 3: Interactive approximation")
subprocess.run([python, "part3_interactive.py"], cwd=r"D:\CS\python_learning\Taylor_series")