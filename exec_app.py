from util.BS import get_problem_info, make_file
import os

cur_wd = r"C:\Users\gnaro\OneDrive\바탕 화면\Solvedac_practice\With_Levels\Temp"
cur_user = "gnaroshi"
problem_id = 0
problem_title = None
problem_list = []


def exec(cur_wd, cur_user, problem_id, problem_title, problem_list):
    while True:
        print("1: select working directory")
        print("2: select boj problem")
        print("3: select multiple boj problem")
        print("4: clear selected boj problem")
        print("5: make file")
        print("6: show selected boj problems")
        print("7: quit")
        print("-" * 60)
        n = int(input())
        if n == 0:
            print(os.getcwd())
        elif n == 1:
            print("current directory:")
            print("##" + os.getcwd() + "##")
            while True:
                print("1: change directory")
                print("2: cancel")
                try:
                    a = int(input())
                    if a == 1:
                        print("input new directory:")
                        t_wd = input()
                        cur_wd = t_wd
                        print("changed working directory: ")
                        print(cur_wd)
                        os.chdir(cur_wd)
                        break
                    elif a == 2:
                        break
                    else:
                        print("undecidable")
                except:
                    print("undecidable")

        elif n == 2:
            link = input()
            problem_id, problem_title = get_problem_info(link)

            # TODO make dup file warning
            if problem_id == 0 and problem_title == None:
                print("-----problem is not sellected-----")
            else:
                print("problem id: " + str(problem_id))
                print("problem title: " + problem_title)

        elif n == 3:
            print("how many?")
            m = int(input())
            for i in range(m):
                print("input " + str(i) + "boj problem link")
                link = input()
                problem_id, problem_title = get_problem_info(link)

                # TODO make dup file warning
                if problem_id == 0 and problem_title == None:
                    print("-----problem is not sellected-----")
                else:
                    print("problem id: " + str(problem_id))
                    print("problem title: " + problem_title)
                problem_list.append([problem_id, problem_title])

        elif n == 4:
            print("problem list cleared")
            problem_list = []
            problem_id = 0
            problem_title = None

        elif n == 5:
            if len(problem_list) != 0:
                for temp_problem in problem_list:
                    print(temp_problem)
                    make_file(temp_problem[0], temp_problem[1])
            else:
                make_file(problem_id, problem_title)
        elif n == 6:
            if len(problem_list) > 1:
                print("listed problem size: " + str(len(problem_list)))
                cnt = 1
                for i, t in problem_list:
                    print(str(cnt) + "::")
                    print("problem id: " + str(i))
                    print("problem title: " + t)
                    cnt += 1
            elif problem_id != 0 and problem_title != None:
                print("there is one selected boj problem")
                print("problem id: " + str(problem_id))
                print("problem title: " + problem_title)
            else:
                print("none of selected boj problem")

        elif n == 7:
            print("-" * 60)
            print("program terminate")
            print("-" * 60)
            break
        else:
            print("undecidable")
        print("-" * 60)


if __name__ == "__main__":
    os.chdir(cur_wd)

    exec(cur_wd, cur_user, problem_id, problem_title, problem_list)
