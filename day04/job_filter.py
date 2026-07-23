jobs = [
    {
        "title":"AI应用助理",
        "company":"字节跳动",
        "city":"深圳",
        "salary_min":6000,
        "salary_max":12000,
        "skills":["Python","RAG","SQL"]

    },
    {
        "title":"数据分析师",
        "company":"火山",
        "city":"北京",
        "salary_min":5000,
        "salary_max":8000,
        "skills":["Python","SQL","Excel"]  
    },
    {
        "title":"AI应用助理",
        "company":"腾讯",
        "city":"深圳",
        "salary_min":8000,
        "salary_max":15000,
        "skills":["Python","RAG","SQL","vs code"]
    },
    {
        "title":"AI应用生成师",
        "company":"小米",
        "city":"武汉",
        "salary_min":8000,
        "salary_max":16000,
        "skills":["Python","RAG","SQL"]
    },
    {
        "title":"AI工程师",
        "company":"月之暗面",
        "city":"北京",
        "salary_min":7000,
        "salary_max":13000,
        "skills":["Python","RAG","SQL"]
    }
]
target_city = input("请输入目标城市：")
min_salary = int(input("请输入最低月薪："))
target_skill = input("请输入技能关键词：")

matched_jobs = []

for job in jobs:
    city_matches = job["city"] == target_city
    salary_matches = job["salary_min"] >= min_salary
    skill_matches = target_skill in job["skills"]

    if city_matches and salary_matches and skill_matches:
        matched_jobs.append(job)

print(f"共找到 {len(matched_jobs)} 个匹配岗位")

if len(matched_jobs) == 0:
    print("没有找到符合条件的岗位")
else:
    for job in matched_jobs:
        print(
            f"{job['title']}｜"
            f"{job['company']}｜"
            f"{job['city']}｜"
            f"{job['salary_min']}-{job['salary_max']}元"
        )
