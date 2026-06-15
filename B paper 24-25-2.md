这是一份针对**武汉理工大学2024-2025学年第2学期《高等数学A（下）》B卷**的详细解析 。选择题部分为您剖析核心考点与解题思路；计算题、解答题与证明题部分则严格按照**阅卷标准**提供规范的得分步骤 。

---

## 一、 选择题（每小题3分，共45分）

### 1. 旋转体体积

* **题目：** 圆形区域 $x^{2}+(y-b)^{2}\le a^{2}\ (b>a>0)$ 绕 $x$ 轴旋转一周所得旋转体的体积为（ ）。
* **解析：** 边界方程 $x^2+(y-b)^2=a^2$ 可解得上下半圆周分别为 $y_2(x) = b + \sqrt{a^2-x^2}$ 和 $y_1(x) = b - \sqrt{a^2-x^2}$，其中 $x \in [-a, a]$。采用平面圆环微元法，截面空心圆环的外半径为 $y_2(x)$，内半径为 $y_1(x)$。旋转体体积为 $V = \pi \int_{-a}^{a} [y_2^2(x) - y_1^2(x)] dx = \pi \int_{-a}^{a} [(b + \sqrt{a^2-x^2})^2 - (b - \sqrt{a^2-x^2})^2] dx = \pi \int_{-a}^{a} 4b\sqrt{a^2-x^2} dx = 4\pi b \int_{-a}^{a} \sqrt{a^2-x^2} dx$。由于定积分 $\int_{-a}^{a} \sqrt{a^2-x^2} dx$ 表示半径为 $a$ 的基准半圆面积 $\frac{1}{2}\pi a^2$，代入可得体积 $V = 4\pi b \cdot (\frac{1}{2}\pi a^2) = 2\pi^2 a^2 b$。
* **答案：** **(D)**


2. 一阶微分方程通解 

* **考点**：全微分方程、凑微分法。
* 
**解析**：将方程 $\frac{dy}{dx}=-\frac{2x+y}{x+2y}$ 改写为对称形式：$(2x+y)dx + (x+2y)dy = 0$ 。


* 展开得：$2xdx + ydx + xdy + 2ydy = 0$。
* 观察到 $ydx + xdy = d(xy)$，对其进行凑微分：

$$d(x^2) + d(xy) + d(y^2) = 0 \implies d(x^2 + xy + y^2) = 0$$


* 两边积分，得通解为 $x^2 + xy + y^2 = C$。


* 
**答案**：**(A)** 



3. 点关于平面的对称点 

* **考点**：空间解析几何、点到平面的对称点。
* 
**解析**：已知平面法向量为 $\vec{n} = (1,1,2)$ 。


* 设原点 $O(0,0,0)$ 在平面上的投影（垂足）为 $H$ 。过 $O$ 点且垂直于平面的直线方程为 $\frac{x}{1} = \frac{y}{1} = \frac{z}{2} = t$，即 $H$ 坐标可表示为 $(t, t, 2t)$。


* 将 $H$ 代入平面方程 $x+y+2z=6$：$t + t + 2(2t) = 6 \implies 6t = 6 \implies t = 1$ 。


* 故垂足为 $H(1,1,2)$。
* 设对称点为 $M'(x,y,z)$，则 $H$ 是 $OM'$ 的中点，即 $M' = 2H - O = (2,2,4)$。


* 
**答案**：**(D)** 



4. 空间直线的夹角 

* **考点**：直线的分方向向量、向量夹角公式。
* **解析**：
* 直线 $L_1$ 的方向向量为 $\vec{s}_1 = (5, 1, 3)$ 。


* 直线 $L_2$ 由两平面交线给出，其方向向量 $\vec{s}_2$ 垂直于两平面的法向量 $\vec{n}_1=(1,6,5)$ 和 $\vec{n}_2=(3,8,7)$ ：



$$\vec{s}_2 = \vec{n}_1 \times \vec{n}_2 = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & 6 & 5 \\ 3 & 8 & 7 \end{vmatrix} = (42-40)\vec{i} - (7-15)\vec{j} + (8-18)\vec{k} = (2, 8, -10)$$



