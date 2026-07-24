import csv
import json
from pathlib import Path

initial_jobs = [
    {
        "title":"AI应用助理",
        "company":"阿里巴巴",
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

def save_jobs_to_json(jobs, file_path):                        #保存JSON
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            jobs,
            file,
            ensure_ascii=False,
            indent=2
        )

def load_jobs_from_json(file_path):                            #读取JSON
    with open(file_path, "r", encoding="utf-8") as file:        
        return json.load(file)

def save_jobs_to_csv(jobs, file_path):                          #导出CSV
    fieldnames = [
        "title",
        "company",
        "city",
        "salary_min",
        "salary_max",
        "skills"
    ]

    with open(
        file_path,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for job in jobs:
            row = job.copy()
            row["skills"] = "|".join(job["skills"])
            writer.writerow(row)

data_dir = Path(__file__).parent
json_path = data_dir / "jobs.json"
csv_path = data_dir / "jobs.csv"

if not json_path.exists():
    save_jobs_to_json(initial_jobs, json_path)
    print("首次运行：已经创建 jobs.json")

jobs = load_jobs_from_json(json_path)

save_jobs_to_csv(jobs, csv_path)

print(f"成功读取 {len(jobs)} 个岗位")
print(
    f"第一个岗位："
    f"{jobs[0]['title']}｜"
    f"{jobs[0]['company']}"
)
print(f"JSON 文件：{json_path}")
print(f"CSV 文件：{csv_path}")