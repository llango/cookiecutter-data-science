import sys

REQUIRED_PYTHON = "{{ cookiecutter.python_interpreter }}"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("无法识别的解释器: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "该项目需要Python {}。 发现: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> 开发环境通过所有测试!")


if __name__ == '__main__':
    main()
