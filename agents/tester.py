import subprocess

class TesterAgent:

    def test(self):
        print("🧪 Tester: 执行单元测试...")

        try:
            result = subprocess.run(
                ["python", "-m", "unittest", "test_sample.py"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return {"status": "pass", "detail": "测试通过"}
            else:
                return {"status": "fail", "detail": result.stdout}

        except Exception as e:
            return {"status": "error", "detail": str(e)}