class RefactorAgent:

    def refactor(self, issues):
        print("🛠 Refactor: 生成重构建议...")

        suggestions = []

        for issue in issues:
            t = issue["type"]

            if t == "debug":
                suggestions.append({
                    "action": "replace",
                    "detail": "使用 logging 替代 print"
                })

            elif t == "unused_var":
                suggestions.append({
                    "action": "remove",
                    "detail": "删除未使用变量"
                })

            elif t == "long_function":
                suggestions.append({
                    "action": "refactor",
                    "detail": "拆分函数为多个小函数"
                })

            elif t == "duplicate_logic":
                suggestions.append({
                    "action": "optimize",
                    "detail": "合并重复循环逻辑"
                })

        return suggestions