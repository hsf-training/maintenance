#!/usr/bin/env python3

"""Get txt file of all repositories that contain a carpentry-style Jekyll
lesson
"""

import pandas as pd


df = pd.read_csv("repositories.csv")
df = df[df.is_carpentry_lesson].copy()["repository"]
df.to_csv("lesson_repositories.txt", header=False, index=False)
