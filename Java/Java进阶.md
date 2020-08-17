## **面向对象(进阶内容)**

- **面向对象三大特性：** **封装、继承、多态**

- 将问题转化为类和类的对象来解决

- **类的组成（成员）：** **属性、方法(函数)、构造器(构造函数)；代码块、内部类**

- **关键字：** 

- 
  | 关键字    | 意义                                      |
  | --------- | ----------------------------------------- |
  | this      | this表示成员变量                          |
  | super     | super表示父类的引用                       |
  | final     | final（最终）修饰引用、方法、类无法被修改 |
  | extends   | 继承，比如class A extends class B         |
  | interface | 接口是一种特殊的抽象类，用于多继承        |
  | abstract  | 抽象类只用声明不用实现，用于单继承        |

## 面向过程与面向对象区别

1. 面向过程：具体到每一个步骤，强调的是功能行为，以函数为最小单位，考虑怎么做。
2. 面向对象：具体到每一个功能将功能封装进对象，强调具备了功能的对象，以类/对象为最小单位，考虑谁来做。

## 面对对象的三大特征

1. 封装（Encapsulation）
2. 继承（Inheritance）
3. 多态（Polymorphism）

### 面向对象的三大特征说明

1. 继承性

   继承是一种联结类的层次模型，并且允许和鼓励类的重用，它提供了一种明确表述共性的方法。对象的一个新类可以从现有的类中派生，这个过程称为类继承。新类继承了原始类的特性，新类称为原始类的派生类（子类），而原始类称为新类的基类（父类）。派生类可以从它的基类那里继承方法和实例变量，并且类可以修改或增加新的方法使之更适合特殊的需要。

2. 封装性

   封装是把过程和数据包围起来，对数据的访问只能通过已定义的界面。面向对象计算始于这个基本概念，即现实世界可以被描绘成一系列完全自治、封装的对象，这些对象通过一个受保护的接口访问其他对象。

3. 多态性

   多态性是指允许不同类的对象对同一消息作出响应。多态性包括参数化多态性和包含多态性。多态性语言具有灵活、抽象、行为共享、代码共享的优势，很好的解决了应用程序函数同名问题。

4. 抽象性(补充)

   抽象就是忽略一个主题中与当前目标无关的那些方面，以便更充分地注意与当前目标有关的方面。抽象并不打算了解全部问题，而只是选择其中的一部分，暂时不用部分细节。抽象包括两个方面，一是过程抽象，二是数据抽象。

## 面对对象的思想概述

1. 程序员从面向过程的执行者转化成了面向对象的指挥者。
2. 面对对象分析问题的思路和步骤：
   - 根据问题需要，选择问题所针对的现实世界中的实体。
   - 从实体中寻找解决问题相关的属性和功能，这些属性和功能就形成了概念世界中的类。
   - 把抽象的实体用计算机语言进行描述，形成计算机世界中类的定义。即借助某种程序语言，把类构造成计算机能够识别和处理的数据结构。
   - 将类实例化成计算机世界中的对象，对象是计算机世界中解决问题的最终工具。
3. 将功能和结构封装到类中，再通过类的实例化来调用具体的功能和结构

## Java基本元素：类和对象

### 面对对象的思想概述

1. 类（Class）和对象（Object）是面向对象的核心概念。
   - 类是对一类事物的描述，是抽象的、概念上的定义
   - 对象是实际存在的该类事物的每个个体，因而也称为实例（instance）
2. 万物皆对象
   - 面对对象程序设计的重点是类的设计
   - 类的设计，其实就是类的成员的设计

### Java类及类的成员

1. 现实世界的生物体，大到鲸鱼，小到蚂蚁，都是由最基本的细胞构成的。同理，Java代码世界是由诸多不同功能的类构成的。
2. 现实生物世界中的细胞又是由什么构成的呢？细胞核、细胞质……那么，Java中用类来描述事物也是如此。常见类的成员有：
   - 属性：对应类中的成员变量
   - 行为：对应类中的成员方法

> Field = 属性 = 成员变量 = 域、字段，Method = （成员）方法 = 函数
>
> 创建类的对象 = 类的实例化 = 实例化类

### 类的成员之一：属性

