#!/usr/bin/env python3

"""Print list of all repositories that contain a carpentry-style Jekyll
lesson.
"""

import pandas as pd


def get_lesson_repository_list() -> list[str]:
    df = pd.read_csv("repositories.csv")
    return df[df.is_carpentry_lesson].copy()["repository"].to_list()


if __name__ == "__main__":
    lst = get_lesson_repository_list()
    print(" ".join(lst))