方向向量可按比例简化为 $\vec{s}_2 = (1, 4, -5)$。
* 计算两向量夹角余弦值（直线夹角取锐角或直角）：

$$\cos\theta = \frac{|\vec{s}_1 \cdot \vec{s}_2|}{|\vec{s}_1||\vec{s}_2|} = \frac{|5 \times 1 + 1 \times 4 + 3 \times (-5)|}{\sqrt{5^2+1^2+3^2}\sqrt{1^2+4^2+(-5)^2}} = \frac{|-6|}{\sqrt{35}\sqrt{42}} = \frac{6}{7\sqrt{30}} = \frac{\sqrt{30}}{35}$$


* 因此 $\theta = \arccos\frac{\sqrt{30}}{35}$ 。




* 
**答案**：**(A)** 



5. 多元函数的连续、偏导与可微性 

* **考点**：二元函数的连续性、偏导数定义、全微分判定。
* **解析**：
1. **连续性**：利用极坐标代换 $x=r\cos\theta, y=r\sin\theta$，当 $r \to 0$ 时，$\left|f(x,y)\right| = \left|\frac{r^3\cos^2\theta\sin\theta}{r^2}\right| = r\left|\cos^2\theta\sin\theta\right| [cite_start]\le r \to 0 = f(0,0)$ ，故在 $(0,0)$ 处连续。


2. 
**偏导数**：依据定义，$f_x'(0,0) = \lim_{\Delta x\to0}\frac{f(\Delta x,0)-f(0,0)}{\Delta x} = 0$ ，同理 $f_y'(0,0) = 0$，偏导数存在。


3. **可微性**：考察全增量极限 $\lim_{(x,y)\to(0,0)}\frac{f(x,y)-f(0,0)-[f_x'(0,0)x+f_y'(0,0)y]}{\sqrt{x^2+y^2}} = \lim_{(x,y)\to(0,0)}\frac{x^2y}{(x^2+y^2)^{3/2}}$。沿着直线 $y=x$ 趋近时，极限为 $\frac{x^3}{(2x^2)^{3/2}} = \frac{1}{2\sqrt{2}} \ne 0$，故不可微。


* 
**答案**：**(C)** 



6. 高阶混合偏导数 

* **考点**：多元函数偏导数计算。
* 
**解析**：函数 $u(x,y)=x^{y}$ 。


* 先对 $x$ 求偏导（此时 $y$ 视为常数）：$\frac{\partial u}{\partial x} = yx^{y-1}$ 。


* 再对 $y$ 求偏导（应用乘积求导法则与指数函数求导公式）：

$$\frac{\partial^{2}u}{\partial x\partial y} = \frac{\partial}{\partial y}(yx^{y-1}) = 1 \cdot x^{y-1} + y \cdot (x^{y-1}\ln x) = x^{y-1}(1+y\ln x)$$




* 
**答案**：**(C)** 



7. 速度与加速度的垂直时刻 

* **考点**：向量值函数的导数、向量垂直的充要条件。
* **解析**：
* 速度向量为位置向量的一阶导数：$\vec{v}(t) = \vec{r}'(t) = (1, 2t, 3t^2-3)$ 。


* 加速度向量为二阶导数：$\vec{a}(t) = \vec{v}'(t) = (0, 2, 6t)$ 。


* 速度与加速度垂直 $\iff \vec{v}(t) \cdot \vec{a}(t) = 0$ ：



$$1 \times 0 + 2t \times 2 + (3t^2-3) \times 6t = 0 \implies 4t + 18t^3 - 18t = 0 \implies 18t^3 - 14t = 0$$


* 因 $t>0$，方程两边同除以 $2t$ 得 $9t^2 - 7 = 0 \implies t = \frac{\sqrt{7}}{3}$ 。在 $t>0$ 范围内有且仅有 $1$ 个解 。




* 
**答案**：**(B)** 



8. 条件极值的必要条件 

