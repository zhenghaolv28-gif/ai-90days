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
print(f"岗位总数：{len(jobs)}")

first_job = jobs[0]

print(f"第一个岗位名称：{first_job['title']}")
print(f"第一个岗位公司：{first_job['company']}")
print(
    f"第一个岗位薪资："
    f"{first_job['salary_min']}-{first_job['salary_max']}元"
)

print(f"第三个岗位技能：{jobs[2]['skills']}")

all_skills = (
    jobs[0]["skills"]
    + jobs[1]["skills"]
    + jobs[2]["skills"]
    + jobs[3]["skills"]
    + jobs[4]["skills"]
)

unique_skills = set(all_skills)

print(f"去重后的技能：{unique_skills}")