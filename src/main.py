#!/usr/bin/python
import index
import privacy_policy
import e404
import timeline
import contestants
import search
import static_files

def run():
    print("Creating whole project")
    index.run()
    privacy_policy.run()
    e404.run()
    timeline.run()
    contestants.run()
    search.run()
    static_files.run()

if __name__ == "__main__":
    run()
