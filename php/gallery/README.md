效果演示：https://files.photo.gallery/demo

设置说明：https://forum.photo.gallery/viewtopic.php?f=66&t=9964

更多支持图片信息功能显示：https://files.photo.gallery/demo/?samples
例如图片使用的相机，GPS信息，等等。
支持在线播放 视频 音乐 和内置显示某些语言文件代码这些，等等。

php需要安装扩展：fileinfo exif imagemagick

配置:

```
// 根目录配置
'root' => '根目录路径', // root path relative to script.
'start_path' => false, // start path relative to script. If empty, root is start path

// 登录账号密码配置
'username' => 'zhujizixun',
'password' => '12345678', // Add password directly or use https://tinyfilemanager.github.io/docs/pwd.html to encrypt the password (encrypted password is more secure, as it prevents your password from being exposed directly in a file).
// 排除文件或者目录
'files_exclude' => '/.(html|xml)$/i', // '/.(pdf|jpe?g)$/i'
'dirs_exclude' => '//js|/_files(/|$)/i', //'//Convert|/football|/node_modules(/|$)/i',
'allow_symlinks' => true, // allow symlinks
```

