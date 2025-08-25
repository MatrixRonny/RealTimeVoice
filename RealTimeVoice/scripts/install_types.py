import os
import subprocess
import sys

is_windows = os.name == 'nt'

# # Prepare commands as a single script
# if is_windows:
#     activate_venv = "main-env\\Scripts\\activate.bat"
#     script = "\n".join([
#         activate_venv,
#         "pip install types-requests types-configobj"
#     ])
#     shell_exe = "cmd"
#     shell_args = ["/C", script]
# else:
#     activate_venv = "source main-env/Scripts/activate"
#     script = "\n".join([
#         activate_venv,
#         "pip install types-requests types-configobj"
#     ])
#     shell_exe = "bash"
#     shell_args = ["-c", script]

# # Run the script in a shell so environment changes persist
# result = subprocess.run(
#     [shell_exe] + shell_args,
#     capture_output=True,
#     text=True,
#     cwd=os.getcwd()
# )

# print(result.stdout)
# print(result.stderr, file=sys.stderr)

types_to_install: list[str] = ["types-requests"]
shell_exe: str
shell_args: list[str]
if is_windows:
    shell_exe = "cmd"
    shell_args = []
    script = "\n".join([
        "@echo off",
        "..\\main-env\\Scripts\\activate.bat",
        f"pip install {' '.join(types_to_install)}",
        "exit 0"
    ])
else:
    shell_exe = "bash"
    shell_args = []
    script = "\n".join([
        "source ../main-env/Scripts/activate",
        f"pip install {' '.join(types_to_install)}",
        "exit 0"
    ])

try:
    # Start an interactive shell process
    proc = subprocess.Popen(
        [shell_exe] + shell_args,
        stdin=subprocess.PIPE,
        stdout=sys.stdout,
        stderr=sys.stderr,
        cwd=os.getcwd()
    )

    # Cast stdin to ensure it is not None before writing
    if proc.stdin is None:
        raise RuntimeError("stdin of the process is None")

    proc.stdin.write((script + "\n").encode())
    proc.stdin.flush()
    proc.wait()
except KeyboardInterrupt:
    pass

if proc.returncode != 0:
    print(f"Error: Command failed with return code {proc.returncode}", file=sys.stderr)
    sys.exit(proc.returncode)
else:
    print("Type stubs installed successfully.")