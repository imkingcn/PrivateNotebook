## **Java(基础内容)**

### Java语言的特点

- **面向对象性**：两个基本概念：类、对象；三大特性：**封装、继承、多态**
- 健壮性：吸收了C/C++语言的优点，但去掉了其影响程序健壮性的部分（如指针、内存的申请与释放等），提供了一个相对安全的内存管理和访问机制
- 跨平台性：通过Java语言编写的应用程序在不同的系统平台上都可以运行。“Write once , Run Anywhere”

### JDK,JRE和JVM的关系是什么？以及JDK、JRE包含的主要结构有哪些？

- 关系：JDK包含JRE，JRE包含JVM
- JDK = JRE + Java开发工具（javac.exe、java.exe、javadoc.exe）
- JRD = JVM + Java核心类库

## 注释

1. `//单行注释`
2. `/*多行注释*/`
3. `/**文档注释（Java特有）*/`

### 单行和多行注释的作用

1. 对所写程序进行解释说明，增强可读性，方便自己和别人。
2. 调试所写代码（注释掉不需要运行部分）。
3. 特点：单行和多行注释掉的内容不参与编译，编译以后生成的.class文件中不包含注释掉的信息。

### 文档注释的使用

1. 注释内容可以被JDK提供的工具javadoc所解析，生成一套以网页文件形式体现的该程序的说明文档。

2. 操作方式

   - > javadoc -d [生成文件名] -author -version [解析文件名.java]（-author和-version分别为注释当中@author和@version后面的内容）

- **注意：多行注释不能嵌套使用**

## 编译

- 每个人的第一行代码便是`Hello World`

  ```Java
  public class Hello{
          public static void main(String[] args){
              System.out.println("Hello World !");
          }
      }
  ```

  1. java程序的**编写-编译-运行**的过程
     - 编写：我们将编写的java代码保存在以“.java”结尾的源文件中
     - 编译：使用javac.exe来编译我们的java源文件。格式：`avac 源文件名.java`
     - 运行：使用java.exe解释运行我们的字节码文件（.class)。格式：`java 类名`
  2. 在一个`java`源文件中可以声明多个类（`class`包括`内部类`和`外部类`），但是**只能有一个类声明为`public`的，而且要求声明为`public`的类的类名必须与源文件名必须相同**。
  3. 程序的入口是`main()`方法，格式是固定的。可以写成：`public static void main(String[] args)`或`public static void main(String[] a)`或`public static void main(String a[])`
  4. 输出语句
     - `System.out.println()`：输出后换行，无内容则只换行
     - `System.out.print()`：输出后不换行
  5. 每一个执行语句都以分号结尾，每个执行语句只要以分号隔开即使不换行也不影响执行
  6. 编译的过程：编译以后，会生成一个或多个字节码文件，字节码文件与java源文件中的类名相同。

## 关键字&保留字

### 关键字（keyword）

1. 定义：被Java语言赋予特殊含义，用作专门用途的字符（单词）。

2. 特点：关键字中所有字母都为小写。

3. 列表

   ```Java
   abstract, assert,boolean, break, byte, case, catch, char, class, const, continue, default, do, double, else, enum,extends, final, finally, float, for, if, implements, import, instanceof, int, interface, long, native, new, package, private, protected, public, return, short, static, strictfp, super, switch, synchronized, this, throw, throws, transient, try, void, volatile, while
   ```
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222939.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222941.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222942.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222936.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222937.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222940.png)
   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814222938.png)

### 保留字（reserved word）

1. Java保留字：现有的Java版本尚未使用，但以后版本可能会作为关键字使用。自己命名标识符时要避免使用这些保留字。

   ```Java
   byValue, cast, false, future, generic, inner, operator, outer, rest, true, var ， goto ，const,null
   ```


## 标识符（Identifier）

### 标识符

1. Java对各种变量、方法和类等要素命名时使用的字符序列称为标识符。
2. 比如：类名、变量名、方法名、接口名、包名……
3. 技巧：凡是自己可以取名字的地方都叫标识符。

