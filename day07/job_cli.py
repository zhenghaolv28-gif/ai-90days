import csv
import json
from pathlib import Path

def load_jobs_from_json(file_path):                            #读取JSON
    with open(file_path, "r", encoding="utf-8") as file:        
        return json.load(file)

def get_filter_conditions():
    target_city = input("请输入目标城市：")
    min_salary = int(input("请输入最低月薪："))
    target_skill = input("请输入技能关键词：")

    return target_city, min_salary, target_skill

def filter_jobs(jobs, target_city, min_salary, target_skill):
    matched_jobs = []

    for job in jobs:
        city_matches = job["city"] == target_city
        salary_matches = job["salary_min"] >= min_salary
        skill_matches = target_skill in job["skills"]

        if city_matches and salary_matches and skill_matches:
            matched_jobs.append(job)

    return matched_jobs


def display_jobs(matched_jobs):
    
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
csv_path = data_dir / "matched_jobs.csv"

jobs = load_jobs_from_json(json_path)

target_city, min_salary, target_skill = get_filter_conditions()

matched_jobs = filter_jobs(
    jobs,
    target_city,
    min_salary,
    target_skill
)

display_jobs(matched_jobs)

save_jobs_to_csv(matched_jobs, csv_path)

print(f"筛选结果已导出：{csv_path}")