import os
import pandas as pd

def check_files(root_dir, file_list):
    data = []
    folders_checked = set()
    for projects in sconstruct_paths:
        if projects not in folders_checked:
            file_dict = {file: '✔' if os.path.isfile(os.path.join(projects, file)) else '' for file in file_list}
            data.append({'Folder': projects, **file_dict})
            folders_checked.add(projects)
    df = pd.DataFrame(data)
    return df

def find_sconstruct_paths(project_dir, exclude_paths):
    sconstruct_paths = []
    for root, dirs, files in os.walk(project_dir):
        if all(exclude_path not in root for exclude_path in exclude_paths):
            if 'SConstruct' in files:
                sconstruct_paths.append(root)
    return sconstruct_paths

def output_to_markdown(df, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(df.to_markdown(index=False))

# 示例用法:
BSP_ROOT = '.'
exclude_paths = ['templates', 'doc']
files_to_check = ['rtconfig.h','rtconfig.py', '.config','Kconfig', 'template.uvprojx','template.ewp', 'README.md', 'README_ZH.md','SConscript', 'template.Uv2','template.uvproj']
sconstruct_paths = find_sconstruct_paths('.', exclude_paths)
result_table = check_files(sconstruct_paths, files_to_check)
print(result_table)
output_file = 'output.md'
output_to_markdown(result_table, output_file)