### 定义合法标识符规则（***必须遵守***）

1. 由26个英文字母大小写，0-9，_或$组成；
2. 数字不可开头；
3. 不可以使用关键字和保留字，但可以包含关键字和保留字；
4. Java中严格区分大小写，长度无限制；
5. 标识符不能包含空格。

### Java中名称命名规范（***建议遵守***）

1. 包名：多单词组成时所有字母都小写：xxxyyyzzz；
2. 类名、接口名：多单词组成时，所有单词的首字母大写：XxxYyyZzz ；
3. 变量名、方法名：多单词组成时，第一个单词首字母小写，第二个单词开始每个单词首字母大写：xxxYyyZzz；
4. 常量名：所有字母都大写。多单词时每个单词用下划线连接：XXX_YYY_ZZZ；
5. 注意
   - 注意1：在取名字时，为提高阅读性，要尽量有意义（见名知意）
   - 注意2：Java采用unicode字符集，因此标识符也可以使用汉字声明，但不建议使用

## 变量

### 变量的概念

1. 内存中的一个存储区域；
2. 该区域的数据可在同一类型范围内不断变化；
3. 变量是程序中最基本的存储单元。包含变量类型（强类型：必须先声明）、变量名和存储的值。
   - 定义变量的格式：数据类型 变量名 = 变量值
     - 例：`int demo = 01;`

### 变量的作用

1. 用于在内存中保存数据。

### 变量的使用

1. **Java中每个变量必须先声明，后使用**；
2. 变量都定义在其作用域内。在作用域内，它是有效的。换句话说，出了作用域，就失效了。“一对`{}`”即为一个作用域；
3. 同一个作用域内，不能声明两个同名的变量,**前者会被后者覆盖**。
4. Java定义的数据类型（按数据类型分）：对于每一种数据都定义了明确的具体数据类型（强类型语言），在内存中分配了不同大小的内存空间。

