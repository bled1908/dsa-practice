# -*- coding: utf-8 -*-
import os
import re

def get_problem_links_from_folder(folder):
    problem_links = []
    for file in os.listdir(folder):
        if file.endswith(".py"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                content = f.read()
                # Extract problem details from the header docstring
                problem_match = re.search(r"Problem:\s*(.*)", content)
                platform_match = re.search(r"Platform:\s*(.*)", content)
                link_match = re.search(r"Link:\s*(.*)", content)
                difficulty_match = re.search(r"Difficulty:\s*(.*)", content)
                if problem_match and link_match:
                    problem_links.append({
                        "title": problem_match.group(1).strip(),
                        "platform": platform_match.group(1).strip() if platform_match else "",
                        "link": link_match.group(1).strip(),
                        "difficulty": difficulty_match.group(1).strip() if difficulty_match else ""
                    })
    return problem_links

def update_readme():
    repo_path = os.getcwd()
    readme_path = os.path.join(repo_path, "README.md")

    # Auto-detect all folders in repo (only topic folders)
    topic_folders = [
        f for f in os.listdir(repo_path)
        if os.path.isdir(f) and not f.startswith(".") and f.lower() not in ["venv", "__pycache__"]
    ]

    table = "| Topic | Problems Solved | Problem Links |\n"
    table += "|-------|-----------------|---------------|\n"

    total_solved = 0
    total_problems = 0

    for folder in sorted(topic_folders):
        problems = get_problem_links_from_folder(folder)
        solved = len(problems)
        total_solved += solved
        # You can set target problems per topic if you want progress tracking
        target = max(solved, 10)  # default target = 10
        total_problems += target

        problem_links_md = "<br>".join(
            [f"[{p['title']}]({p['link']}) ({p['difficulty']})" for p in problems]
        ) if problems else "—"

        table += f"| {folder} | {solved}/{target} | {problem_links_md} |\n"

    progress = total_solved / total_problems if total_problems > 0 else 0
    progress_bar = "█" * int(progress * 20) + "░" * (20 - int(progress * 20))

    readme_content = f"# 📚 DSA Practice Tracker\n\n" \
                     f"**Total Solved:** {total_solved}/{total_problems}\n\n" \
                     f"**Progress:** {progress*100:.2f}%\n\n" \
                     f"```\n{progress_bar}\n```\n\n" \
                     f"{table}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()