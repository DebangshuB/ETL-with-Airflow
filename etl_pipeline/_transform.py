import os


"""
    These are the categories that I could make sense of and thought that they could be used to derive some metrics.
    Both are API calls.
"""

categories = {
    'nova.osapi_compute.wsgi.server',
    'nova.metadata.wsgi.server',
}


def parse(line: str) -> str:
    line = line.strip("\n").split(' ')

    if len(line) <= 2:
        return ""

    if line[5] not in categories:
        return ""

    """
        For every log line I am keeping :
            1 : Date
            2 : Time
            5 : Type
            12: IP
            13: Protocol
            19: Status Code
            21: Duration
    """

    if len(line) == 22:
        line = ",".join([line[1] + " " + line[2], ("compute" if line[5] == "nova.osapi_compute.wsgi.server" else "metadata"),
                        line[12], line[13].strip("\""), line[17], line[19], line[21]])

    else:
        line = ",".join([line[1] + " " + line[2], ("compute" if line[5] == "nova.osapi_compute.wsgi.server" else "metadata"),
                        line[7], line[8].strip("\""), line[12], line[14], line[16]])

    line = line.split(",")

    if len(line) == 8:
        return [line[:2] + line[3:], line[:3] + line[4:]]
    else:
        return [line]


def run(HOME):

    os.chdir(os.path.join(HOME, "data"))
    files = os.listdir()

    with open(os.path.join(os.getcwd(), "logs.csv"), 'w') as file_out:

        for log in files:
            with open(os.path.join(os.getcwd(), log)) as file_in:

                for line in file_in:

                    for log in parse(line):
                        file_out.write((','.join(log)) + "\n")

    os.system("rm *.log")


if __name__ == "__main__":
    run(os.environ.get("HOME"))
