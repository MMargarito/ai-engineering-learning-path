import csv
import platform
from pathlib import Path

cwd = Path.cwd()
p = platform.platform()
py_v = platform.python_version()
script_dir = Path(__file__).resolve().parent  
file_path = script_dir.parent/"lesson-01-roles/job_skills.csv"


    
def main():
    with open(file_path, newline='') as job_skills:
        skills_reader = csv.DictReader(job_skills)
        skills_data = [row["skill"] for row in skills_reader]
    
    print(f"Python version: {py_v}")
    print(f"Platform: {p}")
    print(f"Working directory: {cwd}")
    print(f"Skill rows: {len(skills_data)}")
    
if __name__ == "__main__":
    main()
