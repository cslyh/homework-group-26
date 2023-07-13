**姓名：罗裕辉       学号：202100460046**

负责project:1,2,3,4,5,9,11,13,14,17,21（全部由本人单独完成）

以下是项目报告，从**原理、实现特点、实现效果**三方面展现

# Project1:implement the naïve birthday attack of reduced SM3

## 原理

1. 攻击者预先选择一组随机的输入（消息）并计算它们的哈希值。
2. 攻击者检查这些哈希值中是否存在相同的值，即找到了一个碰撞。如果找到碰撞，攻击者可以利用它来破解加密算法或密码散列函数，例如找到两个具有相同哈希值的不同输入。
3. 攻击者可以通过逐渐增加随机输入的数量，增加产生碰撞的概率。根据生日悖论，当输入数量接近输出值的平方根时，碰撞的概率达到50%以上。
4. 一旦发现碰撞，攻击者可以进一步分析攻击目标，如密钥破解、伪装身份、篡改数据等。

## 环境配置

CPU：i7-13700h

解释器：anaconda3-2023

## 实现特点

- **充分利用CPU的算力**，进程数设置为multiprocessing.cpu_count()，使用python多进程加速
![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/ef194b9d-0e6a-4525-a440-4ee3fe138a4c)

- **使用共享字典存储**，牺牲空间换时间

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/1573c147-de9e-4b5e-92ef-35e83d9c930c)


## 实现效果

完成32、40、48bit碰撞

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/b3b25ccf-143b-4038-ba36-b366ebf1c6f5)


![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/50ef1cee-4e09-4acd-a689-d0046500e82b)

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/3926bced-8e27-4ad2-a611-a8440b8fa155)


![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/4779ce37-f1a2-4f0e-b6c8-73ae0197fce0)






# Project2: implement the Rho method of reduced SM3

## 原理

1. 选择一个递推序列的初始值x0，并定义一个递归函数f(x)。递归函数f(x)可以是一个简单的数学函数，比如f(x) = x^2 + 1。
2. 通过重复应用递归函数f(x)，得到一系列序列x0, x1, x2, ..., xi。这些序列值遵循一个循环节，即存在两个序列值xi和xj，使得xi ≡ xj (mod n)。
3. 使用Floyd循环检测算法（Floyd's cycle-finding algorithm），在序列中找到循环节的起始位置。
4. 根据循环节的性质，使用在循环节内生成的序列值计算出n的一个非平凡因子。
5. 递归地应用Pollard Rho算法，直到将n分解为素数的乘积。

## 环境配置

CPU：i7-13700h

解释器：anaconda3-2023

## 实现特点

- 按照思想随机设置一个初始值不断迭代，仍然是**使用共享字典存储**，牺牲空间换时间

## 实现效果

完成32、40、48bit碰撞，并且比生日攻击更快，可能是由于是递归迭代，字符串不够随机

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/026f54e9-37eb-4ddb-be5b-ccd2ca17a23d)


![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/c0510e6c-9b9b-4101-9fae-5dcf2d1e6541)


![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/2a7c78dc-759e-4d61-a590-a65d771e3814)

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/01a1b06d-4756-436b-90d5-19f618f5c283)




# Project3: implement length extension attack for SM3, SHA256, etc.

## 原理

这里的长度扩展攻击主要是针对MD结构的，因为MD结构是**分块迭代进行哈希**计算的方式，附上密码学引论慕课上的图和SM3的填充规则，因此我们可以在原始消息后按照规则填充至512整数倍后再填充任意消息实现长度扩展攻击：

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/30aaee05-ba21-45c6-9206-01105fcb3306)


![img](https://pic3.zhimg.com/v2-366d5284c75a6ac92fdbc12ce5b45a2a_r.jpg)

## 实现特点

- 填充攻击：根据上面阐述的原理，在原始消息后按照规则填充至512整数倍后再填充任意消息实现长度扩展攻击

## 实现效果

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/20aeb116-1bf1-4d96-a536-6765b1076b19)






# Project4: do your best to optimize SM3 implementation (software)

## 原理

参考网上资料，SM3的过程如下

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/30357310-8157-41fa-8a55-14bc40489c3c)


