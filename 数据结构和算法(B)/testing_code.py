import os
import subprocess

def run_and_check(input_file, expected_output_file):
    try:
        # 读取输入数据（自动检测编码）
        with open(input_file, "r", encoding="utf-8") as f:
            input_data = f.read()

        # 调用 Python 程序（使用原始字符串避免路径转义问题）
        result = subprocess.run(
            ["python", r"C:\Users\chris\Desktop\Peking University\code\python\py\数算\2.py"],
            input=input_data,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8"
        )
        actual_output = result.stdout.rstrip('\n')  # 忽略末尾换行符

        # 读取预期输出（自动检测编码）
        with open(expected_output_file, "r", encoding="utf-8") as f:
            expected_output = f.read().rstrip('\n')

        # 比较输出
        if actual_output == expected_output:
            print(f"[✓] {input_file} 测试通过")
        else:
            print(f"[✗] {input_file} 测试失败")
            print(f"  实际输出: {actual_output}")
            print(f"  预期输出: {expected_output}")

    except subprocess.CalledProcessError as e:
        print(f"[✗] {input_file} 运行失败: {e}")
    except FileNotFoundError:
        print(f"[✗] 文件不存在: {input_file} 或 {expected_output_file}")
    except Exception as e:
        print(f"[✗] {input_file} 出现错误: {e}")

def batch_test(test_dir):
    for filename in os.listdir(test_dir):
        if filename.endswith(".in"):
            input_file = os.path.join(test_dir, filename)
            expected_output_file = os.path.join(test_dir, filename.replace(".in", ".out"))
            if os.path.exists(expected_output_file):
                run_and_check(input_file, expected_output_file)
            else:
                print(f"[✗] 缺少对应的 .out 文件: {expected_output_file}")

if __name__ == "__main__":
    # 使用原始字符串避免路径转义问题
    test_directory = r"C:\Users\chris\Documents\WeChat Files\wxid_rxf3dbimeokt12\FileStorage\File\2025-06\29740(1)\cases"
    batch_test(test_directory)