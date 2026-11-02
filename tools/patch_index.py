import io

p = r"D:\Github-code\_hub\index.html"
s = io.open(p, encoding="utf-8").read()

anchor = """<a class="go" href="https://github.com/pgy763/shopkeeper-agent">看项目 <span class="arrow">→</span></a>
      </article>

    </div>
  </section>"""

add = """<a class="go" href="https://github.com/pgy763/shopkeeper-agent">看项目 <span class="arrow">→</span></a>
      </article>

    </div>
  </section>

  <section>
    <div class="cards">

      <article class="card">
        <div class="kicker">怎么防 · CLI</div>
        <h2><a href="https://github.com/pgy763/llm-lint">llm-lint</a></h2>
        <p>手册里最贵的十条，做成了一个能跑的命令。扫一遍源码，在 commit 之前把「事务里调模型」「单例 ChatMemory」「SSE 没设超时」这类问题标在 diff 上——不联网、不要 key、不需要 classpath。</p>
        <ul class="facts">
          <li>10 条规则</li>
          <li>JDK 17+</li>
          <li>一行 uses: 接进 CI</li>
          <li>MIT</li>
        </ul>
        <a class="go" href="https://github.com/pgy763/llm-lint">看工具 <span class="arrow">→</span></a>
      </article>

    </div>
  </section>"""

assert s.count(anchor) == 1, s.count(anchor)
s = s.replace(anchor, add)

path_anchor = """    <div class="path">
      <div class="q">我想看一个完整项目长什么样</div>"""
path_add = """    <div class="path">
      <div class="q">我想在提交前就拦下来</div>
      <div class="a"><a href="https://github.com/pgy763/llm-lint">llm-lint</a> 扫一遍 <code>src/main/java</code>，十条最容易踩的坑静态就能查出来</div>
    </div>
    <div class="path">
      <div class="q">我想看一个完整项目长什么样</div>"""
assert s.count(path_anchor) == 1
s = s.replace(path_anchor, path_add)

io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok", len(s))