* **考点**：拉格朗日乘数法。
* 
**解析**：根据拉格朗日乘数法，在约束极值点 $(0,0)$ 处必存在常数 $\lambda$，使得拉格朗日函数 $L(x,y) = f(x,y) + \lambda \varphi(x,y)$ 满足一阶导数为 $0$ ：



$$\begin{cases} f_x'(0,0) + \lambda \varphi_x'(0,0) = 0 \\ f_y'(0,0) + \lambda \varphi_y'(0,0) = 0 \end{cases}$$


* 题目给出 $\varphi_{y}^{\prime}(x,y)\ne0$ ，由此可得：$\lambda = -\frac{f_y'(0,0)}{\varphi_y'(0,0)}$。


* 代入第一式得：$f_x'(0,0) - \frac{f_y'(0,0)}{\varphi_y'(0,0)}\varphi_x'(0,0) = 0 \implies f_x'(0,0)\varphi_y'(0,0) = f_y'(0,0)\varphi_x'(0,0)$。
* 若 $f_x'(0,0) \ne 0$，由于 $\varphi_y'(0,0) \ne 0$，则等式左边不为 $0$，故右边的 $f_y'(0,0)$ 绝不能为 $0$ 。




* 
**答案**：**(D)** 



9. 极坐标积分转化为直角坐标 

* **考点**：二重积分坐标系转换、积分区域边界方程转化。
* 
**解析**：由累次积分得积分区域 $D$ 为：$0 \le \theta \le \frac{\pi}{2},\ 0 \le r \le 2\sin\theta$ 。


* 边界曲线 $r = 2\sin\theta \implies r^2 = 2r\sin\theta$，化为直角坐标方程为 $x^2 + y^2 = 2y \implies x^2 + (y-1)^2 = 1$。
* 由于 $\theta \in [0, \frac{\pi}{2}]$ ，区域 $D$ 是位于第一象限的半圆。


* 改写为先对 $x$ 后对 $y$ 的二重积分：$y$ 的外层取值范围为 $[0, 2]$；对于固定的 $y$，内层 $x$ 从 $0$ 变换到圆周 $x = \sqrt{2y-y^2}$。
* 故改写为：$\int_{0}^{2}dy\int_{0}^{\sqrt{2y-y^2}}f(x,y)dx$ 。




* 
**答案**：**(C)** 



10. 三重积分的性质判断 

* **考点**：三重积分的对称性与轮换对称性。
* **解析**：
* 
$\Omega_1$ 是上半球 $z \ge 0$ 。在 $\Omega_1$ 中，依据轮换对称性，因区域关于 $x$ 和 $y$ 具有奇偶对称性（且 $x, y$ 轴对称不变），可得 $\iiint_{\Omega_1} x dV = \iiint_{\Omega_1} y dV = 0$。


* 因此，$\iiint_{\Omega_1}(x+y+z)dV = \iiint_{\Omega_1} x dV + \iiint_{\Omega_1} y dV + \iiint_{\Omega_1} z dV = \iiint_{\Omega_1} z dV$ 。


* 选项 (D) 指出结果为 $3\iiint_{\Omega_1} zdV$ ，显然错误（误用了全全对称球体的结论）。




* 
**答案**：**(D)** 



11. 第一类曲线积分 

* **考点**：第一类曲线积分、交线圆的参数化。
* 
**解析**：曲线 $\Gamma$ 为球面与平面 $y=x$ 的交线 。该曲线是一个包含 $z$ 轴立面上的单位大圆，具有空间几何特殊性。


* 选取平面 $y=x$ 上互相垂直的两个单位向量作为基底：$\vec{u}_1 = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0)$，$\vec{u}_2 = (0,0,1)$。
* 写出 $\Gamma$ 的参数方程：$x = \frac{\cos\theta}{\sqrt{2}},\ y = \frac{\cos\theta}{\sqrt{2}},\ z = \sin\theta\ (\theta \in [0, 2\pi])$。
* 弧长微元 $ds = d\theta$。
* 代入积分中：$\oint_{\Gamma}(x^{2}+y^{2})ds = \int_{0}^{2\pi} \left(\frac{\cos^2\theta}{2} + \frac{\cos^2\theta}{2}\right) d\theta = \int_{0}^{2\pi} \cos^2\theta d\theta = \pi$ 。




