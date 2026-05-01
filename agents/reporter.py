class ReporterAgent:

    def generate(self, file_path, issues, suggestions, test_result):
        print("📄 Reporter: 生成报告...\n")

        report = f"""
================ PR REPORT ================

文件: {file_path}

🔍 检测问题:
"""
        for i in issues:
            report += f"- {i['message']}\n"

        report += "\n🛠 重构建议:\n"
        for s in suggestions:
            report += f"- [{s['action']}] {s['detail']}\n"

        report += "\n🧪 测试结果:\n"
        report += f"{test_result['status']} - {test_result['detail']}\n"

        report += "\n=========================================\n"

        return report