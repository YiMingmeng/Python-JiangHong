import turtle
def draw_polygon(sides, side_len): #绘制指定边长度的多边行
    for i in range(sides):
        turtle.forward(side_len)   #绘制边长
        turtle.left(360.0/sides)   #旋转角度
def main():
    turtle.color("red")     #设置绘制时画笔的颜色
    turtle.pensize(3)       #定义绘制时画笔的线条宽度
    turtle.speed(1)         #定义绘图的速度 
    turtle.goto(0,0)        #移动海龟到坐标原点(0,0)
    step = 50               #边长（海龟步长）为50
    draw_polygon(3, step)  #绘制红色的三边形

    #画笔移动到点(100,0)绘制正方形
    turtle.up()           #移动时不绘图
    turtle.goto(100,0)    #定位到(100,0)
    turtle.color("green") #再次定义画笔颜色
    #绘制绿色的正方形
    turtle.down()
    draw_polygon(4, step)

    #画笔移动到点(200,0)绘制正五边形
    turtle.up()           #移动时不绘图
    turtle.goto(200,0)    #定位到(200,0)
    turtle.color("blue")  #再次定义画笔颜色
    #绘制绿色的正方形
    turtle.down()
    draw_polygon(5, step)

   
    #画笔移动到点(-200,0)时不绘图
    turtle.up()                  #移动时不绘图
    turtle.goto(-200,0)
    turtle.color("black")        #再次定义画笔颜色
    turtle.write("绘制完成！",font=('Arial', 20, 'normal'))   #在(-200,0)点上打印"绘制完成！"

if __name__ == '__main__': main()
