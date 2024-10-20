import argparse
import random
import time
from datetime import datetime

# 日志级别
log_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]


# 日志生成函数
def generate_log_entry():
    level = random.choice(log_levels)
    message = f"{level}: This is a sample log message."
    return message


# 主函数
def generate_logs(file_name):
    with open(file_name, "a") as log_file:  # 使用 'a' 模式以追加日志
        try:
            count = 0
            while True:
                if count % 5 == 0:  # 每5行的第一行以时间开头
                    timestamp = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )  # \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
                    log_file.write(f"{timestamp} - Log Start:\n")
                log_entry = generate_log_entry()
                log_file.write(f"{log_entry}\n")
                log_file.flush()  # 立即写入文件
                count += 1
                time.sleep(1)  # 每秒生成一条日志
        except KeyboardInterrupt:
            print("\n日志生成已停止。")


# 解析命令行参数
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成随机日志并写入文件")
    parser.add_argument("file_path", type=str, help="日志文件的路径")
    args = parser.parse_args()

    # 开始生成日志
    generate_logs(args.file_path)
