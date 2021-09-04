#!/usr/bin/python
import util
import templates

def run():
    print("Creating privacy policy")
    html = templates.get("privacy_policy")
    html = templates.initial_replace(html, 0)
    html = templates.final_replace(html, ".")
    util.writefile("../dest/privacy_policy.html", html)

if __name__ == "__main__":
    run()