* 
**答案**：**(A)** 



12. 第一类曲面积分 

* **考点**：第一类曲面积分、球面轮换对称性。
* 
**解析**：展开被积函数：$(x+y)^2 = x^2 + 2xy + y^2$ 。


* 依据球面对称性，奇函数项积分 $\iint_{\Sigma} 2xy dS = 0$ 。


* 依据轮换对称性，$\iint_{\Sigma} x^2 dS = \iint_{\Sigma} y^2 dS = \iint_{\Sigma} z^2 dS$ 。


* 由于在球面上 $x^2+y^2+z^2=1$ ，则 $3\iint_{\Sigma} x^2 dS = \iint_{\Sigma} 1 dS = 4\pi \implies \iint_{\Sigma} x^2 dS = \frac{4\pi}{3}$。


* 故 $\iint_{\Sigma}(x+y)^{2}dS = \iint_{\Sigma} x^2 dS + \iint_{\Sigma} y^2 dS = \frac{4\pi}{3} + \frac{4\pi}{3} = \frac{8\pi}{3}$ 。




* 
**答案**：**(D)** 



13. 数项级数敛散性命题判断 

* **考点**：级数收敛的定义及反例。
* **解析**：
* 1) 错。反例：$\sum (-1)^n$，部分和有界但级数发散 。


* 2) 错。反例：$\sum (-1)^n$，部分和振荡发散，极限不为 $\infty$ 。


* 3) 错。仅对正项级数成立。交错级数反例：$u_n = \frac{(-1)^n}{\sqrt{n}}$ 收敛，但 $u_n^2 = \frac{1}{n}$ 发散 。


* 4. 错。必须要求 $\sum u_n$ 绝对收敛才行。反例：$u_n = \frac{(-1)^n}{n}$（条件收敛），取 $v_n = \frac{1}{n}$ 满足 $|v_n| [cite_start]\le |u_n|$，但 $\sum v_n$ 发散 。




* 4个结论全部错误 。




* 
**答案**：**(D)** 



14. 条件收敛级数的拆分 

* **考点**：条件收敛的定义、级数的可加性。
* 
**解析**：级数 $\sum_{n=1}^{\infty}(-1)^{n}a_{n}$ 条件收敛，意味着 $\sum (-1)^n a_n$ 收敛，而正项级数 $\sum a_n$ 发散 。


* 将正项级数拆为奇偶项：$\sum a_n = \sum a_{2n} + \sum a_{2n-1}$ 。因其发散，故两子项级数至少有一个发散。


* 原级数展开：$\sum (-1)^n a_n = \sum a_{2n} - \sum a_{2n-1}$ 。因其收敛，表明两级数之差为有限值。


* 一个收敛级数与一个发散级数相减不可能收敛，因此 $\sum a_{2n}$ 和 $\sum a_{2n-1}$ 必须**同时发散** 。


* 由此可知：和级数 $\sum a_{2n} + \sum a_{2n-1}$ 发散 ；差级数 $\sum a_{2n} - \sum a_{2n-1}$ 收敛 。




* 
**答案**：**(C)** 



15. 幂级数的收敛半径 

* **考点**：达朗贝尔比值法求收敛半径。
* 
**解析**：通项为 $u_n(x) = c_n x^{2n+1}$，其中 $c_n = \frac{(2n+1)!}{(n!)^{2}}$ 。



$$\lim_{n\to\infty} \left| \frac{u_{n+1}(x)}{u_n(x)} \right| = \lim_{n\to\infty} \frac{(2n+3)!}{[(n+1)!]^2} \cdot \frac{[n!]^2}{(2n+1)!} \cdot |x|^2 = \lim_{n\to\infty} \frac{(2n+3)(2n+2)}{(n+1)^2} |x|^2 = 4|x|^2$$



令 $4|x|^2 < 1 \implies |x| [cite_start]< \frac{1}{2}$，故收敛半径 $R = \frac{1}{2}$ 。


