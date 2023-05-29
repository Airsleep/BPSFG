import os
import time
import re
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

boj_base_url = "https://www.acmicpc.net/problem/"


def get_problem_info(link):
    tlink = link.split("/")
    if len(tlink) != 5:
        print(
            "wrong address - address format should be https://www.acmicpc.net/problem/xxx"
        )
        return

    problem_id = tlink[4]
    if not problem_id.isdigit():
        print("wrong address")
        return
    boj_problem_api_url = "https://solved.ac/api/v3/problem/show"
    query_string = {"query": " ", "problemId": f"{problem_id}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "GET", boj_problem_api_url, headers=headers, params=query_string
    )
    if response.ok:
        print("-----successfully got problem info-----")
        temp_problem_json = json.loads(response.text)
        problem_title = str(temp_problem_json.get("titleKo"))
        return int(problem_id), problem_title
    else:
        print("failed get problem info")
    return 0, None
    # bp_response = requests.get(link)
    # bp_html = bp_response.text
    # bp_soup = BeautifulSoup(bp_html, "html.parser")
    # problem_title = bp_soup.find("span", {"id": "problem_title"})
    # print(bp_soup)
    # print(problem_title)


def make_file(problem_id, problem_title):
    print("current directory:")
    print("##" + os.getcwd() + "##")
    file_extension = ""
    while True:
        print("select language (1: cpp, 2: python)")
        sl = int(input())
        if sl == 1:
            file_extension = "cpp"
            break
        elif sl == 2:
            file_extension = "py"
            break
        else:
            print("wrong input")
    if problem_id != 0 and problem_title != None:
        file_name = str(problem_id) + "." + file_extension
        if os.path.isfile(file_name):
            print("problem file already exist")
        else:
            f = open(file_name, "w", encoding="UTF-8")
            if file_extension == "cpp":
                f.write("// problem: " + problem_title + "\n")
                f.write("// id: " + str(problem_id) + "\n")
                f.write("// time taken:\n")
                f.write("#include <bits/stdc++.h>\n")
                f.write("using namespace std;\n")
                f.write("int main(void)\n")
                f.write("{\n")
                f.write("    ios::sync_with_stdio(false);\n")
                f.write("    cin.tie(nullptr);\n")
                f.write("\n")
                f.write("    return 0;\n")
                f.write("}\n")
            elif file_extension == "py":
                f.write("# problem: " + problem_title + "\n")
                f.write("# id: " + str(problem_id) + "\n")
                f.write("# time taken:")
            f.close()

    else:
        print("problem unsellected")
