
Bookkeeping = []
def show_menu():
    """显示菜单选项"""
    print("\n" + "*" * 30)
    print("欢迎使用记账小程序")
    print("*" * 30)
    print("1、添加收入")
    print("2、添加支出")
    print("3、查看记录")
    print("4、查看统计")
    print("5、退出")
    print("*" * 30)


# show_menu()

def add_income():
    """添加收入"""
    income = input("\n请输入收入金额:")
    income_type = input("请输入类型:")
    remark = input("请输入备注:")
    income_item = {
        "income": income,
        "income_type": income_type,
        "remark": remark
    }

    Bookkeeping.append(income_item)
    print("√添加成功")

    # print(Bookkeeping)


# add_income()

def add_expense():
    """添加支出"""
    expense = input("\n请输入支出金额:")
    expense_item = {
        "expense": expense,
    }

    Bookkeeping.append(expense_item)
    print("√添加成功")
    # print(Bookkeeping)


# add_expense()

def view_records():
    if not Bookkeeping:
        print("\n当前没有记录")
        return
    print("收入/支出列表")
    for index, book in enumerate(Bookkeeping, 1):
        print(f"{index}{Bookkeeping[index - 1]}")


# view_records()

def view_stats():
    symmery = {}
    for item in Bookkeeping:
        # print(item.get('income'),item.get('expense'))
        #
        for key, value in item.items():
            if key in ("income", "expense"):
                num = float(value)
                if key in symmery:
                    symmery[key] += num
                else:
                    symmery[key] = num

    income_total = symmery.get('income', 0)
    expense_total = symmery.get('expense', 0)
    balance = income_total - expense_total
    print(f"【财务统计】 总收入: {income_total}  总支出: {expense_total}  当前余额：{balance}")
    # print(f"支出: {expense_total}")

    # print(f"收入: {symmery['income']}\n支出: {symmery['expense']}")

    # Bookkeeping[income] += num
    # Bookkeeping[expense] += num


# view_stats()

def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("\n请选择操作 (1-5): ").strip()

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_records()
        elif choice == '4':
            view_stats()
        elif choice == '5':
            print("\n感谢使用，再见！")
            break
        else:
            print("\n无效的选择，请重新输入！")


if __name__ == "__main__":
    main()


