nickname = input("请输入你的昵称：")
days = int(input("请输入计划学习天数："))
min_hours_per_day = float(input("请输入每天最少学习小时："))
max_hours_per_day = float(input("请输入每天最多学习小时："))

min_total_hours = days * min_hours_per_day
max_total_hours = days * max_hours_per_day
meets_goal =  min_total_hours >= 180

print(f"学习者：{nickname}")
print(f"计划学习天数：{days}天")
print(f"每天学习时间：{min_hours_per_day}-{max_hours_per_day}小时")
print(f"预计总学习时间：{min_total_hours}-{max_total_hours}小时")
print(f"最少学习时间是否达到180小时:{meets_goal}")