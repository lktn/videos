from manim import * 
config.pixel_height = 1920
config.pixel_width = 1080
class am(Scene):
    def construct(self):
        triangle1 = Polygon([-2, -3, 0], [2, -3, 0], [-2, -1, 0], color=BLUE, fill_opacity=0.5)

        line1 = Line(start = triangle1.get_vertex_groups()[0][0], end = triangle1.get_vertex_groups()[0][1])
        line2 = Line(start = triangle1.get_vertex_groups()[0][0], end = triangle1.get_vertex_groups()[0][2])
        
        zela_a1 = MathTex("a").next_to(line1, direction=DOWN)
        zela_b1 = MathTex("b").next_to(line2, direction=LEFT)
        
        angle1 = RightAngle(line2, line1, length=0.4, quadrant=(1,1), color=WHITE)
        group1 = VGroup(triangle1, angle1)

        self.play(Create(group1))
        self.play(Write(zela_a1), Write(zela_b1))

        group2 = group1.copy()
        group2[0].color = YELLOW

        self.add(group2)
        self.wait(0.2)
        temp = group2.copy().shift([-4 , 2 , 0])

        self.play(Transform(group2, temp ))
        self.wait(0.5)

        self.play(Rotate(group2, angle = -PI/2, about_point = [-2, -1, 0]))

        line1 = Line(start = group2[0].get_vertex_groups()[0][0], end = group2[0].get_vertex_groups()[0][1])
        line2 = Line(start = group2[0].get_vertex_groups()[0][0], end = group2[0].get_vertex_groups()[0][2])
        
        zela_a2 = MathTex("a").next_to(line1 , direction=LEFT)
        zela_b2 = MathTex("b").next_to(line2 , direction=UP)
        
        self.play(Write(zela_a2), Write(zela_b2))
        
        triangle3 = Polygon([-2, -1, 0], [0, 3, 0], [2, -3, 0], color= RED)
        self.play(Create(triangle3))

        line1 = Line(start = triangle3.get_vertex_groups()[0][0] , end = triangle3.get_vertex_groups()[0][1])
        line2 = Line(start = triangle3.get_vertex_groups()[0][0] , end = triangle3.get_vertex_groups()[0][2])
        
        zela_c1 = MathTex("c").next_to(line1.get_center(), direction=LEFT)
        zela_c2 = MathTex("c").next_to(line2.get_center(), direction=DOWN)
        
        self.play(Write(zela_c1), Write(zela_c2))
        
        angle3 = RightAngle(line1, line2, length=0.4, quadrant=(1, 1))
        
        self.play(Create(angle3))
        self.wait(0.5)

        kole_shekl = VGroup(group1, group2, triangle3, zela_c1, zela_c2, angle3)
        matn1 = MathTex("$\dfrac{1}{2}ab+\dfrac{1}{2}ab+\dfrac{1}{2}cc $", tex_environment = "center").next_to(kole_shekl , UP).shift(UP*3)
        
        self.play(group1[0].animate.set_fill(BLUE, opacity = 0.5))
        self.play(TransformFromCopy(triangle1.copy(), matn1[0][0:5] ))
        self.play(Write(matn1[0][5:6]))
        self.play(group2[0].animate.set_fill(YELLOW, opacity = 0.5))
        self.play(TransformFromCopy(group2[0].copy(), matn1[0][6:11] ))
        self.play(Write(matn1[0][11:12]))
        self.play(triangle3.animate.set_fill(RED, opacity = 0.5))
        self.play(TransformFromCopy(triangle3.copy(), matn1[0][12:16]),)
        
        matn2 = MathTex("$ab + \dfrac{1}{2}c^{2} = $\\\\$ \dfrac{1}{2} \\times (a+b)\\times (a + b)$", tex_environment = "center").next_to(kole_shekl, UP).shift(UP*3)
        
        self.play(TransformMatchingShapes(matn1, matn2[0][0:8] , fade_transform_mismatches=True , path_arc = PI/2))
        hight = Line(start = [-2, -3, 0], end = [-2, 3, 0])
        nhom = VGroup(triangle1, hight)
        f1 = Brace(nhom, LEFT)
        f2 = MathTex("a+b").next_to(f1, LEFT, buff=0.2)
        bracet_text = VGroup(f1, f2)
        
        self.play(Transform(VGroup(zela_b1, zela_a2), bracet_text))
        self.play(Write(matn2[0][9:13]))
        self.play(TransformFromCopy(bracet_text.copy(), matn2[0][13:18]))
        self.play(Write(matn2[0][18:19]))
        self.play(TransformFromCopy(VGroup(zela_b2, zela_a1).copy(), matn2[0][19:24]))
        self.play(Write(matn2[0][8:9]))
        
        matn3 = MathTex("$\dfrac{1}{2}(a+b)^2=ab+\dfrac{1}{2}c^{2}$", tex_environment = "center").next_to(kole_shekl, UP).shift(UP*3)
        self.play(TransformMatchingShapes(matn2, matn3))
        
        matn4 = MathTex("$\dfrac{1}{2}(a^2+b^2)+ab=ab+\dfrac{1}{2}c^2 $", tex_environment = "center").next_to(kole_shekl, UP).shift(UP*3)
        self.play(TransformMatchingShapes(matn3, matn4))

        matn5 = MathTex("$\dfrac{1}{2}(a^2+b^2)=\dfrac{1}{2}c^2 $", tex_environment = "center" ).next_to(kole_shekl, UP).shift(UP*3)
        self.play(TransformMatchingShapes(matn4, matn5))
        
        matn6 = MathTex("$a^2+b^2=c^2$", tex_environment = "center" ).next_to(kole_shekl, UP).shift(UP*3)
        self.play(TransformMatchingShapes(matn5, matn6))
        self.play((Circumscribe(matn6)))
        self.wait(1)
