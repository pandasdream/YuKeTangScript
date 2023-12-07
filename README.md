# YuKeTangAutoPlayerScriptForBUAA

###### Python写的一个雨课堂自动连播脚本，主要应对这学期的gcll课

##### 使用方法

- 安装库

  ```
  pip install -r ./requriements.txt
  ```

- 登录雨课堂，`F12`进入开发者工具，点击网络，选择`Fetch/XHR`，刷新页面，找到`get_video_watch_progress`这个请求，可以找到`cookie`和`user_id`字段，填入到`./conf.txt`中

- 确定要从哪个`video_id`开始播放，将`video_id`填入到`./conf.txt`中(视频播放页`url`的`video/xxxxxxxx`那里就是`video_id`)

- 运行`main.py`

##### 补充

- `./conf.txt`中的其他字段暂时没有发现变化的情况，不放心可以再检查一遍，在`get_video_watch_progress`中均有对应

- 配合`GlobalSpeed`浏览器插件设置全局2倍速效率更高，代码里默认是2倍速，如果懒得用插件需要改代码或者运行两轮脚本

- 本脚本仅供参考，请合理使用

  