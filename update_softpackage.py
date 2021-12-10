# -*- coding: utf-8 -*-
import os
import json

# 存放的数据列表
data_list = []
group_name = []
curren_name = []
package_name = []
github_link = []
package_description = []
package_json_name = []
package_license = []
package_cata = []
package_auth = []

package_list = ['iot', 'ai', 'language', 'misc', 'multimedia',
                'peripherals', 'security', 'system', 'tools']

filename = 'rtthread_softlist.md'
with open(filename, 'w', encoding='utf-8') as file_object:
    file_object.write("#RTTHREAD software package list\r\n")
    for root, dirs, files in os.walk("packages"):
        for f in files:
            curren_name = os.path.basename(
                os.path.abspath(os.path.join(root, "..")))
            if os.path.splitext(f)[1] == '.json':
                if group_name != curren_name:
                    if curren_name in package_list:
                        group_name = curren_name
                        file_object.write("\r\n")
                        file_object.write("## " + group_name + "\n")
                        file_object.write("\r\n |forks|stars| name|author  | license   |note|"+"\n" +
                                          "| ------------------------------------------------------------ | ------------------- | ------------------------------------------------------------ | ------------------- | -------------------- | ------------------------------------------------------------ |" + "\n")
                package_name = os.path.basename(os.path.join(root))
                # print(os.path.basename(os.path.join(root)))      ##package name
                json_path = os.path.join(root, f)
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    json_dict = json.load(json_file, encoding="utf-8")
                    for dict in json_dict.items():
                        if dict[0] == "description":
                            # json_list.append(dict[1])
                            # print(dict[1])
                            package_description = dict[1]
                        if dict[0] == "author":
                            for dict_sub in dict[1].items():
                                # json_list.append(dict[1])
                                if dict_sub[0] == "name":
                                    package_json_name = dict_sub[1]
                                    # print(dict_sub)

                        if dict[0] == "license":
                            # json_list.append(dict[1])
                            # print(dict[1])
                            package_license = dict[1]
                        if dict[0] == "repository":
                            # print(dict[1])
                            github_link = dict[1]
                            github_repo =  github_link[github_link.find('com')+4:]
                            github_name = eval(repr(github_repo).replace('.', '/'))
                            strlist =github_name.split('/')
                            
                            #print(' '+github_repo+'{'+strlist[0]+'},{'+strlist[1]+'}\r\n')
                            # json_list.append(dict[1])
                file_object.write("|![GitHub forks](https://img.shields.io/github/forks/"+strlist[0]+"/"+strlist[1]+"?style=plastic)|![GitHub Repo stars](https://img.shields.io/github/stars/"+strlist[0]+"/"+strlist[1]+"?style=social)| ["+package_name + "](" + github_link + ") |" +
                                  package_json_name+"|"+package_license+"|"+package_description + "|\n")
