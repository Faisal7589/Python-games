import cx_Freeze

executables = [cx_Freeze.Executable("client.py")]
cx_Freeze.setup(
     name = "RPC", options={"build_exe":{"packages":["pygame"]}},
     executables = executables
)