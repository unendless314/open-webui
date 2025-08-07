# Docker 环境 Google Gemini Pipe 部署指南

## 🚀 快速开始

### 方法一：在 OpenWebUI 界面设置（最简单）

1. 保存改进后的代码为 `google_gemini_pipe.py`
2. 在 OpenWebUI 中导入这个 pipe
3. 在模型选择界面点击设置图标
4. 在 `GOOGLE_API_KEY` 字段输入你的 API Key
5. 点击保存，即可使用

### 方法二：使用环境变量（推荐）

如果你使用 docker-compose，编辑你的 `docker-compose.yml`：

```yaml
version: '3.8'
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    environment:
      - GOOGLE_API_KEY=你的Google_API_Key  # 替换为你的实际 API Key
    volumes:
      - open-webui:/app/backend/data
    restart: unless-stopped

volumes:
  open-webui:
```

或者用 docker run：

```bash
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e GOOGLE_API_KEY="你的Google_API_Key" \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### 方法三：使用配置文件

1. 在宿主机创建配置目录：
```bash
mkdir -p ./config
echo "你的Google_API_Key" > ./config/google_api_key.txt
```

2. 修改 docker-compose.yml 添加卷映射：
```yaml
version: '3.8'
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
      - ./config:/app/config  # 映射配置目录
    restart: unless-stopped

volumes:
  open-webui:
```

## 🔑 获取 Google API Key

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. 登录你的 Google 账户
3. 点击 "Create API Key"
4. 选择一个项目或创建新项目
5. 复制生成的 API Key（格式类似：`AIzaSyABC123...`）

## ⚙️ 主要改进特性

### 1. 多种密钥配置方式
- **OpenWebUI 界面设置**：最用户友好
- **环境变量**：适合容器部署
- **配置文件**：适合开发测试

### 2. 智能错误提示
- API Key 未设置时显示设置说明
- 无效 API Key 时给出友好提示
- 网络错误时提供排查建议

### 3. 增强的思考模型支持
- 实时显示思考时间
- 可折叠的思考过程显示
- 可配置的更新间隔

### 4. 安全和性能优化
- API Key 格式验证
- 请求超时保护（默认 120 秒）
- 更好的资源清理机制

## 🎛️ 配置选项说明

在 OpenWebUI 的模型设置中，你可以调整以下参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `GOOGLE_API_KEY` | 空 | Google API 密钥 |
| `USE_PERMISSIVE_SAFETY` | False | 是否使用宽松安全设置 |
| `THINKING_MODEL_PATTERN` | "thinking" | 思考模型匹配模式 |
| `EMIT_STATUS_UPDATES` | True | 是否显示思考状态 |
| `DEBUG_MODE` | False | 调试模式 |
| `REQUEST_TIMEOUT` | 120 | 请求超时时间（秒） |

## 🐛 常见问题排查

### 问题1：显示"需要设置 Google API Key"
**解决方案**：
- 检查 API Key 是否正确设置
- 确认 API Key 格式正确（以 AIza 开头）

### 问题2：显示"API Key 无效或已过期"
**解决方案**：
- 重新生成 API Key
- 检查 Google Cloud 项目配置
- 确认 Gemini API 已启用

### 问题3：思考模型没有显示思考过程
**解决方案**：
- 确认使用的是思考模型（模型名包含 "thinking"）
- 检查 `EMIT_STATUS_UPDATES` 设置为 True

### 问题4：请求超时
**解决方案**：
- 增加 `REQUEST_TIMEOUT` 值
- 检查网络连接
- 尝试重新发送请求

## 📝 使用示例

### Docker Compose 完整示例

```yaml
version: '3.8'

services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    restart: unless-stopped
    ports:
      - "3000:8080"
    environment:
      # 基本配置
      - WEBUI_NAME=My AI Chat
      
      # Google API 配置
      - GOOGLE_API_KEY=AIzaSyABC123DEF456GHI789JKL012MNO345PQR  # 替换为你的
      - USE_PERMISSIVE_SAFETY=false
      - EMIT_STATUS_UPDATES=true
      - DEBUG_MODE=false
      
    volumes:
      # 数据持久化
      - open-webui:/app/backend/data
      
      # 可选：配置文件方式
      # - ./config:/app/config
      
    # 可选：资源限制
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G

volumes:
  open-webui:
```

启动命令：
```bash
# 保存上面的内容为 docker-compose.yml，然后运行：
docker-compose up -d

# 查看日志
docker-compose logs -f open-webui

# 停止服务
docker-compose down
```

## 🔄 更新和维护

### 更新容器
```bash
docker-compose pull
docker-compose up -d
```

### 查看日志
```bash
docker-compose logs -f open-webui
```

### 备份数据
```bash
docker run --rm -v open-webui_open-webui:/data -v $(pwd):/backup alpine tar czf /backup/openwebui-backup.tar.gz -C /data .
```

现在你就可以轻松地在 Docker 环境中使用 Google Gemini API 了！推荐使用方法一（界面设置）或方法二（环境变量），这样最简单方便。