# 开发工具集 (Development Tools)

本目录包含项目开发中使用的自动化工具脚本。

## 目录结构

```
tools/
├── README.md                  # 本文档
├── git-commit-to-blog.py      # Git commit 转博客文章工具
├── md-validator.py            # Markdown 文件校验工具
├── install-hooks.sh           # Git hooks 安装脚本
├── hooks/
│   └── post-commit            # Git post-commit hook
└── templates/
    └── commit-post.md         # 博客文章模板
```

---

## 1. Git Commit to Blog (git-commit-to-blog.py)

将 Git commit 信息自动转换为 Hexo 博客文章。

### 功能特点

- 读取 git commit 信息（标题、描述、作者、时间）
- 自动生成符合 Hexo 格式的 markdown 文件
- 支持自定义模板
- 可以处理单个 commit 或批量处理

### 使用方法

```bash
# 处理最新的 commit
python tools/git-commit-to-blog.py

# 处理指定的 commit
python tools/git-commit-to-blog.py --commit abc123

# 批量处理最近 10 个 commits
python tools/git-commit-to-blog.py --all --limit 10

# 指定输出目录
python tools/git-commit-to-blog.py --output-dir apps/blog-hexo/source/_posts/

# 使用自定义模板
python tools/git-commit-to-blog.py --template tools/templates/my-template.md
```

### 命令行参数

| 参数           | 说明                 | 默认值                           |
| -------------- | -------------------- | -------------------------------- |
| `--repo-path`  | Git 仓库路径         | 当前目录                         |
| `--output-dir` | 输出目录             | `apps/blog-hexo/source/_posts/`  |
| `--template`   | 模板文件路径         | `tools/templates/commit-post.md` |
| `--commit`     | 指定 commit hash     | 最新 commit                      |
| `--all`        | 处理多个 commits     | false                            |
| `--limit`      | 批量处理时的数量限制 | 10                               |

### 模板变量

模板使用 `{{ variable }}` 语法，支持以下变量：

- `{{ title }}` - commit 标题（第一行）
- `{{ date }}` - commit 日期
- `{{ author }}` - 作者名称
- `{{ email }}` - 作者邮箱
- `{{ hash }}` - commit 短 hash
- `{{ full_hash }}` - commit 完整 hash
- `{{ branch }}` - 当前分支名
- `{{ body }}` - commit 详细描述
- `{{ changed_files }}` - 变更文件列表

---

## 2. Markdown Validator (md-validator.py)

校验 Markdown 文件格式，检查特殊字符和常见问题。

### 检查项目

#### 错误级别 (Error)

- `frontmatter-missing` - 缺少 YAML frontmatter
- `frontmatter-incomplete` - frontmatter 未正确关闭
- `frontmatter-title` - 缺少 title 字段
- `frontmatter-date` - 缺少 date 字段
- `link-empty-url` - 链接 URL 为空
- `link-space-url` - 链接 URL 包含空格
- `image-empty-src` - 图片源为空
- `code-block-unclosed` - 代码块未关闭
- `encoding` - 文件编码错误

#### 警告级别 (Warning)

- `special-char` - 包含特殊不可见字符
- `frontmatter-date-format` - 日期格式不规范
- `link-empty-text` - 链接文本为空
- `heading-empty` - 空标题
- `heading-level-jump` - 标题级别跳跃 (strict 模式)

#### 提示级别 (Info)

- `smart-quote` - 使用了智能引号
- `code-block-no-lang` - 代码块未指定语言 (strict 模式)
- `line-length` - 行过长 (strict 模式)
- `trailing-whitespace` - 行尾空格 (strict 模式)
- `consecutive-blank-lines` - 连续空行过多 (strict 模式)

### 使用方法

```bash
# 验证单个文件
python tools/md-validator.py path/to/file.md

# 验证整个目录
python tools/md-validator.py apps/blog-hexo/source/_posts/

# 启用严格模式
python tools/md-validator.py --strict .

# JSON 格式输出
python tools/md-validator.py --output json .

# Markdown 报告格式
python tools/md-validator.py --output markdown . > report.md

# 忽略特定规则
python tools/md-validator.py --ignore "smart-quote,trailing-whitespace" .
```

### 命令行参数

| 参数       | 说明                          | 默认值 |
| ---------- | ----------------------------- | ------ |
| `path`     | 文件或目录路径                | `.`    |
| `--strict` | 启用严格模式                  | false  |
| `--output` | 输出格式 (text/json/markdown) | `text` |
| `--ignore` | 忽略的规则（逗号分隔）        | 无     |
| `--fix`    | 自动修复问题（待实现）        | false  |

### 输出示例

```
❌ posts/hello.md:1:1 [frontmatter-missing] Missing YAML frontmatter
⚠️ posts/hello.md:15:8 [special-char] Found problematic character: Zero-width space
   💡 Remove or replace the Zero-width space
ℹ️ posts/hello.md:20:5 [smart-quote] Found smart quote: '"'
   💡 Replace with regular quote: '"'
```

---

## 3. Git Hooks

### 安装方法

```bash
# 运行安装脚本
chmod +x tools/install-hooks.sh
./tools/install-hooks.sh
```

### post-commit Hook

每次 commit 后自动运行，将 commit 信息转换为博客文章。

可以通过修改 `tools/hooks/post-commit` 来自定义行为。

---

## 配合使用示例

### 完整工作流

```bash
# 1. 安装 git hooks
./tools/install-hooks.sh

# 2. 正常开发和提交代码
git add .
git commit -m "feat: 添加新功能"
# post-commit hook 自动生成博客文章

# 3. 验证生成的文章
python tools/md-validator.py apps/blog-hexo/source/_posts/

# 4. 构建博客
cd apps/blog-hexo && hexo generate
```

### CI/CD 集成

```yaml
# GitHub Actions 示例
- name: Validate Markdown
  run: |
    python tools/md-validator.py --strict apps/blog-hexo/source/_posts/
```

---

## 依赖

这些工具只使用 Python 标准库，无需额外安装依赖：

- Python 3.7+
- Git (用于 git-commit-to-blog.py)

---

## 许可证

MIT License
