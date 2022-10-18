gitlab http://172.16.11.4:9999/
账号wangshuo 
密码ws000120







git  status   					获取状态 
git add .  						添加到本地缓存 
git commit -m '提交消息内容'  	提交
git merge <分支名称>  			合并
git checkout    				分支/文件路径 切换分支/删除文件
git checkout -b                 			创建分支并切换到新的分支上面
git branch   				查看本地分支 
git branch -a                   			查看所有分支 
git branch -r 				查看远程分支
git branch -vv 				查看本地分支与远程分支关联关系
git branch -d A 				删除本地分支
git push origin -d <branch>			删除远程分支 （用本地分支名，前面不加origin）
git remote -v  				获取需要远程仓库 
git push <my_remote> <branch> 		推送至我的远程仓库
git pull <base_remote> <branch>  		拉取主远程仓库代码 
git config --global user.name "名称"     		重新配置名称
git config --global user.email "邮箱"    		重新配置邮箱   
git branch --set-upstream-to dev origin/mastrer       本地分支关联远程分支                                                                                                                                                                                                                                                                                                                                                    
git config --global credential.helper store  	 解决一直重新输入用户名密码的问题
git config --system --unset credential.helper  	 重新配置git用户名和密码
git reset --soft HEAD^ 			 撤回commit操作，写的代码仍然保留


 git update-index --assume-unchanged /path/file          git不再跟踪文件路径的更新了
 git update-index --no-assume-unchanged /path/file     解除不跟踪设置,即可使git再次跟踪 