#### 属性（成员变量）与局部变量区别

1. 相同点

   - 定义变量的格式：数据类型 变量名 = 变量值
   - 先声明，后使用
   - 变量都有其对应的作用域

2. 不同点

   - 在类中声明的位置不同：

     - 属性：直接定义在类的一对{}内
     - 局部变量：声明在方法内、方法形参、构造器形参、构造器内部的变量

   - 关于权限修饰符

     - 属性：可以在声明属性时，指明其权限，使用权限修饰符，常用的权限修饰符有：private(私有的)、public(公共的)、friendly(默认、缺省的)、protected(受保护的)。

       ![](https://gitee.com/koyangyang/pictures/raw/master/20200816221815.png)

     - 局部变量：不可以使用权限修饰符。

   - 默认初始化值的情况

     - 属性：类的属性，根据其类型，都有默认初始化值。
       - 整形（byte、short、int、long）：0
       - 浮点型（float、double）：0.0
       - 字符型（char）：0（或’\u0000’）
       - 布尔型（boolean）：false
       - 引用数据类型（类、数组、接口）：null
     - 局部变量：没有默认初始化值，意味着在调用局部变量之前一定要显示赋值。
       - 特别地：形参在调用时，我们赋值即可，例如下列代码实例的User方法中的String language。

   - 在内存中加载的位置

     - 属性：加载到堆空间中（非static）
     - 局部变量：加载到栈空间

   - 变量的分类二：按照在类中声明的位置

     ![](https://gitee.com/koyangyang/pictures/raw/master/20200816222001.png)

     ```Java
     public class UserTest {
         public static void main(String[] args) {
             User u1 = new User();//类的实例化
             System.out.println(u1.name);
             System.out.println(u1.age);
             System.out.println(u1.isMale);
             u1.talk("日语");//特别的
             u1.eat();
         }
     }
     
     class User{
         //属性（或成员变量）
         String name="张三";
         int age=18;
         boolean isMale=true;
         
         public void talk(String language) {//形参，也是局部变量
             System.out.println("我们使用" + language +"进行交流。");
         }
         
         public void eat() {
             String food = "烙饼";//局部变量
             System.out.println("北方人喜欢吃" + food);
         }
     }
     ```

     ![](https://gitee.com/koyangyang/pictures/raw/master/20200816223548.png)
     
### 类和对象的实例化

将类进行实例化，每一个实例就叫做对象。比如`Car car=new Car()`,则car就是Car类的一个对象。

```Java
public class ClassCar{
	public static void main(String[] args) {
		System.out.println("====================");
		Bike bike=new Bike();
		/*调用方法：对象.方法*/
		bike.pass();
		/*调用属性：对象.属性*/
		bike.name="普通自行车";
		bike.pass();
		bike.brand("28大杠");
		System.out.println("====================");
		Car car=new Car();
		car.pass();
		/*调用属性：对象.属性*/
		car.name="法拉利";
		car.pass();
		car.brand("布加迪威龙");
		System.out.println("====================");
		Car car1=car;//将car变量保存的地址赋给car1，导致car1和car指向了堆空间中的同一个对象实体。
		car1.pass();
		/*调用属性：对象.属性*/
		car1.name="法拉利";
		car1.pass();
		car1.brand("布加迪威龙");
	}
}
class Bike{
	Bike(){
		System.out.println("这是bike类的无参构造函数");
	}
	String name="28大杠";
	void pass(){
		System.out.println(name+"跑得慢");
	}
	void brand(String Name){
		System.out.println("品牌是："+Name);
	}
}
class Car{
	Car(){
		System.out.println("这是car类的无参构造函数");
	}
	String name="布加迪威龙";
	void pass(){
		System.out.println(name+"跑的快");
	}
	void brand(String Name){
		System.out.println("品牌是："+Name);
	}
}
```

### 匿名对象

没有变量名的对象叫做匿名对象，匿名对象只能使用一次

```Java
public class InstanceTest {
    public static void main(String[] args) {
        Phone p = new Phone();
        
        System.out.println("正常调用：");
        p.sendEmail();
        p.playGame();
        
        //匿名
        System.out.println("\n匿名对象：");
        new Phone().sendEmail();
        new Phone().playGame();
        
        System.out.println("\n匿名对象只能代用一次：");
        new Phone().price = 1999;
        new Phone().showPrice();
        
        System.out.println("\n匿名对象的使用：");
        PhoneMall mall = new PhoneMall();
//        mall.show(p);
        mall.show(new Phone());
    }
}

class PhoneMall{
    public void show(Phone phone) {
        phone.sendEmail();
        phone.playGame();
    }
}

class Phone{
    double price;//价格
    
    public void sendEmail() {
        System.out.println("发送邮件");
    }
    
    public void playGame() {
        System.out.println("玩游戏");
    }
    
    public void showPrice() {
        System.out.println("手机的价格为：" + price);
    }
}
```



![](https://gitee.com/koyangyang/pictures/raw/master/20200816164238.png)

### 类的成员之一：方法

#### 类中方法的声明和使用

1. 举例（后面的代码实例中）：

   - public void eat(){}（void：没有返回值）
   - public void sleep(int hour){}
   - public String getNmae() {}（String：返回一个String类型的数据）
   - public String getNation(String nation){}

2. 方法的声明：权限修饰符 返回值类型 方法名(形参列表){

    方法体

    }

   - 注意：static、final、abstract来修饰的方法以后再讲。

3. 说明：

   - 关于权限修饰符：目前默认方法的权限修饰符先都使用public。

   - Java规定的4种权限修饰符：private、public、缺省、protected —> 封装性再细说.

   - 返回值类型：有返回值or无返回值

     - 如果方法有返回值，则必须在方法声明时，指定返回值的类型。同时，方法中必须使用return关键字来返回指定类型的变量或常量。例如下列代码实例方法中的getName()方法。

     - 如果方法没有返回值，则方法声明时，使用void来表示。通常，没有返回值的方法中，就不使用return。但是，如果使用的话，只能“return;”，表示结束此方法。

     - 我们定义方法该不该有返回值？

       ①题目要求

       ②凭经验：具体问题具体分析

   - 方法名：属于标识符，遵循表示符的规则和命名规范，“见名知意”。

   - 形参列表：方法可以声明0个，1个或多个形参。

     - 格式：数据类型1 形参1,数据类型2 形参2,…

     - 我们定义方法时要不要形参？

       ① 题目要求

       ② 凭经验，具体问题具体分析

   - 方法体：方法功能的体现。

4. return关键字的使用：

   - 使用范围：使用在方法体中。
   - 作用：①结束方法；②针对于有返回值的方法，使用“return 数据;”方法返回所要的数据。
   - 注意：return关键字后面不可以声明执行语句。

5. 方法的使用中可以调用当前类的属性或方法

   - 特别地：方法A中调用方法A：递归方法。
   - 方法中不能再定义方法。

6. 各种方法详解

   ```Java
   public class CustomarTest {
       public static void main(String[] args) {
           Customar customar=new Customar();
           customar.eat();
           customar.sleep(12);
           System.out.println(customar.getNmae());
           System.out.println(customar.getNation("China"));
       }
   }
   
   //客户类
   class Customar{
       //属性:
       String name;
       int age;
       boolean isMale;
       
       //方法：
       public void eat(){//无参无返回值方法
           System.out.println("客户吃饭");
       }
       
       public void sleep(int hour) {//有参无返回值方法
           System.out.println("休息了" + hour + "小时");
       }
       
       public String getNmae() {//无参有返回值方法
           if(age > 18) {
               return name;
           }else {//没有else则报错，必须要有一个返回值。
               return "Tom";
           }
       }
       
       public String getNation(String nation) {//有参有返回值方法
           String info = "我的国籍是：" + nation;
           return info;
       }
   }
   ```

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200816224547.png)

#### 方法重载

1. 定义
   - 在同一个类中，允许存在一个以上的同名方法，只要它们的参数个数或者参数类型不同即可。
     - “两同一不同”：同一个类、相同的方法名；参数列表不同：参数个数不同、参数类型不同。
2. 特点

- 与返回值类型无关，只看参数列表，且参数列表必须不同。（参数个数或参数类型）。调用时，根据方法参数列表的不同来区别。

```Java
public class OverLoadEx1 {
    public static void main(String[] args) {
        OverLoadEx1 m = new OverLoadEx1();
        m.mOL(2);
        m.mOL(2, 5);
        m.mOL("字符串");
    }
    
    public void mOL(int i) {
        System.out.println(i * i);
    }
    
    public void mOL(int i,int j) {
        System.out.println(i * j);
    }
    
    public void mOL(String s) {
        System.out.println(s);
    }
}
```

![](https://gitee.com/koyangyang/pictures/raw/master/20200816231735.png)

#### 方法参数的值传递机制

##### 变量的值传递机制

1. 关于变量的赋值：

   如果是基本数据类型，此时赋值的是变量所保存的数据值；

   如果变量是引用数据类型，此时，赋值的是变量所保存的数据的地址值。

2. 示例

   ```Java
   public class ValueTransfer {
       public static void main(String[] args) {
           System.out.println("******基本数据类型的值传递情况******");
           int m = 10;
           int n = m;
           System.out.println("m = " + m + ", n = " + n);
           n = 20;
           System.out.println("m = " + m + ", n = " + n);
           
           System.out.println("******引用数据类型的值传递情况******");
           Order o1 = new Order();
           o1.orderID = 1001;
           Order o2 = o1;//赋值以后，o1和o2的地址值相同，都指向了堆空间中同一个对象实体。
           System.out.println("o1.orderID = " + o1.orderID + ", o2.orderID = " + o2.orderID);
           o2.orderID = 1002;
           System.out.println("o1.orderID = " + o1.orderID + ", o2.orderID = " + o2.orderID);
       }
   }
   
   class Order{
       int orderID;
   }
   ```

   - 运行结果

     ![](https://gitee.com/koyangyang/pictures/raw/master/20200816232303.png)

##### 方法的形参传递机制：值传递

1. 形参：方法定义时，声明的小括号内的参数。

   实参：调用方法时实际传递给形参的数据。

2. 值传递机制：

   如果参数是**基本数据类型**，此时实参赋给形参的是实参真实存储的**数据值**;

   如果参数是**引用数据类型**，此时实参赋给形参的是实参存储数据的**地址值**。

3. 示例

   ```Java
   public class ValueTransfer01 {
       public static void main(String[] args) {
           int m = 10;
           int n = 20;
           System.out.println("m = " + m + ", n = " + n);
           //交换两个变量值的操作
   //        int temp = m;
   //        m = n;
   //        n = temp;
           ValueTransfer01 test = new ValueTransfer01();
           test.swap(m, n);//未能交换
           System.out.println("m = " + m + ", n = " + n);
       }
       
       
       public void swap(int m,int n) {
           int temp = m;
           m = n;
           n = temp;
       }
   }
   ```

   - 执行结果

     ![](https://gitee.com/koyangyang/pictures/raw/master/20200816232408.png)

#### 递归（recursion）方法

1. 递归方法：一个方法体内调用自身。

2. 方法递归包含了一种隐式的循环，它会重复执行某段代码，但这种重复执行无需循环控制。递归一定要向已知方向递归，否则这种递归就变成了无穷递归，类似于死循环。

3. 代码演示

   ```Java
   public class RecursionIns {
       public static void main(String[] args) {
           //计算1-100内所有数的和
           //方式一
           int sum1 = 0;
           for(int i = 1;i <= 100;i++) {
               sum1 += i;
           }
           System.out.println("方式一：" + sum1);
           
           //方式二（递归）：
           RecursionIns test = new RecursionIns();
           int sum2 = test.getSum(100);
           System.out.println("方式二：" + sum2);
           
           //计算阶乘
           int n = 5;
           int fac = test.getFac(n);
           System.out.println(n + "的阶乘为：" + fac);
       }
   
       //计算1-100内所有数的和的方法
       public int getSum(int n) {
           if(n == 1) {
               return n;
           }else {
               return n + getSum(n - 1);
           }
       }
       
       //计算1-n之间的乘积：n!
       public int getFac(int n) {
           if(n == 1) {
               return n;
           }else {
               return n * getFac(n - 1);
           }
       }
   }
   ```

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200816232633.png)

#### OOP特征一：封装与隐藏

- OOP，即Object oriented programming，面向对象编程。

##### 引入

1. 为什么需要封装？封装的作用和含义？
   - 我要用洗衣机，只需要按一下开关和洗涤模式就可以了。有必要了解洗衣机内部结构吗？有必要碰电动机吗?
   - 我要开车……
2. 我们程序设计追求“高内聚，低耦合”。
   - 高内聚：类的内部操作细节自己完成，不允许外部干涉；
   - 低耦合：仅对外暴露少量的方法用于使用。
3. 隐藏对象内部的复杂性，只对外公开简单的接口。便于外界调用，从而提高系统的可扩展性、可维护性。通俗的说，把该隐藏的隐藏起来，该暴露的暴露出来。这就是封装性的设计思想。

##### 信息的封装和隐藏

- 当我们创建一个类的对象以后，我们可以通过“对象.属性”的方式，对对象的属性进行赋值。这里，赋值的操作要受属性的数据类型和存储范围的制约。除此之外，没有其他制约条件。但是，在实际问题中，我们需要给属性赋值加入额外的条件。这个条件就不能再属性声明时体现，我们只能通过方法进行限制条件的添加。（比如，示例中的setLegs()方法）同时，我们需要避免用户再使用“对象.属性”的方式对属性进行赋值。则需要将属性声明为私有的（private）。

  –> 此时，针对属性就体现了封装性。

1. 封装性的体现：我们讲类的属性xxx私有化（private），同时，提供公共的（public）方法来获取（getXxx）和设置（setXxx）此属性的值。

2. 拓展：封装性的体现

   ①如上 ②不对外暴露的私有的方法 ③单例模式 …

##### 例子

```Java
public class PrivateTest{
	public static void main(String[] args) {
		City name=new City();
		// System.out.println(name.city);
		// System.out.println(name.date);
		System.out.println(name.getcity());
		System.out.println(name.getdate());
	}
}
class City{
	private String city="北京";//无法被对象引用
	private int date=20200817;//无法被对象引用
	public String getcity(){
		return city;
	}
	public int getdate(){
		return date;
	}
}
```

![](https://gitee.com/koyangyang/pictures/raw/master/20200817111316.png)

![](https://gitee.com/koyangyang/pictures/raw/master/20200817111518.png)

##### 四种访问权限修饰符

- 封装性的体现，需要权限修饰符来配合

1. Java规定的种权限（从小到大排列）：`private`、`缺省(默认default)`、`protected`、`public`

2. Java的权限修饰符public、protected、private置于类的成员定义前，用来限定对象对该类成员的访问权限。

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200817111651.png)

3. 4种权限修饰符可以用来修饰类及类的内部结构：属性、方法、构造器、内部类。

4. 具体的，4种权限都可以用来修饰类的内部结构：属性、方法、构造器、内部类；修饰类只能用default（缺省）、public。

### 类的成员之三：构造器（或构造方法）

#### 构造器的作用

1. 创建对象

2. 初始化对象的信息

3. 实例

   ```Java
   public class Gouzaoqi{
   	public static void main(String[] args) {
   		City city1=new City();
   		City city2=new City("北京");
   		City city3=new City("上海",20200827);
   	}
   }
   
   class City{
   	City(){
   		System.out.println("这是一个无参的构造方法的执行结果");
   		System.out.println();
   	}
   	City(String name){
   		System.out.println("这是一个有参的构造方法的执行结果");
   		System.out.println("城市名字"+name);
   		System.out.println();
   	}
   	City(String name,long date){
   		System.out.println("这是一个有两个参的构造方法的执行结果");
   		System.out.println("城市名字"+name+"时间是"+date);
   		System.out.println();
   	}
   }
   ```

   ![](https://gitee.com/koyangyang/pictures/raw/master/20200817144947.png)

#### 说明

1. 如果没有显式的定义类的构造器的话，则系统默认提供一个空参的构造器。
2. 定义构造器的格式：权限修饰符 类名(形参列表){}。
3. 一个类中定义多个构造器，彼此构成重载。
4. 一旦我们显式定义了构造器之后，系统就不再提供默认的空参构造器。
5. 一个类中，至少会有一个构造器。

#### 赋值的先后顺序
- 默认初始化
- 显式初始化
- 构造器中初始化
- 通过"对象.方法"的方式赋值

## 继承

### super和this的含义

- **super** ：代表父类的**存储空间标识**（可以理解为父类的引用）。
- **this** ：代表**当前对象的引用**（谁调用就代表谁）。

### super和this的用法

this.成员变量 -- 本类的
super.成员变量 -- 父类的

this.成员方法名() -- 本类的
super.成员方法名() -- 父类的

### 使用

```Java
public class Classextends{
	public static void main(String[] args) {
		Fu fu=new Fu();
		Zi zi=new Zi();
		fu.show();
		zi.show();
		zi.showname();
	}
}
class Fu{
	String name="哈哈";
	void show(){
		System.out.println("这是父类的show()函数");
	}
}
class Zi extends Fu{
	String name="嘿嘿";
    /*对父类的show函数的重写*/
	void show(){
		System.out.println("这是子类的show()函数");
	}
	void showname(){
		System.out.println(this.name);//调用子类的name
		System.out.println(super.name);//调用父类的name
	}
}
```

![](https://gitee.com/koyangyang/pictures/raw/master/20200817151026.png)

> 注意：
>
> 1. 通过super引用属性、方法、构造器时，都要求该成员是可见的，即该成员的修饰符不能是private的，跨包的话还不能是缺省的。
>
> 2. super的追溯不仅限于直接父类
>
> 3. 如果某个属性或方法前面使用“this.”，那么先从本类中查找，如果未找到，会沿着继承关系往上找
>
>    如果某个属性或方法前面使用“super.”，那么先从直接父类中查找，如果未找到，会沿着继承关系往上找
>
>    如果某个属性或方法前面既没有“this.”，也没有“super.”，遵循就近原则，先从本类中查找，如果未找到，会沿着继承关系往上找

> ### 方法重写注意事项
>
> 1. 方法名：必须完全一致
>
> 2. 形参列表：必须完全一致
>
> 3. 返回值类型：
>
>    如果是基本数据类型和void，必须一致
>
>    如果是引用数据类型，重写的方法的返回值类型 **<=** 被重写方法的返回值类型，Student<Person
>
> 4. 修饰符：重写的方法的修饰符范围 **>=** 被重写方法的修饰符范围（public > protected > 缺省 > private）
>
> 5. 被重写方法不能被 `private`、`static`、`final` 修饰，如果跨包的话，修饰符缺省的也不能被重写，因为缺省的跨包不可见

### 构建函数的继承

```Java
class Father{
    public Father(){
        System.out.println("父类的无参构造");
    }
}

class Son extends Father{
    private String str;
    private int num;

    public Son(){
        //隐含调用了super();  子类的构造器中一定会调用父类的构造器，默认调用父类的无参构造
        System.out.println("子类的无参构造");
    }

    public Son(String str){
        //隐含调用了super()父类构建函数
        this.str = str;
        System.out.println("子类的有参构造1");
    }

    public Son(String str,int num){
        //调用重载的构造器，隐含调用了super()
        this(str);//调用本类中的Son(String str)这个构建函数
        this.num = num;
        System.out.println("子类的有参构造2");
    }
}

public class ConstructorTest {
    public static void main(String[] args) {
        Son s1 = new Son();
        Son s3 = new Son("java", 10);
    }
}
```



![](https://gitee.com/koyangyang/pictures/raw/master/20200817152303.png)

> # 继承后的特点——构造方法
>
> 首先我们要回忆两个事情，构造方法的定义格式和作用：
>
> 1. 构造方法的名字是与类名一致的。所以子类是无法继承父类构造方法的。
> 2. 构造方法的作用是初始化成员变量的。所以子类的初始化过程中，必须先执行父类的初始化动作。
>    - 子类不会继承父类的构造器，但是一定会调用父类的构造器
>    - 默认情况下，调用的是父类的无参构造，super()写或不写都会调用父类的无参构造，如果要写，必须在子类构造器首行
>    - 如果父类没有无参构造，必须在子类的构造器首行使用super(实参列表)显式调用父类的有参构造，否则编译报错
>    - super([形参列表]) 和 this([形参列表]) 都必须是在构造方法的第一行，所以不能同时出现。