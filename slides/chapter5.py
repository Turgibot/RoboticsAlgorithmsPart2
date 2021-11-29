from OPU import *
from manim_slide import MyBullets



class Chap5_00(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"In the last unit we learn about forward kinematics.")
        bullets+= Text(r"We calculated the configuration of the EE for a given set of joint positions.")
        bullets+= Text(r"Today: We would learn how to calculate the twist of an EE from a given set of joint positions and velocities.")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=False).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist, img)
        self.wait()




class Chap5_01(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Motivation", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

          #include video
        cap = cv2.VideoCapture("../media/videos/kukaweld.mp4")

        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.6).shift(DOWN*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

       
        self.wait()


class Chap5_02(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Motivation", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

          #include video
        cap = cv2.VideoCapture("../media/videos/kukapaint.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.6).shift(DOWN*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

       
        self.wait()


class Chap5_03(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Introduction", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        txt1= Tex(r"Before we talk about twist, let $x \in \mathbb{R}^m$ be the EE minimal set of coordinates.").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"Then, its velocity is $\dot{x} = \frac{dx}{dt}\in \mathbb{R}^m$.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"So the FK can be written as $x(t) = f(\theta(t))$.").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Where $\theta \in \mathbb{R}^n$ is a set of n joint variables.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"By the chain rule the time derivative at time t is $\dot{x} = \frac{\partial{f(\theta)}}{\partial{\theta}}\frac{d\theta}{dt} = \frac{\partial{f(\theta)}}{\partial{\theta}}\dot{\theta}=J(\theta)\dot{\theta} $").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"Where $J(\theta)\in\mathbb{R}^{m\times n}$ is called the Jacobian.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        txt7= Tex(r"The Jacobian matrix represents the linear sensitivity of the EE velocity $\dot{x}$ to the joint velocity $\dot{\theta}$, and it is a function of the joint variables $\theta$.").scale(0.5).next_to(txt6, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5, txt6, txt7)
        self.wait()




class Chap5_04(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
 
        txt1= Tex(r"In this section we derive the relationship between an open chain’s joint velocity vector $\theta$ and the EE’s spatial twist $V_s$.").scale(0.5).shift(UP*1.2)
       

        self.add(title, secondary_title, img)
        self.wait()




class Chap5_05(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
 
        txt1= Tex(r"Errata**", color=RED).scale(0.5).shift(LEFT*4)
        arrow = Arrow(start=[-4, 0, 0], end=[-1, -1.9, 0], color=RED)

        self.add(title, secondary_title, img, txt1, arrow)
        self.wait()




class Chap5_06(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
        img1 = ImageMobject('../images/derive_err.png').scale(0.8).shift(DOWN*4.4)
 
        txt1= Tex(r"Errata**", color=RED).scale(0.5).shift(LEFT*4)
        arrow = Arrow(start=[-4, 0, 0], end=[-1, -1.9, 0], color=RED)

        self.add(title, secondary_title, img1, img,txt1, arrow)
        self.play(FadeOut(txt1, arrow, img), img1.animate().move_to([0,-0.2,0]).scale(1.4), secondary_title.animate().shift(RIGHT*4.5), run_time=1)
        self.wait()




class Chap5_07(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/derive_err.png').scale(0.8).shift(DOWN*4.4).move_to([0,-0.2,0]).scale(1.4)
        v = Tex(r"$V_s = J_{s1}\dot{\theta_1}+J_{s2}(\theta)\dot{\theta_2}+...+J_{sn}(\theta)\dot{\theta_n}$", color=GREEN).scale(0.5).shift(UP*1.07).add_background_linkangle(opacity=1)
        self.add(title, secondary_title, img1)
        self.play(FadeIn(v))
        self.wait()


class Chap5_08(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/jacob1.png').scale(1.2).shift(UP)
        img2 = ImageMobject('../images/jacob2.png').scale(1.2).next_to(img1, DOWN)
        self.add(title, secondary_title, img1, img2)
        self.wait()


class Chap5_09(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        self.add(moving_arm,base)
        
        self.wait()

class Chap5_10(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        self.add(moving_arm,base)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        self.play(Rotate(l4,30*DEGREES,about_point=joint4.get_center()),rate_func=linear)
        self.wait()


class Chap5_11(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint3.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint3.get_center()),
                                rate_func=linear)

        self.wait()



class Chap5_12(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        l4.rotate(30*DEGREES,about_point=joint3.get_center())
        l3.rotate(30*DEGREES,about_point=joint3.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint2.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint2.get_center()),
                                Rotate(l2,30*DEGREES,about_point=joint2.get_center()),
                                        rate_func=linear)       

        self.wait()



class Chap5_13(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        l4.rotate(30*DEGREES,about_point=joint3.get_center())
        l4.rotate(30*DEGREES,about_point=joint2.get_center())
        l3.rotate(30*DEGREES,about_point=joint3.get_center())
        l3.rotate(30*DEGREES,about_point=joint2.get_center())
        l2.rotate(30*DEGREES,about_point=joint2.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint1.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint1.get_center()),
                                Rotate(l2,30*DEGREES,about_point=joint1.get_center()),
                                        Rotate(l1,30*DEGREES,about_point=joint1.get_center()),
                                                rate_func=linear)       

        self.wait()

def get_robot():
    link1 = Rectangle(BLUE, 0.75,3)
    joint1 = Circle(0.5).next_to(link1, LEFT).shift(RIGHT*0.5)
    in_joint1= Circle(0.05, color=BLUE).move_to(joint1.get_center())
    link2 = Rectangle(BLUE, 0.75,3).move_to(link1.get_right()+RIGHT*2)
    joint2 = Circle(0.5).next_to(link2, LEFT).shift(RIGHT*0.5)
    in_joint2= Circle(0.05, color=BLUE).move_to(joint2.get_center())
    link3 = Rectangle(BLUE, 0.75,3).move_to(link2.get_right()+RIGHT*2)
    joint3 = Circle(0.5).next_to(link3, LEFT).shift(RIGHT*0.5)
    in_joint3= Circle(0.05, color=BLUE).move_to(joint3.get_center())
    link4 = Rectangle(BLUE, 0.75,3).move_to(link3.get_right()+RIGHT*2)
    joint4 = Circle(0.5).next_to(link4, LEFT).shift(RIGHT*0.5)
    in_joint4= Circle(0.05, color=BLUE).move_to(joint4.get_center())
    base = Rectangle(BLUE, 0.75,0.75).next_to(joint1, DOWN).shift(UP*0.5)
    return joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base


class Chap5_14(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
       

        self.add(title, secondary_title, img, txt1)
        self.wait()


class Chap5_15(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
       
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        self.add(title, secondary_title, img, txt1, img1, mask)
        self.wait()



class Chap5_16(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js1.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*0.3)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()




class Chap5_17(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js2.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*0.85)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()

class Chap5_18(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js3.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*2.2)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()


class Chap5_19(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js4.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*2.2)
        self.add(title, secondary_title, img, txt1, img1, img2)
        self.wait()



class Chap5_20(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        # img2 = ImageMobject('../images/js11.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        # mask.shift(RIGHT*2.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask)
        self.wait()





class Chap5_21(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js11.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*0.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()





class Chap5_22(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js12.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*1.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()






class Chap5_23(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js12.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/rot.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*1.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()





class Chap5_24(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js13.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()




class Chap5_25(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()




class Chap5_26(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js15.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*3)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()

class Chap5_27(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js16.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*4.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()


class Chap5_28(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js17.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*4.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, img2, img3)
        self.wait()


