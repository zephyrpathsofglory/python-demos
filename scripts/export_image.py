import csv
import os
import subprocess

# 指定 docker-compose 文件路径
docker_compose_filepath = "G:\\projects\\nightingale\\docker\\compose-bridge\\docker-compose.yaml"

# 指定输出目录
output_dir = r"F:\\images\\nightingale"  # 镜像和 CSV 文件输出目录

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 执行 docker image ls 命令并过滤输出
result = subprocess.run(
    f"docker-compose -f {docker_compose_filepath} images",
    capture_output=True,
    text=True,
    shell=True,
)

# 解析输出
images = []
if result.returncode == 0:
    output = result.stdout.strip().split("\n")
    for line in output:  # 逐行处理输出
        parts = line.split()
        if len(parts) >= 5:
            container_name = parts[0]
            repo = parts[1]
            tag = parts[2]
            image_id = parts[3]
            size = parts[4]

            images.append((container_name, repo, tag, image_id, size))

            # 保存镜像到 .tar 文件
            tar_file_name = os.path.join(output_dir, f"{image_id}.txt")
            subprocess.run(["docker", "save", "-o", tar_file_name, image_id])
            print(f"镜像名 {repo}:{tag}({image_id}) 已保存到 {tar_file_name}")

# 输出到 CSV 文件
csv_file = os.path.join(output_dir, "images.csv")
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(images)

print(f"符合条件的镜像信息已保存到 {csv_file} 文件中。")
