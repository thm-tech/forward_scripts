## Scan

This project is a easy demo for learn how to use zc.buildout and setuptools to build a python project, just 50+ lines.

这个项目是一个简单的 demo, 来学习如何使用 zc.buildout 和 setuptools 来构建 python 项目, 仅有50+行代码.

## How Use
该项目正如所看到的那样, 只有赤裸着的 python 源代码(在 ./src 目录下). 
执行下面的步骤来完成源代码打包, 依赖安装和生成项目启动文件.
### In windows

1. cd pyseed
2. python bootstrap-buildout.py
3. ./bin/buildout.exe
4. ./start.exe

It will print 'Hello World!' in console.

### In linux

1. cd pyseed
2. python bootstrap-buildout.py
3. ./bin/buildout
4. ./start

It will print 'Hello World!' in shell

## More

1.
```
All codes in ./src will packaged into an egg packages which is named 'pyseed.egg'

所有源代码会被打包成一个名叫 'pyseed.egg' 的 egg 包.
```

2.
```
This project depends on ndict.py == 1.0.5, 
so buildout will automatically download the dependent in ./eggs folder, 
but will not change the system Python environment.Environmental isolation.

配置该项目依赖 ndict.py == 1.0.5, buildout 会自动下载该依赖于 ./eggs 文件夹下, 
而不会改动系统 python 环境.完成了环境隔离
```

3.
```
The project has a./bin/start (. exe) startup script.

该项目拥有一个 ./bin/start(.exe) 启动脚本
```

## End
zc.buildout 学习曲线陡峭.深知不要重复搬砖之道理, 特别制作该 python project seed, 以备不时之需.