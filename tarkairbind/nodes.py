class IRInst:
    def GetCode(self, indent: int = 0) -> str:
        return ""

    def GetIndentedLine(self, line: str, space: int) -> str:
        return f"{'    ' * space}{line}\n"


class IRExitIntInst(IRInst):
    def __init__(self, val: int) -> None:
        self.val = val

    def GetCode(self, indent: int = 0) -> str:
        return self.GetIndentedLine(f"exit {self.val}", indent)


class IRFuncInst(IRInst):
    def __init__(self, name: str) -> None:
        self.name = name
        self.inst: list[IRInst] = []

    def GetCode(self, indent: int = 0) -> str:
        code = self.GetIndentedLine(f"func {self.name}", indent)
        for inst in self.inst:
            code += inst.GetCode(indent + 1)
        code += self.GetIndentedLine(f"endfunc", indent)
        return code


class IRModule(IRInst):
    def __init__(self) -> None:
        self.inst: list[IRInst] = []

    def GetCode(self, indent: int = 0) -> str:
        code = ""
        for inst in self.inst:
            code += inst.GetCode(indent)
        return code
