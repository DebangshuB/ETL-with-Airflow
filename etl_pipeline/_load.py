import os


def run(HOME):

    with open(os.path.join(HOME, "data", "load_data.sql"), 'w') as file_out:
        with open(os.path.join(HOME, "data", "logs.csv")) as file_in:

            line = next(file_in)
            file_out.write("INSERT IGNORE INTO ETL.openstacketl VALUES ('%s','%s','%s','%s',%s,%s,%s)" %
                           tuple(line.strip("\n").split(",")))

            for line in file_in:
                file_out.write(",('%s','%s','%s','%s',%s,%s,%s)" %
                               tuple(line.strip("\n").split(",")))

            file_out.write(";")

    os.chdir(os.path.join(HOME, "data"))
    os.system("rm *.csv")


if __name__ == "__main__":
    run(os.environ.get("HOME"))