- ***基本数据类型（`primitive type`）***

  (1)数值型

  - 整数类型

    - byte
      - 占用存储空间：1字节 = 8bit位
      - 表数范围：-128~127（27），最高位为符号位（0正1负），故为7次方

    - short
      - 占用存储空间：2字节
      - 表数范围：-215~215-1
    - int
      - 占用存储空间：4字节
      - 表数范围：-231~231-1（约21亿）
    - long
      - 占用存储空间：8字节
      - 表数范围：-263~263-1
    - 注意
      - Java各整数类型有固定的表数范围和字段长度，不受具体OS的影响，以保证Java程序的可移植性
      - Java的整型常量默认为int型，声明long型常量须后加‘l’或‘L’
      - Java程序中变量通常声明为int型，除非不足以表示较大的数，才使用long

  - 浮点类型
    - 单精度float
      - 占用存储空间：4字节
      - 表数范围：-3.403E38~3.403E38
    - 双精度double
      - 占用存储空间：8字节
      - 表数范围：-1.798E308~1.798E308
    - 注意：与整数类型类似，Java浮点类型也有固定的表数范围和字段长度，不受具体操作系统的影响
    - 浮点型常量有两种表示形式
      - 十进制数形式：如：5.12、512.0f、.512 (必须有小数点）
      - 科学计数法形式:如：5.12e2、512E2、100E-2
    - float：单精度，尾数可以精确到7位有效数字。很多情况下，精度很难满足需求
    - double：双精度，精度是float的两倍。通常采用此类型
    - Java的浮点型常量默认为double型，声明float型常量，须后加’f’或’F’
    - float表示的数值范围比long还大，是因为它使用科学计数法来计数，但是精度不够

  (2)字符型

  - char
    - 1字符 = 2字节
    - 声明或定义char型变量，通常使用一对单引号（’’），内部只能写一个字符
    - 转义字符（例如：换行符\n、制表符\t、unicode编号等）
  - string
    - 声明或定义string型变量，通常使用一对双引号（’’""），内部能写多个字符
    - 比如`String data = "Hello Java"`
  - 布尔型
    - boolean
      - 只能取两个值之一：true、false
      - 常用于判断、循环结构
      - boolean类型数据只允许取值true和false，无null
      - 不可以使用0或非 0 的整数替代false和true，这点和C语言不同
      - Java虚拟机中没有任何供boolean值专用的字节码指令，Java语言表达所操作的boolean值，在编译之后都使用Java虚拟机中的int数据类型来代替：true用1表示，false用0表示

- 引用数据类型（reference type）

  - 类（class）
  - 接口（interface）
  - 数组（[]）

### 变量的默认值

1. 整形：0
2. 浮点型：0.0
3. char型：0（NUT）或’\u0000’（ASCII码为0的值）
4. boolean型：false
5. 引用数据类型：null

## 基本数据类型之间的运算规则

### 前提

- 这里只讨论7种基本数据类型变量间的运算，不包含boolean类型的。

### 自动类型提升

1. 容量小的类型自动转换为容量大的数据类型。

![](https://gitee.com/koyangyang/pictures/raw/master/20200814230804.png)

- byte、char、short三种类型变量做运算时，结果为int类型，即这三个变量之间的运算结果至少要拿一个int型去接收。原因：可能是防止溢出，并且整形常量默认类型为int型，运算时如果直接加减数字的话编译不通过

### 强制类型转换

- 自动类型提升的逆运算

1. 需要使用强转符
2. 强制类型转换可能导致精度损失

### 字符串类型：String

1. String属于引用数据类型;
2. 声明String类型变量时，使用一对双引号（””），长度不限（不超过内存空间即可）；
3. 定义String类型变量时，双引号之间可以没有内容，但是char类型不可以；
4. String可以和8中基本数据类型变量作运算，且运算只能是连接运算（+），运算结果仍是String类型；
5. 将String类型转为int型：`int num1 = Integer.parseInt(str1)`，而不能用强制转换，强制转换只能在上述7种数据类型之间。

## 运算符

- 概念：运算符是一种特殊的符号，用以表示数据的运算、赋值和比较等

### 算术运算符

![](https://gitee.com/koyangyang/pictures/raw/master/20200814232105.png)

1. 整形数相除后默认结果为整形
   - 需要精确结果进行运算前需要先进行类型转换（自动转换或者强制类型转换）
2. 取模（余）运算（%）
   - 结果符号与被除（模）数相同
3. 自增（减）
   - （前）++：先自增1，后运算
   - （后）++：先运算，后自增1
   - 自减（略）
   - 注意：自增（减）不会改变变量本身数据类型

### 赋值运算符（=）

1. 当“=”两侧数据类型不一致时，可以使用自动类型转换或使用强制类型转换原则进行处理
2. 支持连续赋值
   - `int i1, j1;`
   - `i1 = j1 = 10;`

### 比较（关系）运算符



![](https://gitee.com/koyangyang/pictures/raw/master/20200814232129.png)

1. 比较运算符的运算结果都是boolean型，也就是要么是true，要么false
2. 区分“=”和“==”

### 逻辑运算符

![](https://gitee.com/koyangyang/pictures/raw/master/20200814232219.png)

1. 区分逻辑与（&）和短路与（&&）
   - 相同点：运算结果相同；党符号左边为true时，都会执行符号右边的内容
   - 不同点：当左边为false时，&&不会执行符号右边的运算（短路）
   - 开发中优先使用短路与（&&）
2. 区分逻辑或（|）和短路或（||）
   - 相同点：运算结果相同；当符号右边为false时，二者都会执行符号右边的内容
   - 不同点：当符号左边为true时，|| 不会执行符号右边的运算（短路）
   - 开发中优先使用短路或（||）
3. 逻辑非（!）
4. 逻辑异或（^）

#### 交换两个变量的值

- 方法一：定义临时变量

  ```Java
  int temp = num1;
  num1 = num2;
  num2 = temp;
  ```

- 方法二

  ```Java
  num1 = num1 + num2;
  num2 = num1 - num2;
  num1 = num1 - num2;
  ```

  - 优点：不用定义临时变量、
  - 弊端：①相加操作可能超出存储范围； ②有局限性：只能适用于数值类型。

- 方法三：使用位运算符

  ```Java
  num1 = num1 ^ num2;
  num2 = num1 ^ num2;
  num1 = num1 ^ num2;
  ```

### 三元运算符

1. 格式：

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200814232405.png)

   - 条件表达式的结果为boolean类型
   - 表达式1和表达式2为**同种类型**
   - 三元运算符可嵌套使用

2. 三元运算符与if-else的联系与区别

   - 三元运算符可简化if-else语句，因此能用三元运算符的地方尽量用三元运算符
   - 三元运算符要求必须返回一个结果
   - if后的代码块可有多个语句
   - 凡是可以使用三元运算符的地方都可以改写成if-else，反之则不一定行

3. 练习：获取3个数中的最大值

```java
int max1 = (a > b)? a : b;
int max2 = (max1 > c)? max1 : c;
```

### 运算符优先级

![](https://gitee.com/koyangyang/pictures/raw/master/20200814232758.png)

![](https://gitee.com/koyangyang/pictures/raw/master/20200814232728.png)







## 流程控制

- 流程控制语句是用来控制程序中各语句执行顺序的语句，可以把语句组合成能完成一定功能的小逻辑模块

### 如何从键盘/控制台获取不同类型的变量：需要使用Scanner类

1. 导包：`import java.util.Scanner;`
2. Scanner的实例化：`Scanner scan = new Scanner(System.in);`
3. 调用Scanner的相关方法，来获取指定类型的变量。
4. 对于char类型的获取，Scanner没有提供相关的方法，只能获取一个字符串。
5. 如果一定要获取char类型，可用charAt(0)获取字符串索引为0位置上的字符。

- 注意：需要根据相应的方法，来输入指定类型的值。如果输入的数据类型与要求的类型不匹配，则出现异常：InputMisMatchException，导致程序中断。容量小的可自动提升；

### 如何获取随机数

1. `double value = Math.random()`：返回一个[0.0, 1.0)之间的double型的值。

- 例：获取[a,b]之间的int型随机数：`(int)(Math.random() * (b - a + 1) + a)`

### 流程控制方式结构化程序设计中规定的三种基本流程结构

1. 顺序结构
   - 程序从上到下逐行执行，中间没有任何判断和跳转
2. 分支结构
   - 根据条件，选择性地执行某段代码
   - 有if-else和switch-case两种分支语句
3. 循环结构
   - 根据循环条件，重复性地执行某段代码
   - 有while、do…while、for三种循环语句
   - 注：JDK1.5提供了foreach循环，方便的遍历集合、数组元素

### 分支语句

#### if-else结构

1. 第一种

   if(条件表达式){

   执行表达式

   }

2. 第二种：二选一

   if(条件表达式){

   执行表达式1

   }else{

   执行表达式2

   }

3. 第三种：多选一

   if(条件表达式1){

   执行表达式1

   }

   if(条件表达式2){

   执行表达式2

   }

   ……

   else{

   执行表达式n

   }

4. 使用说明

   - 条件表达式必须是布尔表达式（关系表达式或逻辑表达式）、布尔变量。
   - 语句块只有一条执行语句时，一对{}可以省略，**但建议保留**
   - if-else语句结构，根据需要可以嵌套使用（一般不超过3层，超过3层未解决则停下来想其他办法）。
   - 当if-else结构是“多选一”时，最后的else是可选的，根据需要可以省略。
   - 当多个条件是“互斥”关系时，条件判断语句及执行语句间顺序无所谓。
   - 当多个条件是“包含”关系时，“小上大下 /子上父下”。
   - if (80 < core <= 99)报错原因：前面的(80 < core)的结果为一个boolean类型，boolean类型不能与int类型做大小关系对比。

5. 针对于条件表达式：

   - 如果多个表达式之间是”互斥“关系（或没有交集的关系），判断和执行语句的上下顺序不影响。

   - 如果多个表达式之间有交集的关系，则需要根据实际情况来决定哪个声明在上面。

   - 如果多个表达式之间有包含关系，通常情况下，需要将范围小的声明在范围大的上面，否则范围小的就没机会执行了。

   - 就近原则

     ```Java
     if (x > 2)
         if(y > 2)
             执行语句1;
     else
         执行语句2;
     //上述语句相当于：
     if (x > 2)
         if(y > 2)
             执行语句1;
         else
             执行语句2;
     //以上误判源于省略了单行执行语句的{}，所以尽量不要省略{}
     ```

#### switch-case结构

![](https://gitee.com/koyangyang/pictures/raw/master/20200815092555.png)

1. 说明：

- 根据switch表达式中的值，依次匹配各个case中的常量。一旦配成功，则进入相应的case结构中，调用其执行语句，当调用完执行语句以后，则仍然继续向下执行其他case结构中的执行语句，直到遇到break关键字或此switch-case结构末尾结束为止。

- break，可以使用在switch-case结构中，表示一旦执行到此关键字，就跳出switch-case结构。

- switch结构中的表达式，只能是如下六种数据类型之一：byte、short、char、int、枚举类型（JDK5.0新增）、String类型（JDK7.0新增）。

- case之后只能声明常量，尤其不能是一个范围。

- break关键字是可选的。

- default：相当于if-else中的else，也是可选的，且default位置是可选的，一般还是写在末尾。

- 如果switch-case结构中多个case的执行语句相同，则可以考虑进行合并，即写完多行执行语句相同的case以后只写1行执行语句。

- 凡是可以使用switch-case的结构，都可以转换为if-else。反之，不成立。

- 写分支结构时，如果既可以使用if-else，又可以使用switch-case（switch中表达式的取值情况不太多），优先选择使用switch-case。原因：switch-case执行效率稍高。

- 示例：输入日期，返回日期是那一年的第几天。

  ```Java
  import java.util.Scanner;
  class CountDays{
      public static void main(String[] args){
          Scanner input = new Scanner(System.in);
          System.out.print("请输入年份：");
          int year = input.nextInt();
          System.out.print("\n请输入月份：");
          int month = input.nextInt();
          System.out.print("\n请输入日期：");
          int day = input.nextInt();
          int days = 0;
          switch (month){
          case 12:
              days += 30;
          case 11:
              days += 31;
          case 10:
              days += 30;
          case 9:
              days += 31;
          case 8:
              days += 31;
          case 7:
              days += 30;
          case 6:
              days += 31;
          case 5:
              days += 30;
          case 4:
              days += 31;
          case 3:
              if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
                  days += 29;
              }else{
                  days += 28;
                  }
          case 2:
              days += 31;
          case 1:
              days += day;
              System.out.println("\n" + year +"年" + month + "月" + day + "号是" + year + "年的第" + days + "天。");
              break;
          default:
              System.out.println("\n输入有误！");
          }
      }
  }
  ```

#### 循环结构

1. 在某些条件满足得情况下，反复执行特定代码的功能

2. 循环语句的四个组成部分

   ①初始化部分（init_statement）

   ②循环条件部分（test_exp）–> boolean类型

   ③循环体部分（body_statement）

   ④迭代部分（alter_statement）

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200815092633.png)

3. 通常情况下，循环结束都是因为②中循环条件返回了false

   - 循环语句分类

     - for循环
     - 结构

   - for(① ; ② ; ④){

      ③

     }

     执行过程：① -> ② -> ③ -> ④ -> ② -> ③ -> ④ -> ② -> …… -> 直到②不再返回true，跳出循环

   - 例题：遍历100以内的偶数，输出所有偶数的和，输出所有偶数的个数。

     ```Java
     class ErgodicEvenNum{
         public static void main(String[] args){
             int count = 0;
             int sum = 0;
             for (int i = 0; i <= 100; i++){
                 if (i % 2 == 0){
                     sum += i;
                     count += 1;                        
                 }
             }
             System.out.println("0-100内偶数有" + count + "个，它们的和为：" + sum);
         }
     }
     //i在for循环内有效，出了for循环就失效了
     ```
     
- 例题：输入两个正整数m和n，求其最大公约数和最小公倍数。比如，12和20的最大公约数是4，最小公倍数是60。
  
  - 说明break的作用
  
  ```Java
     import java.util.Scanner;
     class GetGcdLcm{
         public static void main(String[] args){
             Scanner scan = new Scanner(System.in);
             System.out.print("请输入第一个整数：");
             int m = scan.nextInt();
             System.out.print("\n请输入第二个整数：");
             int n = scan.nextInt();
             int min = (m <= n)? m : n;
             for (int i = min; i > 0; i--){
                 if (m % i == 0 && n % i == 0){
                     System.out.print("\n" + m + "和" + n + "的最大公约数为" + i + "，");
                     break;
                 }
             }
             int max = (m >= n)? m : n;
             for (int i = max; i <= m * n; i++){
                 if (i % m == 0 && i % n == 0){
                     System.out.println("最小公倍数为" + i + "。");
                     break;
                 }
             }
         }
     }
  ```
  
4. while循环

   - 结构

   `①初始化部分`

   `while(②循环条件部分){`

    `③循环体部分;`

    `④迭代部分;`

   `}`

   执行过程：① -> ② -> ③ -> ④ -> ② -> ③ -> ④ -> ② -> …… ->②

   - 说明
     - 注意不要忘记声明④迭代部分。否则，循环将不能结束，变成死循环。
     - for循环和while循环可以相互转换
     - for循环和while循环初始化条件的作用范围不同。
     - i 出了while循环后可以继续使用，原因：①初始化部分在循环外。

5. do-while

   - 结构

     `①`

     `do{`

     `③；`

     `④；`

     `}while(②)；`

     执行过程：① -> ③ -> ④ -> ② -> ③ -> ④ -> ② …… ->②

   - 特点

     - 先执行再判断，至少执行一次循环体。
     - 开发中较少使用do-while，for和while使用较多。

6. 循环语句综合题：从键盘输入个数不确定的整数，并判断读入的正数和负数的个数，输入为0时，结束程序。

   ```Java
   import java.util.Scanner;
   class CirCom{
       public static void main(String[] args){
           Scanner scan = new Scanner(System.in);
           int posNum = 0;
           int negNum = 0;
           while(true){
               int alter = scan.nextInt();
               if (alter > 0){
                   posNum += 1;
               }else if (alter < 0){
                   negNum += 1;
               }else{
                   break;
               }
           }
           System.out.println("输入的正数个数为：" + posNum);
           System.out.println("输入的负数个数为：" + negNum);
       }
   }
   ```
   
- 说明：
     - while(true)就相当于for(;;)
     - 结束循环的几种方式
       - 循环条件部分返回false；
       - 在循环体中执行break。

7. 嵌套循环

- 嵌套循环的使用

  - 嵌套循环：将一个循环结构A声明在另一个循环结构B的循环体中，就构成了嵌套循环。
  - 外层循环：循环结构B。
  - 内层循环：循环结构A。

- 说明

  - 内层循环结构遍历一遍，只相当于外层循环结构循环一次。
  - 假设外层循环需要执行m次，内层循环需要执行n次，此时内存层循环的循环体需要执行m*n次。

- 技巧：外层循环控制行数，内层循环控制列数。

- 例题：九九乘法表

  ```Java
  import java.util.Scanner;
  class MultiTable{
      public static void main(String[] args){
          Scanner scan = new Scanner(System.in);
          System.out.println("要打印几行？（1-9）");
          int line = scan.nextInt();
          for (int i = 1; i <= line; i++){
              for (int j = 1; j <= i; j++){
                  System.out.print(i + "x" + j + "=" + i * j + "  ");
              }
              System.out.println();
          }
      }
  }
  ```
  
- 100以内所有质数
  
```Java
  import java.util.Scanner;
  class PriNum{
      public static void main(String[] args){
          Scanner scan = new Scanner(System.in);
          System.out.println("要打印多少以内的质数？");
          int limtNum = scan.nextInt();
          System.out.println("*********结果*********");
          boolean isPriNum = true;
          for (int i = 2; i <= limtNum; i++){
              for (int j = 2; j < i; j++)        {
                  if (i % j ==0){
                      isPriNum = false;
                  }
              }
              if (isPriNum){
                  System.out.println(i);
              }
              isPriNum = true;
          }
      }
  }
```

  - 优化

  ```Java
import java.util.Scanner;
  class PriNum{
      public static void main(String[] args){
          Scanner scan = new Scanner(System.in);
          System.out.println("要打印多少以内的质数？");
          int limtNum = scan.nextInt();
          System.out.println("*********结果*********");
          long start = System.currentTimeMillis();//获取当前时间距1970-01-01 00:00:00的毫秒数（long型）
          boolean isPriNum = true;
          int count = 0;
          for (int i = 2; i <= limtNum; i++){
              //for (int j = 2; j < i; j++){
              for (int j = 2; j <= Math.sqrt(i); j++){//优化二：一个数如果在2到它本身开方的范围内没有商，则为质数
                  if (i % j ==0){
                      isPriNum = false;
                      break;//优化一：只对本身非质数的自然数是有效的。加break前后对比：20181ms/2174ms = 9.28
                  }
              }
              if (isPriNum){
                  count += 1;
              }
              isPriNum = true;
          }
          long end = System.currentTimeMillis();
          System.out.println("质数的个数：" + count);
          System.out.println("所花费的时间：" + (start - end));
          //优化前：17916ms 优化一：1629ms 优化二：16ms
      }
  }
  ```

#### 特殊关键字的使用

- break

  - 使用范围：switch-case、循环结构中
  - 循环中使用的作用：结束当前循环
  - 默认跳出包裹此关键字最近的一层循环
  - 结束指定标识的一层循环结构

  ```Java
  label:for (int i = 1; i <= 4; i++){
      for (int j = 1; j <= 10; j++){
          if (j % 4 == 0){
              break label;
          }
      }
  }
  ```
  
- continue

  - 使用范围：循环结构中

  - 循环中使用的作用：结束当次循环

  - 结束指定标识的一层循环结构的当次循环

    `countinue label;`

- 相同点：两个关键字后面不能声明执行语句

- return

  - 并非专门用于结束循环的，它的的功能是结束一个方法。当一个方法执行到一个return时，这个方法将被结束。
  - 与break、continue不同的是吗，return直接结束整个方法，不管这个return处于多少层循环之内。

- 补充：衡量一个功能代码的优劣

  - 正确性
  - 可读性
  - 健壮性
  - 高效率与低存储：时间复杂度、空间复杂度（衡量算法的好坏）

## 数组

### 数组的概述

- 数组（Array），是多个相同数据类型按一定顺序排列的集合，并使用一个名字命名，通过编号的方式对这些数据进行统一管理。
- 分为一维数组、二维数组等

### 数组的常见概念

1. 数组名
2. 标（或索引/**下标**）
3. 元素
4. 数组的长度：元素的个数

### 特点

1. 数组是有序排列的；
2. 数组属于引用数据类型，但是数组的元素既可以是基本数据类型，也可以是引用数据类型；
3. 创建数组对象会在内存中开辟一整块连续的空间，而数组名中引用的是这块连续空间的首地址；
4. 数组的长度一旦确定，就不能修改；
5. 可以通过下标（或索引）的方式调用指定位置的元素，速度很快。

### 数组的使用

#### 一维数组

- 声明

  - 声明一维数组`int[] array;`

- 初始化

  - 静态初始化

    > `int ids = new int[]{1001,1002,1003,1004};`

  - 动态初始化

    ```Java
    String[] name = new String[5];
    for (int i=0;i<5 ;i++ ) {
    		System.out.println("input:");
    		name[i]=scan.next();
    }
    ```

    

- 错误写法

  - `int[] arr1 = new int[];`
  - ``int[5] arr2 = new int[5];`
  - `int [] arr3 = new int[3]{1,2,3};`

- 数组长度固定,即**数组一旦确定,长度就不能变化**

- 数组的基本操作

  1. 如何调用数组指定函数指定位置的函数
     - 通过索引（角标）的方式调用，索引（角标）从0开始，直到数组的长度-1结束
  2. 如何获取数组的长度
     - 属性：length
     - 使用：`names.length`
  3. 遍历数组(单层for循环)
     - `for(int i = 0; i < names.length; i++){}`

- 完整代码

  ```Java
  import java.util.Scanner;
  public class Test{
  	public static void main(String[] args) {
  		Scanner scan=new Scanner(System.in);
  		int[] data=new int[]{11,12,13,14,15};//静态初始化一个int类型的data数组
  		String[] name = new String[5];//声明一个string类型的数组
  		for (int i=0;i<5 ;i++ ) {//动态初始化一个string类型数组
  			System.out.println("input:");
  			name[i]=scan.next();
  		}
  		System.out.println("这是一个静态赋值的数组：");
  		for (int i=0;i<5 ;i++ ) {
  			System.out.println(data[i]);
  		}
  		System.out.println("这是一个动态赋值的数组：");
  		for (int i=0;i<5 ;i++ ) {
  			System.out.println(name[i]);
  		}
  	}
  }
  ```

  ![](https://gitee.com/koyangyang/pictures/raw/master/20200815110847.png)



#### 二维数组（多维数组）

1. 理解：对于二维数组的理解，可以看成是**一维数组array1的元素而存在**。从数组底层的运行机制来看，其实没有多维数组。***相当于一个一维数组，其中每个元素都是另一个一维数组***

2. 声明

   ```Java
   int[][] arr1 = new int[][]{{1, 2, 3}, {4, 5}, {6, 7, 8}};//静态初始化
   String[][] arr2 = new String[3][2];//动态初始化1
   String[][] arr3 = new String[3][];//动态初始化2
   ```
   
3. 错误类型

   ```Java
   String[][] arr4 = new String[][4];
   String[4][3] arr5 = new String[][];
   int[][] arr6 = new int[4][3]{{1, 2, 3}, {4, 5}, {6, 7, 8}};
   ```
   

- Tips：中括号（[]）的位置可以放在类名或者变量名后面；或者类名后面放一个，变量名后面放一个（二维数组）。
- 类型推断：`int[][] arr7 = {{1, 2, 3}, {4, 5}, {6, 7, 8}};//省略new int[][]`

4. 数组的基本操作

   1. 如何调用数组指定位置的函数

      - `arry[i][j]; //第i行第j列的元素`

   2. 如何获取数组长度

      - `arr4.length;`
      - `arr4[0].length;`

   3. 遍历数组(双城for循环嵌套)

      ```Java
      for(int i = 0; a <= arr4.length; i++){
          for(int j = 0; j <= arr4[i].length){
              //执行语句
          }
      }
      ```

   4. 初始化

      - 初始化依旧分为`静态`和`动态`

      - 完整代码：

        ```Java
        public class Array2{
        		static int a=1;
        		public static void main(String[] args) {
        			int[][] data1=new int[][]{{1,2,3,4},{5,6,7,8},{9,10,11,12}};//静态初始化一个二维数组
        			int[][] data2=new int[3][3];//静态初始化一个二维数组
        			for (int i=0; i<3; i++) {
        				for (int j=0; j<3; j++) {
        					data2[i][j]=a;
        					a++;
        				}
        			}
        			System.out.println("这是一个静态赋值数组Array[3][4]");
        			for (int i=0; i<3; i++) {
        				for (int j=0; j<4; j++) {
        					System.out.print(data1[i][j]);
        				}
        				System.out.println();
        			}
        			System.out.println("这是一个动态态赋值数组Array[3][3]");
        			for (int i=0; i<3; i++) {
        				for (int j=0; j<3; j++) {
        					System.out.print(data2[i][j]);
        				}
        				System.out.println();
        			}
        			System.out.println("二维数组的长度"+data1.length);//data1[i][j]中的i
        			System.out.println("二维数组第1行长度"+data1[1].length);//data1[i][j]中的j
        	}
        }
        ```
        ![](https://gitee.com/koyangyang/pictures/raw/master/20200815143604.png)



