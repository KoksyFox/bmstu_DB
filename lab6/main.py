import database

def menu():
    print("Choose options:")
    print("1 - Scalar query")
    print("2 - Query with JOIN")
    print("3 - CTE")
    print("4 - Query on metadata")
    print("5 - Scalar function")
    print("6 - Table func tion")
    print("7 - Procedure")
    print("8 - System procedure or function")
    print("9 - Create new table")
    print("10 - Insert new data")

    print("\n0 - Exit \n")

if __name__ == "__main__":

    fitness = database.DataBase()

    run = True
    while (run == True):
        menu()

        choice = int(input("Please, input your choice\n"))

        if choice == 1:
            print(fitness.get_number_of_male_visitors())
        elif choice == 2:
            print(fitness.select_all_inf())
        elif choice == 3:
            print(fitness.select_cte_window())
        elif choice == 4:
            print(fitness.select_metadata())
        elif choice == 5:
            print(fitness.scalar_func(25))
        elif choice == 6:
            print(fitness.table_func(21))
        elif choice == 7:
            print(fitness.proc())
        elif choice == 8:
            print(fitness.version())
        elif choice == 9:
            fitness.create_table('types_of_abonemetns')
        elif choice == 10:
            fitness.insert_data('types_of_abonemetns', 'gold', 20000)
        elif choice == 0:
            run = False
