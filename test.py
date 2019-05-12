import numpy as np
import pygame

p = np.array([1,2])



def text_in_center(speaker, text, screen, screen_rect):
    print("Text!")
    fontObj = pygame.font.SysFont('arial', 36)
    textSurfaceObj = fontObj.render(speaker + text,
                                    False, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.left = screen_rect.left + screen_rect.width / 2 - textRectObj.width / 2
    textRectObj.top = screen_rect.top + screen_rect.height / 2 - textRectObj.height / 2
    screen.blit(textSurfaceObj, textRectObj)








pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((960, 1080))
screen_rect = screen.get_rect()
screen_rect = screen.get_rect()
while True:
    text_in_center("Tom ","IOU!", screen, screen_rect)
    pygame.display.flip()








# import random
#
# # coo = []
# # for i in range(8):
# #     x, y = random.randint(1, 10), random.randint(1, 10)
# #     coo.append([x, y])
# #     print(coo)
# #
# # print(coo[4])
# # x, y = coo[4]
# # print(x, y)
#
#
# # class Gun():
# #     def __init__(self):
# #         self.x = 1
# #         self.y = 2
# #
# #     def attck(self):
# #         bullet = Bullet(self.x, self.y)
# #         bullet.print_info()
# #
# # class Bullet():
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def print_info(self):
# #         print(self.x, self.y)
# #
# # gun = Gun()
# # gun.attck()
#
# class A():
#     def __init__(self):
#         self.health = 100
#
#     def print_info(self):
#         print(self.health)
#
# class B():
#     def __init__(self, target):
#         self.atk = 50
#         self.target = target
#
#     def attack(self):
#         self.target.health -= self.atk
#
#     def print_info(self):
#         print(self.atk)
#
# a = A()
# a.print_info()
# b = B(a)
# b.attack()
# a.print_info()
# print(b.target)
# print(a)
#
# # class C(A):
# #     def __init__(self):
# #         self.health = 200
# #
# # class D():
# #     def __init__(self, other):
# #         self.atk = other.atk
# #
# #     def attack(self, target):
# #         target.health -= self.atk
# #         self.atk -= 20
# #
# #
# # c = C()
# # print("C")
# # c.print_info()
# # d = D(b)
# # d.attack(c)
# # print("C")
# # c.print_info()
# # print("b")
# # b.print_info()
#
#
# class A():
#     def __init__(self):
#         self.speed = 1
#
#     def fun(self):
#         self.x_speed = 2
#
# a = A()
# a.fun()
# print(a.x_speed)
# print(a.speed)

# class Parent():
#     def update(self, num1, num2):
#         print((num1 + num2))
#
# class Child(Parent):
#     # def update(self,num1, num2):
#     def update(self,num1, num2):
#         print("I am a child!")
#         # super(Child, self).update(num1, num2)
#         super().update(num1, num2)
#         # super().update()
#         # super(Child, self).update()
#
# c = Child()
# c.update(1, 2)

