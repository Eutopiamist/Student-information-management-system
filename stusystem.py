# 开发者:Eutopia
# 开发时间:2021/2/5 0017 16:36
import os
filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice=='0':
                answer=input('你确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()#录入学生信息
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def menu():
    print('====================学生信息管理系统====================')
    print('-----------------------功能菜单-----------------------')
    print('\t\t1.录入学生信息')
    print('\t\t2.查找学生信息')
    print('\t\t3.删除学生信息')
    print('\t\t4.修改学生信息')
    print('\t\t5.排序')
    print('\t\t6.统计学生总人数')
    print('\t\t7.显示所有学生信息')
    print('\t\t0.退出系统')
    print('----------------------------------------------------')

def insert():
    student_lst=[]
    while True:
        id=input('请输入学生学号（如1001）：')
        if not id:#用布尔值判断空字符串
            print('学号不能为空！！')
            continue
        name=input('请输入学生姓名：')
        if not name:
            print('姓名不能为空！！')
            continue

        try:
            chinese=int(input('请输入语文成绩：'))
            math=int(input('请输入数学成绩：'))
            english=int(input('请输入英语成绩：'))
        except:
            print('输入错误，不是整数类型，请重新输入')
            continue#返回while true重新输入
        #将录入的学生信息保存到字典中
        student={'学号':id,'姓名':name,'语文':chinese,'数学':math,'英语':english}
        #将学生信息添加到列表中
        student_lst.append(student)
        answer=input('是否继续添加？y/n')
        if answer=='y':
            continue
        else:
            break

    #调用save()函数
    save(student_lst)
    print('学生信息录入成功！！！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')#以追加模式打开文件，同时避免中文乱码，加上encoding
    except:
        stu_txt=open(filename,'w',encoding='utf-8')#如果没有文件，以写入模式打开
    for item in lst:#遍历防止多条信息写入
        stu_txt.write(str(item)+'\n')#将每条信息写入文件，同时换行
    stu_txt.close()#此时保存操作完成

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            model=input('按学号查找请输入1，按姓名查找请输入2')
            if model=='1':
                id=input('请输入学生学号：')
            elif model=='2':
                name=input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入！！！')
                search()
            with open(filename,'r',encoding="utf-8") as sfile:
                students=sfile.readlines()
                for item in students:
                    d=dict(eval(item))
                    if id!='':#通过不等于判断使用的是哪种查询方式
                        if d['学号']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['姓名']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()#每次使用清空表格，保持整洁
            answer=input('是否继续查询？y/n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息！！！')
            return
def show_student(lst):
    if len(lst)==0:#根据列表长度判断内容
        print('没有查询到学生信息！！！')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(format_title.format('学号','姓名','语文成绩','数学成绩','英语成绩','总成绩'))
    #定义内容显示格式
    format_date='{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
    for item in lst:
        print(format_date.format(item.get('学号'),
                                 item.get('姓名'),
                                 item.get('语文'),
                                 item.get('数学'),
                                 item.get('英语'),
                                 int(item.get('语文'))+int(item.get('数学'))+int(item.get('英语'))))

def delete():
    while True:
        student_id=input('请输入要删除的学生的学号')
        if student_id!='':#判断学生学号存在
            if os.path.exists(filename):#判断磁盘上文件存在
                with open(filename,'r',encoding='utf-8')as file:
                    student_old=file.readlines()#文件存在读取内容
            else:
                student_old=[]#文件不存在列表设为空
            flag=False #标记是否删除
            if student_old:#用布尔值判断列表有内容
                with open(filename,'w',encoding='utf-8')as dfile:#全部遍历全部重写
                    d={}
                    for item in student_old:
                        d=dict(eval(item))#将字符串转成字典
                        if d['学号']!=student_id:
                            dfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'学号为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到学号为{student_id}的学生信息！！')
            else:
                print('系统内无学生信息！！')
                break
            show()#删除后显示全部学生信息
            answer=input('是否继续删除？y/n')
            if answer=='y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as mfile1:
            student_old=mfile1.readlines()
    else:
        return
    student_id=input('请输入要修改的学生的学号:')
    with open(filename,'w',encoding='utf-8') as mfile2:
        for item in student_old:
            d=dict(eval(item))
            if d['学号']==student_id:
                print('已找到该学生信息，现在您可以开始修改了！')
                while True:
                    try:
                        d['姓名']=input('请输入学生姓名：')
                        d['语文']=int(input('请输入语文成绩：'))
                        d['数学']=int(input('请输入数学成绩：'))
                        d['英语']=int(input('请输入英语成绩：'))
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                mfile2.write(str(d)+'\n')
                print('修改成功！！！')
            else:
                mfile2.write(str(d)+'\n')
        answer=input('是否继续修改其他学生信息？y/n')
        if answer=='y':
            modify()

def sort():
    show()
    student_new=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
            for item in student_list:
                student_new.append(eval(item))
    else:
        return
    sel_model=input('请选择(0.升序 1.降序):')
    if sel_model=='0':
        sel_model_bool=False
    elif sel_model=='1':
        sel_model_bool=True
    else:
        print('您的输入有误，请重新输入！！！')
        sort()

    sel_type=input('请选择(1.按语文成绩排序 2.按数学成绩排序 3.按英语成绩排序 4.按总成绩排序)')
    if sel_type=='1':
        student_new.sort(key=lambda x:int(x['语文']),reverse=sel_model_bool)
    elif sel_type=='2':
        student_new.sort(key=lambda x:int(x['数学']),reverse=sel_model_bool)
    elif sel_type=='3':
        student_new.sort(key=lambda x:int(x['英语']),reverse=sel_model_bool)
    elif sel_type=='4':
        student_new.sort(key=lambda x:int(x['语文'])+int(x['数学'])+int(x['英语']),reverse=sel_model_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:#不为空列表
                print(f'系统中一共有{len(students)}名学生信息')
            else:
                print('暂未保存学生信息！！！')
    else:
        print('暂未保存学生信息！！！')
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)#借用之前定义show_student函数

if __name__ == '__main__':
    main()