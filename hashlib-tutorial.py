# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h1>hashlib --- 安全哈希与消息摘要</h1>
# 

# %%
import hashlib

# 所运行的 Python 解释器上可用的哈希算法的名称
print(hashlib.algorithms_available)


# %%
# 模块在所有平台上都保证支持的哈希算法的名称
print(hashlib.algorithms_guaranteed)


# %%
# 每种类型的哈希算法都有一个构造器方法
# 例如，md5()，sha1(), sha224(), sha256(), sha384(), sha512(), blake2b() 和 blake2s()等。
sha256 = hashlib.sha256()

# 通过 update() 方法向该对象输入字节对象(通常是bytes)
# 例如要计算 b'Nobody inspects the spammish repetition' 的安全哈希
sha256.update(b'Nobody inspects the ')
sha256.update(b'spammish repetition')

# 返回已传给 update() 方法的数据的安全哈希,大小为 digest_size 的字节串对象
print(sha256.digest())
print(sha256.digest_size)


# %%
# 类似于 digest() 但安全哈希会以两倍长度字符串对象的形式返回，其中仅包含十六进制数码
print(sha256.hexdigest())