由于要求对SM3进行软件优化，经过思考发现，在SM3算法中，关键的是中间的8个32位整数，它们分别表示为`a`、`b`、`c`、`d`、`e`、`f`、`g`和`h`。这些中间值在SM3算法的压缩函数中起着重要的作用。在每个压缩函数的迭代中，这些中间值会根据输入数据和常量进行更新和变换。它们的变化过程是SM3算法中的核心部分。因此主要考虑如何提高这8个32位整数变换的并行度。

## 环境配置

CPU：i7-13700h

JDK版本：Java8

IDE：IDEA2019.2.3

## 实现特点

考虑到使用方便，采用Java语言实现SM3，并在两处使用Java并行流进行优化，如下：

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/13cc415d-f596-4ebe-86c8-464d0bd3a46f)

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/e98d64cf-c1c8-4440-8f81-8487d9c8cf5f)


> 介绍：Java并行流是Java 8引入的一种并行处理数据流的机制。它可以将一个数据流分成多个子流，并行地对每个子流进行操作，从而提高处理大量数据的效率。使用并行流可以简化并行处理的编程模型，无需显式地创建和管理线程。Java并行流内部使用了Fork/Join框架来自动将任务分配给多个线程执行，并将结果合并。

## 实现效果

运行结果为1.55ms完成一次SM3运算

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/af0f8dbd-88b3-41ba-90e6-c425bbdbd8b1)


# Project5: Impl Merkle Tree following RFC6962

## 原理

RFC 6962定义了一种用于可信日志（例如证书透明性日志）的Merkle树结构。该Merkle树的目的是提供一种有效的方式来验证日志中的条目是否存在，且日志内容未被篡改。其中，Merkle树被称为"Log Tree"，它由叶子节点和内部节点组成。每个叶子节点都包含一个数据条目以及对应的哈希值。内部节点则表示其子节点的哈希值。

## 实现特点

- 使用RFC 6962定义的Merkle树结构：通过递归方式构建树，并使用SHA-256哈希函数计算节点的哈希值。
- 支持任意数量的叶子节点：代码中的`construct_tree`函数可以处理任意数量的叶子节点，并将它们组织成一个Merkle树。
- 支持验证证明：提供了`verify_proof`函数来验证Merkle树中的证明。通过给定叶子节点、证明路径和根哈希，可以验证该叶子节点是否属于Merkle树。

## 实现效果

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/718598b5-0aa4-4bee-a028-527c4e5bfca9)






# Project9: AES / SM4 software implementation

## 原理

SM4的流程图如下：

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/c0f69d8b-ef0c-411b-a88a-b9b585845d88)


目标是优化SM4，考虑到之前计原做过在FPGA上优化加速SM4的实验，加速到2万多倍，参考那次实验完成优化。

## 实现特点

- inline内联：inline是C++关键字，当函数被声明为`inline`时，编译器会尝试将函数的代码插入到调用该函数的地方，而不是通过函数调用的方式执行。这样可以减少函数调用的开销，提高程序的执行效率。这里使用到一些基本算子中。

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/3df5ec11-60f8-404a-ae03-ebd866304c38)


- unroll循环展开：循环展开是一种优化技术，通过将循环中的迭代次数减少，将循环体的代码复制多次来减少循环的开销。这样可以减少循环控制的开销、提高指令级并行性和减少分支预测错误的可能性。这里在最后的密文加载手动循环展开4轮，受限于环境，在FPGA上可以完全展开。

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/271b03f0-c9fd-44fc-a703-c9b475fb0a42)


- 位移操作：位移操作是一种在二进制级别上对数据进行移动的操作，相比四则运算它更快，因此在代码实现中尽可能采用位移操作提速
- SIMD指令：SIMD是单指令多数据，但是可能是由于代码中我们使用的是32位的uint32_t类型，而SSE指令集中128位的__m128i，存在格式转换问题，以及一些数据依赖问题，使用如下的优化后效果不明显，因此并没有采用。

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/669cd111-25a2-4019-bdc7-bce5bae4ee6c)


## 实现效果

0.0016ms完成一次SM4

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/301d76c6-1dbb-4734-a81e-adc05f35b494)


# Project11: impl sm2 with RFC6979

## 原理

SM2 是中国国家密码管理局发布的非对称加密算法标准，而 RFC6979 是一种用于确定性签名密钥生成的方法。将 SM2 与 RFC6979 结合，可以实现使用确定性 K 值生成的方式进行 SM2 的签名操作，其中RFC6979 定义了一种基于 HMAC和KDF的方法，用于生成确定性的 K 值，从而避免了传统算法中需要依赖伪随机数生成器。

