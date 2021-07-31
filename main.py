import functions


def teacher_name_and_points():
    name = functions.read_non_empty_string("Name of the Teacher ==> ")
    points = functions.read_positive_integer("Number of points required ==> ")
    return name, points


def points_earned(table_name):
    points = []
    for i in range(len(table_name)):
        x = functions.read_positive_integer(f'How many points {table_name[i]} earned?\n==>')
        points.append(x)
    return points


def bad_behaviour(point_for_t):
    for i in range(len(point_for_t)):
        point_for_t[i] -= 1


def display(nam, tab, poin):
    print(f'Teacher name: {nam}')
    print(f"{'Table':10}{'Points'}")
    print('====================')
    for i in range(len(tab)):
        if poin[i] < 10:
            print(f"{tab[i]:10}{poin[i]:<3}{'*'}")
        else:
            print(f"{tab[i]:10}{poin[i]}")


def friday_movie(minimum, earned):
    lowest_points = min(earned)
    if minimum > lowest_points:
        print("There will be no movie on friday.")
    else:
        print("Hooray! MOVIE ON FRIDAY!")


def main():
    print("Tomasz Nowak")
    tables = ["Glas", "Dubh", "Gorm", "Dearg"]
    teacher_name, points_for_table = teacher_name_and_points()
    earned_p = points_earned(tables)
    bad_behaviour(earned_p)
    display(teacher_name, tables, earned_p)
    friday_movie(points_for_table, earned_p)


if __name__ == '__main__':
    main()
