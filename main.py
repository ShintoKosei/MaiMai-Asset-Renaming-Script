import os
import shutil

# 定义文件夹路径
wait_assets_folder = 'wait_assets'
original_assets_folder = 'Original_assets'
output_folder = 'output'

# 检查输出文件夹是否有内容
if os.path.exists(output_folder) and os.listdir(output_folder):
    delete_confirm = input(f"输出文件夹 '{output_folder}' 中已有内容，是否删除？(y/n): ")
    if delete_confirm.lower() == 'y':
        shutil.rmtree(output_folder)
        os.makedirs(output_folder)
        print("输出文件夹已清空。")
    else:
        print("请手动清空输出文件夹后重新运行脚本。")
        exit()
else:
    # 创建输出文件夹，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# 获取文件列表，并按文件名排序
wait_assets_files = sorted(os.listdir(wait_assets_folder))
original_assets_files = sorted(os.listdir(original_assets_folder))

# 过滤非png文件
non_png_wait_assets_files = [file for file in wait_assets_files if not file.endswith('.png')]
non_png_original_assets_files = [file for file in original_assets_files if not file.endswith('.png')]

# 提示删除非png文件
if non_png_wait_assets_files or non_png_original_assets_files:
    print("以下文件不是PNG格式:")
    for file in non_png_wait_assets_files:
        print(f"wait_assets 文件夹: {file}")
    for file in non_png_original_assets_files:
        print(f"Original_assets 文件夹: {file}")

    delete_confirm = input("是否删除这些非PNG文件？(y/n): ")
    if delete_confirm.lower() == 'y':
        for file in non_png_wait_assets_files:
            os.remove(os.path.join(wait_assets_folder, file))
        for file in non_png_original_assets_files:
            os.remove(os.path.join(original_assets_folder, file))
        print("非PNG文件已删除。请重新运行脚本。")
        exit()
    else:
        print("未删除任何文件。请手动删除非PNG文件，然后重新运行脚本。")
        exit()

# 提取不包含ID的文件名部分
wait_assets_base_names = [file.rsplit('-', 1)[0] for file in wait_assets_files if file.endswith('.png')]
original_assets_base_names = [file.rsplit('-', 1)[0] for file in original_assets_files if file.endswith('.png')]

# 找出不匹配的文件名
extra_in_wait_assets = set(wait_assets_base_names) - set(original_assets_base_names)
extra_in_original_assets = set(original_assets_base_names) - set(wait_assets_base_names)

# 输出不匹配的文件名
if extra_in_wait_assets:
    print("wait_assets 文件夹中不匹配的文件名（不包含ID部分）:")
    for base_name in extra_in_wait_assets:
        print(base_name)
else:
    print("wait_assets 文件夹中没有不匹配的文件名（不包含ID部分）。")

if extra_in_original_assets:
    print("Original_assets 文件夹中不匹配的文件名（不包含ID部分）:")
    for base_name in extra_in_original_assets:
        print(base_name)
    delete_confirm = input("是否删除 Original_assets 文件夹中的多余文件？(y/n): ")
    if delete_confirm.lower() == 'y':
        for file in original_assets_files:
            original_base = file.rsplit('-', 1)[0]
            if original_base in extra_in_original_assets:
                os.remove(os.path.join(original_assets_folder, file))
        print("多余的文件已删除。请重新运行脚本以完成重命名。")
        exit()
    else:
        print("未删除任何文件。请手动处理多余的文件，然后重新运行脚本。")
        exit()
else:
    print("Original_assets 文件夹中没有不匹配的文件名（不包含ID部分）。")

# 建立 wait_assets 文件和 Original_assets 文件的对应关系
wait_assets_files_dict = {}
for wait_assets_file in wait_assets_files:
    if wait_assets_file.endswith('.png'):
        wait_assets_base, wait_assets_id = wait_assets_file.rsplit('-', 1)
        if wait_assets_base not in wait_assets_files_dict:
            wait_assets_files_dict[wait_assets_base] = []
        wait_assets_files_dict[wait_assets_base].append(wait_assets_file)

original_assets_files_dict = {}
for original_assets_file in original_assets_files:
    if original_assets_file.endswith('.png'):
        original_base, original_id = original_assets_file.rsplit('-', 1)
        if original_base not in original_assets_files_dict:
            original_assets_files_dict[original_base] = []
        original_assets_files_dict[original_base].append(original_assets_file)

# 遍历并重命名文件
for wait_assets_base in wait_assets_files_dict:
    if wait_assets_base in original_assets_files_dict:
        wait_assets_file_list = wait_assets_files_dict[wait_assets_base]
        original_assets_file_list = original_assets_files_dict[wait_assets_base]
        min_length = min(len(wait_assets_file_list), len(original_assets_file_list))
        for i in range(min_length):
            wait_assets_file = wait_assets_file_list[i]
            original_assets_file = original_assets_file_list[i]
            original_base, original_id = original_assets_file.rsplit('-', 1)
            new_file_name = f"{wait_assets_base}-{original_id}"
            shutil.copyfile(os.path.join(wait_assets_folder, wait_assets_file), os.path.join(output_folder, new_file_name))
    
    # 处理可能多出的文件
    if len(wait_assets_files_dict[wait_assets_base]) != len(original_assets_files_dict.get(wait_assets_base, [])):
        print(f"注意: 在文件基名 '{wait_assets_base}' 下，中方和国际文件数目不一致。")

print("文件处理完成。")