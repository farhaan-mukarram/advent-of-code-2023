import re
from helper import parseFile


FILENAME = "input.txt"

PATTERN = r"(^.+)({.+})"

workflow_info = {}
parts_info = {}


def determine_part_status(part_idx: int):
    part_ratings = parts_info[part_idx]

    destinations = ["in"]

    current_rules = workflow_info["in"]
    flag = False

    while not flag:
        for rule in current_rules:
            if ":" in rule:
                condition, destination = rule.split(":")
                rating, value = re.split(r">|<", condition)

                operator_search_res = re.search(r">|<", condition)
                if operator_search_res is not None:
                    operator = operator_search_res.group()

                    if operator == "<":
                        if part_ratings[rating] < int(value):
                            if destination == "A" or destination == "R":
                                flag = True
                                destinations.append(destination)

                                return destination

                            else:
                                current_rules = workflow_info[destination]
                                destinations.append(destination)
                                break

                    elif operator == ">":
                        if part_ratings[rating] > int(value):
                            if destination == "A" or destination == "R":
                                flag = True
                                destinations.append(destination)

                                return destination

                            else:
                                current_rules = workflow_info[destination]
                                destinations.append(destination)

                                break

            else:
                if rule == "A" or rule == "R":
                    destinations.append(rule)
                    return rule

                else:
                    current_rules = workflow_info[rule]
                    destinations.append(rule)

                    break


if __name__ == "__main__":
    lines = parseFile(FILENAME)

    idx = lines.index("")

    workflows = lines[:idx]
    part_ratings = lines[idx + 1 :]

    # populate the workflow_info map
    for workflow in workflows:
        search_result = re.search(PATTERN, workflow)

        if search_result is not None:
            workflow_name, workflow_rules = search_result.group(1), search_result.group(
                2
            )

            workflow_info[workflow_name] = (
                workflow_rules.replace("{", "").replace("}", "").split(",")
            )

    # populate the parts_info map
    for part_idx, part in enumerate(part_ratings):
        x_rating_result = re.search(r"x=(\d+)", part)
        m_rating_result = re.search(r"m=(\d+)", part)
        a_rating_result = re.search(r"a=(\d+)", part)
        s_rating_result = re.search(r"s=(\d+)", part)

        if (
            x_rating_result is not None
            and m_rating_result is not None
            and a_rating_result is not None
            and s_rating_result is not None
        ):
            x_rating = x_rating_result.group(1)
            m_rating = m_rating_result.group(1)
            a_rating = a_rating_result.group(1)
            s_rating = s_rating_result.group(1)

            parts_info[part_idx] = {
                "x": int(x_rating),
                "m": int(m_rating),
                "a": int(a_rating),
                "s": int(s_rating),
            }

    accepted_parts = []
    for part_idx in parts_info.keys():
        part_status = determine_part_status(part_idx)

        if part_status == "A":
            accepted_parts.append(parts_info[part_idx])

    sum_of_part_ratings = 0
    for part in accepted_parts:
        for value in part.values():
            sum_of_part_ratings += value

    print(
        "The sum of ratings numbers for parts that got accepted is:",
        sum_of_part_ratings,
    )
