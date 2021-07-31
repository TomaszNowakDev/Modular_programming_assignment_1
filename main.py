import functions


def teacher_name_and_points():
    name = functions.read_non_empty_string("Name of the Teacher ==> ")
    points = functions.read_positive_integer("Number of points ==> ")
    return name, points


def points_earned(table_name):
    points = []
    for i in range(len(table_name)):
        x = functions.read_positive_integer(f'How many points {table_name[i]} earned?\n==>')
        points.append(x)
    return points


def main():
    print("Tomasz Nowak")
    tables = ["Glas", "Dubh", "Gorm", "Dearg"]
    teacher_name, points_for_table = teacher_name_and_points()
    earned_p = points_earned(tables)


if __name__ == '__main__':
    main()
