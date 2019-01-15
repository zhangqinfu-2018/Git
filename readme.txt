安装之后打开Git Bash.
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git init 把这个目录变成Git可以管理的仓库
git add readme.txt 添加文件或修改文件到暂缓区
git commit -m "wrote a readme file" 暂缓区提交到仓库
git status 查看状态
git diff readme.txt  查看修改的内容
git lot 查看提交历史
git reset --hard commit_id 回到对应的版本
git reset HEAD readme.txt 撤销暂存区的修改
git checkout -- readme.txt 撤销工作区的修改
git rm readme.txt 删除仓库里的文件
git reflog 查看所有历史命令
git diff HEAD -- readme.txt 查看工作区和版本库里面最新版本的区别
ssh-keygen -t rsa -C "1096388722@qq.com" 创建SSH Key
登陆GitHub-settings-Add SSH Key-填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容
Create a new repo
Repository name填入Git
Create repository
git remote add origin git@github.com:zhangqinfu-2018/Git.git 本地仓库与远程库的关联
git push -u origin master 第一次推送本地仓库到远程仓库
git push origin master 非第一次推送
git clone git@github.com:zhangqinfu-2018/gitskills.git 远程仓库克隆到本地