* 
**答案**：**(D)** 



---

二、 计算题（每小题8分，共40分） 

16. 求微分方程 $y^{\prime}=\frac{1}{2x+e^{2y}}$ 的通解 。

解：将 $x$ 视为因变量，$y$ 视为自变量，原方程转化为：


$$\frac{dx}{dy} = 2x + e^{2y} \quad \text{--- (2分)}$$


移项得一阶线性非齐次微分方程标准式：


$$\frac{dx}{dy} - 2x = e^{2y} \quad \text{--- (4分)}$$


由一阶线性微分方程公式，通解为：


$$x = e^{-\int (-2)dy} \left[ \int e^{2y} \cdot e^{\int (-2)dy} dy + C \right] \quad \text{--- (6分)}$$

$$x = e^{2y} \left[ \int e^{2y} \cdot e^{-2y} dy + C \right] = e^{2y} (y + C)$$


故微分方程的通解为：$x = (y+C)e^{2y}$ 。 $\quad \text{--- (8分)}$

---

17. 求 $z(x,y)=x^{3}-4x^{2}+2xy-y^{2}$ 的极值和极值点 。

解：首先计算一阶偏导数，并令其为 $0$ 寻找驻点：


$$\begin{cases} z_x' = 3x^2 - 8x + 2y = 0 \\ z_y' = 2x - 2y = 0 \end{cases} \quad \text{--- (2分)}$$


由第二式得 $y = x$，代入第一式得 $3x^2 - 6x = 0 \implies 3x(x-2) = 0$。
解得驻点为：$M_1(0,0)$ 和 $M_2(2,2)$。 $\quad \text{--- (4分)}$
再求二阶偏导数：$A = z_{xx}'' = 6x - 8$，$B = z_{xy}'' = 2$，$C = z_{yy}'' = -2$。

1. **对于驻点 $M_1(0,0)$**：
$A = -8$，$B = 2$，$C = -2$。
$\Delta = AC - B^2 = (-8) \times (-2) - 2^2 = 12 > 0$。
因 $\Delta > 0$ 且 $A < 0$，故 $M_1(0,0)$ 是极大值点，极大值为 $z(0,0) = 0$。 $\quad \text{--- (6分)}$
2. **对于驻点 $M_2(2,2)$**：
$A = 4$項目，$B = 2$，$C = -2$。
$\Delta = AC - B^2 = 4 \times (-2) - 2^2 = -12 < 0$。
因 $\Delta < 0$，该点不是极值点。 $\quad \text{--- (7分)}$
**结论**：极大值点为 $(0,0)$，极大值为 $0$；无极小值。 $\quad \text{--- (8分)}$

---

18. 设函数 $y=y(x)$, $z=z(x)$ 由方程组 $\begin{cases}x+y+z=0\\ x^{2}+y^{2}+z^{2}=1\end{cases}$ 所确定，求 $\frac{dy}{dx}\Big|_{(\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2},0)}$ 和 $\frac{dz}{dx}\Big|_{(\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2},0)}$ 。

解：方程组两边同时对 $x$ 求导，得：


$$\begin{cases} 1 + \frac{dy}{dx} + \frac{dz}{dx} = 0 \\ 2x + 2y\frac{dy}{dx} + 2z\frac{dz}{dx} = 0 \end{cases} \quad \text{--- (4分)}$$

将点 $\left(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}, 0\right)$ 代入上述导数方程组中 ：


$$\begin{cases} 1 + \frac{dy}{dx} + \frac{dz}{dx} = 0 \\ \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\frac{dy}{dx} = 0 \end{cases} \quad \text{--- (6分)}$$


由第二式解得：$\frac{dy}{dx} = 1$。
代入第一式解得：$\frac{dz}{dx} = -2$。
故所求偏导数为：$\frac{dy}{dx} = 1$ , $\frac{dz}{dx} = -2$ 。 $\quad \text{--- (8分)}$

---

