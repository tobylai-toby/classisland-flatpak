# classisland-flatpak

**WARNING** 非ClassIsland官方Flatpak构建

**WARNING** 实验性质的，很可能无法用

## 打包
1. 安装依赖
```bash
flatpak install org.freedesktop.Sdk/x86_64/24.08
```
2. 构建/测试运行
```bash
git clone https://github.com/tobylai-toby/classisland-flatpak.git
cd classisland-flatpak
flatpak-builder --force-clean build cn.classisland.app.yml --install --user --repo=repo
flatpak run cn.classisland.app
```

## FAQ
- Q: 经过测试了吗？
    - 还没有充分测试过
- Q: 支持什么架构？
    - 应该支持x64和aarch64
    - **alpine arm64没法运行，奇怪**
- Q: 上传flathub了吗
    - 没
- Q: extra-data怎么用的是镜像的Github
    - 直接用Github由于某些原因太慢了（）如果你不需要镜像源的话可以自行删掉镜像前缀