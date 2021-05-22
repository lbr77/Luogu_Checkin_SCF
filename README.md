# Luogu_Checkin_SCF
使用scf云函数打卡洛谷

## Use 
在此https://console.cloud.tencent.com/scf新建一个函数，上传从release中下载的zip

然后修改index.py内容，
填入你的洛谷cookie，还有qq号，和从qmsg酱中获得的sendkey

然后配置触发器

定时触发

0 15 10 * * * *

![](https://cdn.jsdelivr.net/gh/lbr77/CDN@main/img/2021-05-22/19-46-57-e23d02.png)

然后每天早上10点15分就会收到qq消息 

![](https://cdn.jsdelivr.net/gh/lbr77/CDN@main/img/2021-05-22/19-49-11-d92836.png)
