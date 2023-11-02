#!/usr/bin/python3
import py_compile

if __name__ == "__main__":
    m_code = py_compile.compile("hidden_4.py")

    names = [name for name in m_code.co_names if not name.startswith("__")]

    s_names = sorted(names)

    for name in s_names:
        print("{}".format(name))
