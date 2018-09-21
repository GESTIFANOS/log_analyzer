#!/usr/bin/env python
import os
import sys
from src import main


if __name__ == "__main__":
        # update to accept date format or delimiter ...
        main.LogAnalyzer.report(sys.argv[1])