## 实现特点

- 由于重点在于k值的生成，因此我们重点实现了K值生成函数

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/71f01541-4332-4b03-b204-e3a8de87e3eb)


- 椭圆曲线参数采用GM/T 0003.1-2012 标准，其余直接调用python库函数，并进行签名和验签应用

## 实现效果

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/a32131db-c05d-4fae-ae48-e25b84e23831)


# Project13: Implement the above ECMH scheme

## 原理

ECMH是一种基于椭圆曲线的加密方案，它结合了椭圆曲线的离散对数难题和椭圆曲线上的点加法运算，从而提供了安全性和效率，具体来说，就是哈希映射成椭圆曲线上的点，然后利用ECC的加法。由于结合了哈希运算，安全性更高。网上找到一篇论文：[1601.06502.pdf (arxiv.org)](https://arxiv.org/pdf/1601.06502.pdf)

## 实现特点

- 哈希映射，将消息哈希后映射成椭圆曲线上的点

  ![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/6d0d568f-f5a1-4231-b66d-3e963c492896)


- ECC的加法，按照ECC的加法规则进行即可
![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/92074591-590c-4c78-a1fa-9ec69ad77032)


## 实现效果

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/36dbafc5-7a0f-4892-8de7-4e787251f563)


# Project14: Implement a PGP scheme with SM2

## 原理

PGP是一种混合加密方案，它的主要思想是使用对称加密算法来加密数据的内容，使用非对称加密算法来加密对称密钥，然后再对加密后的对称密钥和签名数据进行哈希，并使用发送者的私钥进行加密。这样，可以确保数据的机密性、完整性和身份验证。

## 实现特点

- 重点实现PGP的加密运用，采用安全性更高的OAEP

 ![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/3ed969cc-b0aa-432f-847a-4b2f0cf41e21)


- 其余调用库函数实现，主要实现好它们之间的组合运用

## 实现效果

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/1d443a8c-673e-4f0b-9301-9adb47cd7388)


# Project17：比较Firefox和谷歌的记住密码插件的实现区别

## 原理

主要查找文档

Filefor:https://support.mozilla.org/en-US/kb/getting-started-firefox-lockwise

谷歌：<https://support.google.com/chrome/answer/95606>

## 区别

根据文档说明可知，二者有以下区别：

- 密码管理器：Firefox使用称为"Firefox Lockwise"的密码管理器，该管理器会在设备和Firefox帐户之间对密码进行同步，而Google Chrome使用Google帐户对密码进行同步
- 储存：Firefox的密码保存在一个本地的加密数据库中，Google Chrome的密码也被保存在一个加密的本地数据库中，但对于Windows用户，这些密码在某些情况下可以通过Windows凭证访问，所以个别场景下才可能存在泄露隐患。

- 其他：Firefox提供了一个主密码功能，该功能可以在其他人尝试查看存储的密码时要求输入，而在Google Chrome中，可以选择为特定的站点“永不保存密码”。

# Project21: Schnorr Bacth

## 原理

Schnorr Batch 是基于 Schnorr 签名算法的改进版本，用于在一个批处理中同时验证多个签名。它可以显著提高批量验证签名的效率，减少计算和通信开销，具体步骤如下：

1. 收集所有要签名的消息，并计算它们的哈希值。
2. 生成一个随机数作为签名过程中的挑战值。
3. 对所有的哈希值进行线性组合，生成一个新的哈希值。
4. 使用新的哈希值、挑战值和私钥，计算出签名的部分签名值。
5. 对于每个签名，根据部分签名值和挑战值计算出最终的签名值。

这样，我们只需要一次离散对数计算和一次哈希函数计算就可以生成多个签名，而不是为每个签名单独执行这些计算。

## 实现特点

- 批量签名的应用：先计算统计批量挑战再进行分块并批量签名，并以'Project21'和 'Schnorr Bacth'两个消息作为测试

 ![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/a0d1c72b-49af-43ef-8bc2-73754fe77684)


## 实现效果

一次性产生了两个签名

![image](https://github.com/sdu-benfu/homework-group-26/assets/92632263/b43fe413-c34c-4f5f-995d-156e1484e261)


