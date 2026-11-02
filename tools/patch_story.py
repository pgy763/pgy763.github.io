import io

p = r"D:\Github-code\_hub\story.html"
s = io.open(p, encoding="utf-8").read()

# 1. 新增一节，插在「验证到什么程度」之前
anchor = "  <h2>验证到什么程度</h2>"
section = """  <h2>第四件：从「读」到「拦住」</h2>
  <p>
    手册解决的是「已经报错了怎么办」。但更省事的是别踩进去。所以挑出最贵的十条
    （事务里调模型、单例 ChatMemory、直接注入 ChatClient、SSE 没设超时、流式里 block、
    <code>text/event-stream</code> 缺 charset、maxTokens 太小、空 catch 吞 IO、
    HTTP 客户端没配超时、硬编码密钥），做成了一个独立工具：
    <a href="https://github.com/pgy763/llm-lint">llm-lint</a>。
  </p>
  <p>
    它是纯静态扫描，不需要 classpath、不联网、不要 API key。这三点是有意的 ——
    要能塞进 pre-commit 和 CI，就不能依赖「先把环境跑起来」这个前提。
  </p>
  <p>
    写的底线是宁可漏报、不可乱报：没有符号解析，类型只按声明的文本判断，链式调用一律不追。
    判断不了就沉默，不猜。
  </p>
  <p>
    验收方式是 20 个样本文件：<code>samples/bad</code> 里每个文件必须<strong>只</strong>触发它自己那条规则，
    <code>samples/good</code> 里的修复版必须一条都不报。CI 两个方向都跑 —— 少报会红，乱报也会红。
  </p>

  <h2>验证到什么程度</h2>"""
assert s.count(anchor) == 1
s = s.replace(anchor, section)

# 2. 表格加一行
row_anchor = """      <tr>
        <td>shopkeeper</td>"""
row = """      <tr>
        <td>llm-lint</td>
        <td>CI：10 个反例各报一条、10 个正例零报告、两方向都卡</td>
        <td>在 llm-gateway、prompt-ops 两个真实项目上跑过，0 误报</td>
        <td>样本之外的写法、跨文件类型推断</td>
      </tr>
      <tr>
        <td>shopkeeper</td>"""
assert s.count(row_anchor) == 1
s = s.replace(row_anchor, row)

# 3. 加一条「被代码纠正过」的
find_anchor = """  <div class="finding">
    <div class="t">站点仓库名少了一个前缀，根路径一直是 404</div>"""
finding = """  <div class="finding">
    <div class="t">第一条规则写完，先被自己的正例打回来了</div>
    <p>
      LLM003 最初只要字段类型是 <code>ChatClient</code> 就报。可正例里那些用
      <code>ChatClient.builder()</code> 自己造出来的字段也被报了 —— 那恰恰是最推荐的写法。
      口径后来收紧成「带注入注解的才报」。<strong>没有正例的规则，只算写了一半。</strong>
    </p>
  </div>

  <div class="finding">
    <div class="t">站点仓库名少了一个前缀，根路径一直是 404</div>"""
assert s.count(find_anchor) == 1
s = s.replace(find_anchor, finding)

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok", len(s))