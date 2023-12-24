import re
import numpy as np
from helper import parseFile


FILENAME = "input.txt"


def is_in_future_path(solution, line_info):
    py_final = solution[0]
    px_final = solution[1]

    px_initial = line_info["px"]
    py_initial = line_info["py"]

    vx = line_info["vx"]
    vy = line_info["vy"]

    tx = (px_final - px_initial) / vx
    ty = (py_final - py_initial) / vy

    return ty > 0 and tx > 0


if __name__ == "__main__":
    lines = parseFile(FILENAME)

    test_area_bounds = {"min": 200000000000000, "max": 400000000000000}

    line_details = []

    intersections = {}

    for line in lines:
        numbers = re.findall(r"-?\d+", line)
        positions = numbers[:3]
        velocities = numbers[3:]

        px, py = positions[:2]
        vx, vy = velocities[:2]

        gradient = int(vy) / int(vx)
        intercept = int(py) - (gradient * int(px))

        # x0 + (m * x1) = b
        line_details.append(
            {
                "x1": -1 * gradient,
                "b": intercept,
                "px": int(px),
                "py": int(py),
                "vx": int(vx),
                "vy": int(vy),
            }
        )

    i = 0

    while i < len(line_details):
        line_a = line_details[i]

        j = 0

        while j < len(line_details):
            item = (max(i, j), min(i, j))

            if i != j and item not in intersections.keys():
                line_b = line_details[j]
                X = np.array([[1, line_b["x1"]], [1, line_a["x1"]]])
                B = np.array([line_b["b"], line_a["b"]])

                try:
                    solution = np.linalg.solve(X, B)

                    is_in_line_a_future_path = is_in_future_path(
                        solution=solution, line_info=line_a
                    )
                    is_in_line_b_future_path = is_in_future_path(
                        solution=solution, line_info=line_b
                    )

                    if is_in_line_a_future_path and is_in_line_b_future_path:
                        min_x, max_x = test_area_bounds["min"], test_area_bounds["max"]
                        min_y = min_x
                        max_y = max_x

                        x0, x1 = solution

                        # test area bound checking
                        if (x0 >= min_y and x0 <= max_y) and (
                            x1 >= min_x and x1 <= max_x
                        ):
                            intersections[item] = True

                except:
                    pass

            j += 1

        i += 1

    print(
        "The number of intersections occurring within the test area are:",
        len(intersections),
    )
