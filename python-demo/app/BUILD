load("@py_deps//:requirements.bzl", "requirement")

py_binary(
    name = "hello",
    srcs = ["hello.py"],
    deps = [
        "//utils:math_utils",
        requirement("requests"),
        ],
)

py_test(
    name = "hello_test",
    srcs = ["hello_test.py"],
    deps = [
        "//utils:math_utils",
    ],
)
