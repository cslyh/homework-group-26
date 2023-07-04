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

- **充分利用CPU**，进程数设置为multiprocessing.cpu_count()，使用python多进程加速
- **使用共享字典存储**，牺牲空间换时间

## 实现效果

完成32、40、48bit碰撞

![1688481001212](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688481001212.png)

![img](file:///D:\Tencent\QQData\1803601837\Image\C2C\9CIPCD2_BG}$%U15HOCE4Z3.png)

![1688479181209](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688479181209.png)

![1688479193792](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688479193792.png)





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

![1688480947344](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688480947344.png)

![1688479372325](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688479372325.png)

![1688479380511](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688479380511.png)

![1688479385843](C:\Users\HBenF\AppData\Roaming\Typora\typora-user-images\1688479385843.png)