19. 计算曲线积分 $\oint_{L}\frac{-ydx+xdy}{x^{2}+y^{2}}$，其中 $L$ 为椭圆 $\frac{(x-1)^{2}}{16}+\frac{y^{2}}{4}=1$，取逆时针方向 。

解：被积函数的奇点为原点 $(0,0)$，经检验，原点 $(0,0)$ 位于椭圆 $L$ 的内部 。
在 $L$ 内部围绕原点作一顺应逆时针方向的足够小的圆周 $L_r: x^2 + y^2 = r^2$。 $\quad \text{--- (2分)}$
由格林公式的复连通区域性质，由于在两曲线围成的区域内满足 $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} = \frac{y^2-x^2}{(x^2+y^2)^2}$，因此有：


$$\oint_{L} \frac{-ydx+xdy}{x^{2}+y^{2}} = \oint_{L_r} \frac{-ydx+xdy}{x^{2}+y^{2}} \quad \text{--- (4分)}$$


引入小圆周 $L_r$ 的参数方程：$x = r\cos\theta, y = r\sin\theta\ (\theta: 0 \to 2\pi)$。
则 $dx = -r\sin\theta d\theta$，$dy = r\cos\theta d\theta$，$x^2+y^2 = r^2$。 $\quad \text{--- (6分)}$
代入积分得：


$$\oint_{L_r} \frac{-ydx+xdy}{x^{2}+y^{2}} = \int_{0}^{2\pi} \frac{-r\sin\theta(-r\sin\theta) + r\cos\theta(r\cos\theta)}{r^2} d\theta = \int_{0}^{2\pi} 1 d\theta = 2\pi$$


故原曲线积分值为 $2\pi$。 $\quad \text{--- (8分)}$

---

20. 计算曲面积分 $\iint_{S}(y\sin z+x)dydz+ydzdx-2zdxdy$，其中 $S$ 为曲面 $z=\frac{1}{2}(x^{2}+y^{2})$ 介于 $z=0$ 及 $z=1$ 之间的部分取下侧 。

解：补加一个平面平顶盖面 $S_1: z = 1, x^2 + y^2 \le 2$，取上侧 。
设 $S$ 与 $S_1$ 共同围成的封闭立体区域为 $\Omega$ 。由于 $S$ 取下侧，$S_1$ 取上侧，此时整个封闭曲面方向朝外 。 $\quad \text{--- (2分)}$
根据高斯公式：


$$\iint_{S+S_1} = \iiint_{\Omega} \left[ \frac{\partial(y\sin z+x)}{\partial x} + \frac{\partial(y)}{\partial y} + \frac{\partial(-2z)}{\partial z} \right] dV \quad \text{--- (4分)}$$

$$\iiint_{\Omega} (1 + 1 - 2) dV = 0 \implies \iint_{S} = - \iint_{S_1} \quad \text{--- (5分)}$$


在 $S_1$ 上，$z = 1$，$dydz = 0, dzdx = 0$，且 $dxdy$ 方向朝上取正号：


$$\iint_{S_1} -2z dxdy = \iint_{x^2+y^2\le 2} -2(1) dxdy = -2 \times \text{Area}(x^2+y^2\le 2) \quad \text{--- (7分)}$$


该圆盘半径为 $\sqrt{2}$，面积为 $2\pi$。故 $\iint_{S_1} = -4\pi$。
因此，$\iint_{S} = -(-4\pi) = 4\pi$。 $\quad \text{--- (8分)}$

---

三、 解答题（本题共1小题，共9分） 

21. 平面薄片由曲线 $y=x^{2}$ 和直线 $y=1$ 围成（其面密度为1），试求：(1)该平面薄片的重心坐标；(2)该平面薄片关于y轴的转动惯量 。

解：(1) 确定积分区域 $D: -1 \le x \le 1,\ x^2 \le y \le 1$。

* 计算薄片质量 $M$：

$$M = \iint_{D} 1 dA = \int_{-1}^{1} dx \int_{x^2}^{1} dy = \int_{-1}^{1} (1-x^2)dx = \left[ x - \frac{1}{3}x^3 \right]_{-1}^{1} = \frac{4}{3} \quad \text{--- (2分)}$$


