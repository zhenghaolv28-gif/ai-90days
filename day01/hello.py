nickname = "Deku"
target_role = "AI应用开发相关岗位"

days = 90
min_hours_per_day =2
mix_hours_per_day = 5

min_total_hours = days * min_hours_per_day
max_total_hours = days * max_hours_per_day

print(f"我的名字:{nickname}")
print(f"目标岗位:{target_role}")
print(f"每天学习时间:{min_hours_per_day}-{max_hours_per_day}")
print(f"90天预计学习时间:{min_total_hours}-{max_total_hours}")
