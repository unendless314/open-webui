# Gemini 网络搜索功能使用指南

## 🌐 新功能概述

现在你的 Gemini Pipe 集成了 Google Search 功能，可以让 AI 实时搜索最新信息并提供带引文的答案！

## ✨ 主要特性

### 1. 自动网络搜索
- AI 会自动判断是否需要搜索最新信息
- 支持多语言搜索查询
- 实时获取最新数据

### 2. 智能引文系统
- 自动为回答添加来源链接
- 显示搜索使用的关键词
- 引文格式：[[来源标题]](链接)

### 3. 状态显示
- 实时显示搜索进度
- 区分思考和搜索状态
- 显示完成时间

## 🎛️ 配置选项

在 OpenWebUI 模型设置中，你可以控制以下参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `ENABLE_WEB_SEARCH` | True | 启用/禁用网络搜索功能 |
| `AUTO_CITE_SOURCES` | True | 自动添加引文和来源链接 |
| `SEARCH_LANGUAGE` | zh-CN | 搜索语言设置 |
| `REQUEST_TIMEOUT` | 120 | 搜索请求超时时间（秒） |
| `EMIT_STATUS_UPDATES` | True | 显示搜索进度状态 |

## 🚀 使用方法

### 基本使用
1. 确保使用支持网络搜索的模型（如 Gemini 2.5）
2. 在 OpenWebUI 中启用 `ENABLE_WEB_SEARCH` 选项
3. 直接提问，AI 会自动判断是否需要搜索

### 示例对话

**用户**: 谁赢了2024年欧洲杯？

**AI**: 🔍 搜索相关信息...

西班牙赢得了2024年欧洲杯，在决赛中以2-1击败英格兰[[UEFA官网]](https://uefa.com/euro2024/final)。这是西班牙队历史上第四次获得欧洲杯冠军[[阿尔及利亚电视台]](https://aljazeera.com/sports/euro2024)。

🔍 **搜索查询**: UEFA Euro 2024 winner, who won euro 2024

## 🎯 最佳实践

### 适合使用网络搜索的问题
- ✅ 最新新闻和事件
- ✅ 实时数据和统计
- ✅ 最新产品信息
- ✅ 当前股价、汇率等
- ✅ 体育比赛结果

### 不需要搜索的问题
- ❌ 历史事实
- ❌ 基础科学知识
- ❌ 编程语法
- ❌ 数学计算
- ❌ 创意写作

## 🔧 高级配置

### 1. 针对不同模型的配置

```python
# 自动检测支持搜索的模型
def _should_use_new_api(self, model_id: str) -> bool:
    # Gemini 2.5 及以上版本支持 grounding
    if 'gemini-2.5' in model_id.lower():
        return True
    return self.valves.ENABLE_WEB_SEARCH
```

### 2. 引文格式自定义

当前引文格式：`[[来源标题]](链接)`

你可以在设置中调整 `AUTO_CITE_SOURCES` 来控制是否显示引文。

### 3. 搜索语言设置

- `zh-CN`: 中文搜索
- `en-US`: 英文搜索
- `ja-JP`: 日文搜索
- `ko-KR`: 韩文搜索

## 📊 功能对比

| 功能 | 旧版本 | 新版本（带搜索） |
|------|--------|------------------|
| 基础对话 | ✅ | ✅ |
| 思考模式 | ✅ | ✅ |
| 实时信息 | ❌ | ✅ |
| 来源引用 | ❌ | ✅ |
| 搜索状态 | ❌ | ✅ |
| 多模态支持 | ✅ | ✅ |

## 🐛 常见问题

### Q1: 为什么有些问题不显示搜索状态？
**A**: AI 会智能判断是否需要搜索。对于基础知识问题，会直接使用训练数据回答。

### Q2: 搜索功能不工作怎么办？
**解决步骤**:
1. 检查是否使用 Gemini 2.5 或更高版本
2. 确认 `ENABLE_WEB_SEARCH` 已启用
3. 检查 API Key 权限是否包含搜索功能
4. 开启 `DEBUG_MODE` 查看详细日志

### Q3: 引文链接无法访问
**A**: 某些链接可能是内部链接或需要特殊权限，这是正常现象。

### Q4: 搜索结果不够准确
**尝试**:
- 使用更具体的问题描述
- 调整 `SEARCH_LANGUAGE` 设置
- 在问题中明确指定时间范围

## 🔒 隐私和安全

### 数据处理
- 搜索查询会发送到 Google 服务器
- 不会存储搜索历史
- 遵循 Google 的隐私政策

### 安全建议
- 避免搜索敏感个人信息
- 不要依赖搜索结果进行重要决策
- 定期检查 API 使用量

## 🚀 部署示例

### Docker Compose 配置

```yaml
version: '3.8'
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    environment:
      - GOOGLE_API_KEY=你的API密钥
      # 可选的搜索相关配置
      - ENABLE_WEB_SEARCH=true
      - AUTO_CITE_SOURCES=true
      - SEARCH_LANGUAGE=zh-CN
    volumes:
      - open-webui:/app/backend/data
    restart: unless-stopped
```

### 环境变量设置

```bash
# 基本设置
export GOOGLE_API_KEY="你的API密钥"

# 搜索功能设置
export ENABLE_WEB_SEARCH="true"
export AUTO_CITE_SOURCES="true"
export SEARCH_LANGUAGE="zh-CN"

# 启动容器
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e GOOGLE_API_KEY="$GOOGLE_API_KEY" \
  -e ENABLE_WEB_SEARCH="$ENABLE_WEB_SEARCH" \
  -e AUTO_CITE_SOURCES="$AUTO_CITE_SOURCES" \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

## 📈 性能优化

### 1. 搜索缓存
- 系统会自动缓存搜索结果
- 相同问题短时间内不会重复搜索

### 2. 超时设置
- 默认超时 120 秒
- 可根据网络情况调整 `REQUEST_TIMEOUT`

### 3. 并发处理
- 支持多用户同时使用搜索功能
- 自动负载均衡

## 🔮 未来功能

计划中的功能增强：
- [ ] 搜索结果缓存优化
- [ ] 更多搜索引擎支持
- [ ] 自定义搜索范围
- [ ] 搜索结果过滤
- [ ] 图片搜索支持

## 📞 支持

如果遇到问题，请：
1. 检查配置是否正确
2. 查看 DEBUG 日志
3. 确认 API 配额是否充足
4. 参考 [Google AI Studio 文档](https://aistudio.google.com/app/apikey)

现在你的 Gemini AI 已经拥有了强大的实时搜索能力！🎉