* 求重心坐标 $(\bar{x}, \bar{y})$ ：
因区域 $D$ 关于 $y$ 轴对称且密度均匀，故由对称性直接得 $\bar{x} = 0$。 $\quad \text{--- (3分)}$



$$M_x = \iint_{D} y dA = \int_{-1}^{1} dx \int_{x^2}^{1} y dy = \frac{1}{2}\int_{-1}^{1} (1-x^4)dx = \int_{0}^{1}(1-x^4)dx = \frac{4}{5} \quad \text{--- (5分)}$$


$$\bar{y} = \frac{M_x}{M} = \frac{4/5}{4/3} = \frac{3}{5}$$



故重心坐标为 $\left(0, \frac{3}{5}\right)$。 $\quad \text{--- (6分)}$

(2) 计算关于 $y$ 轴的转动惯量 $I_y$ ：


$$I_y = \iint_{D} x^2 dA = \int_{-1}^{1} x^2 dx \int_{x^2}^{1} dy = \int_{-1}^{1} x^2(1-x^2)dx \quad \text{--- (7分)}$$

$$I_y = 2\int_{0}^{1} (x^2 - x^4)dx = 2\left[ \frac{1}{3}x^3 - \frac{1}{5}x^5 \right]_{0}^{1} = 2 \times \frac{2}{15} = \frac{4}{15}$$


故薄片关于 $y$ 轴的转动惯量为 $\frac{4}{15}$。 $\quad \text{--- (9分)}$

---

四、 证明题（本题共1小题，共6分） 

22. 若 $a_{n}>0\ (n=1,2,\cdot\cdot\cdot), S_{n}=\sum_{k=1}^{n}a_{k}$。试证明：对任意常数 $p>1$，级数 $\sum_{n=2}^{\infty}\frac{a_{n}}{S_{n}^{p}}$ 收敛 。

证明：
因为 $a_n > 0$，所以部分和序列 $\{S_n\}$ 严格单调递增，即 $S_n > S_{n-1} > 0$ 。
注意到 $a_n = S_n - S_{n-1}$ ，考虑函数 $f(x) = \frac{1}{x^p}$ 在区间 $[S_{n-1}, S_n]$ 上的定积分。 $\quad \text{--- (2分)}$
由于当 $x > 0, p > 1$ 时，$f(x) = \frac{1}{x^p}$ 是严格单调递减函数，因此在区间 $[S_{n-1}, S_n]$ 上满足：


$$\int_{S_{n-1}}^{S_n} \frac{1}{x^p} dx > \frac{1}{S_n^p} \cdot (S_n - S_{n-1}) = \frac{a_n}{S_n^p} \quad \text{--- (3分)}$$


对积分进行计算，可得放缩不等式：


$$\frac{a_n}{S_n^p} < \int_{S_{n-1}}^{S_n} x^{-p} dx = \frac{1}{p-1} \left( \frac{1}{S_{n-1}^{p-1}} - \frac{1}{S_n^{p-1}} \right) \quad \text{--- (4分)}$$


对级数的前 $N$ 项部分和进行裂项求和放缩：


$$\sum_{n=2}^{N} \frac{a_n}{S_n^p} < \frac{1}{p-1} \sum_{n=2}^{N} \left( \frac{1}{S_{n-1}^{p-1}} - \frac{1}{S_n^{p-1}} \right) = \frac{1}{p-1} \left( \frac{1}{S_1^{p-1}} - \frac{1}{S_N^{p-1}} \right) \quad \text{--- (5分)}$$


由于 $S_N^{p-1} > 0$，进一步可放大为：


$$\sum_{n=2}^{N} \frac{a_n}{S_n^p} < \frac{1}{p-1} \cdot \frac{1}{S_1^{p-1}} (\text{常数})$$

由此可知，正项级数 $\sum_{n=2}^{\infty}\frac{a_{n}}{S_{n}^{p}}$ 的部分和数列有上界 。根据正项级数收敛的有界性准则，该级数必定收敛。 $\quad \text{--- (6分)}$
