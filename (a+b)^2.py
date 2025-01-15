from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class MyScene(Scene):
    def construct(self):
        a = 6
        b = a*(np.sqrt(5)-1)/2
        c = 2*a/(np.sqrt(5)+3)
        d = {"fill_opacity": 0.5, "stroke_width": 8}
        a1 = Square(side_length=a, stroke_width=4)
        self.play(GrowFromCenter(a1))
        self.wait()

        a2 = Line([-a/2, -a/2, 0], [a/2-c, -a/2, 0], color="#4DBAE1", stroke_width=8)
        a3 = Line([a/2-c, -a/2, 0], [a/2, -a/2, 0], color=PURPLE, stroke_width=8)
        a4 = Line([-a/2, -a/2, 0], [-a/2, a/2-c, 0], color="#4DBAE1", stroke_width=8)
        a5 = Line([-a/2, a/2-c, 0], [-a/2, a/2, 0], color=PURPLE, stroke_width=8)
        self.play(GrowFromCenter(a2), GrowFromCenter(a3), GrowFromCenter(a4), GrowFromCenter(a5))
        self.wait()

        a6 = Brace(a2, -UP, stroke_width=4)
        a7 = Brace(a3, -UP, stroke_width=4)
        a8 = Brace(a4, LEFT, stroke_width=4)
        a9 = Brace(a5, LEFT, stroke_width=4)
        self.play(
            FadeIn(VGroup(a6, MathTex("a").next_to(a6, -UP).scale(1.5)), shift=2*UP),
            FadeIn(VGroup(a7, MathTex("b").next_to(a7, -UP).scale(1.5)), shift=2*UP),
            FadeIn(VGroup(a8, MathTex("a").next_to(a8, LEFT).scale(1.5)), shift=2*RIGHT),
            FadeIn(VGroup(a9, MathTex("b").next_to(a9, LEFT).scale(1.5)), shift=2*RIGHT)
        )
        self.wait()

        a10 = MathTex("(a+b)^2=", "a^2", "+ab", "+ab", "+b^2").scale(1.5).move_to(-6*UP).set_color_by_gradient(BLUE, PINK)
        self.play(Write(a10[0]))
        self.wait()
        
        a11 = Square(side_length=b, color="#4DBAE1", fill_color="#4DBAE1", **d).move_to([(b-a)/2, (b-a)/2, 0])
        a12 = MathTex("a^2").scale(1.5).move_to(a11.get_center())
        self.play(GrowFromCenter(a11))
        self.play(Write(a12))
        self.wait()

        a13 = Rectangle(width=b, height=c, color=PURPLE, fill_color=PURPLE, **d).move_to([(b-a)/2, (a-c)/2, 0])
        a14 = Rectangle(width=c, height=b, color=PURPLE, fill_color=PURPLE, **d).move_to([(a-c)/2, (b-a)/2, 0])
        a15 = MathTex("ab").scale(1.5).move_to(a13.get_center())
        a16 = MathTex("ab").scale(1.5).move_to(a14.get_center())
        self.play(GrowFromCenter(a13), GrowFromCenter(a14))
        self.play(Write(a15), Write(a16))
        self.wait()

        a17 = Square(side_length=c, color="#DD57C8", fill_color="#DD57C8", **d).move_to([(a-c)/2, (a-c)/2, 0])
        a18 = MathTex("b^2").scale(1.5).move_to(a17.get_center())
        self.play(GrowFromCenter(a17))
        self.play(Write(a18))
        self.wait()
        self.play(
            TransformMatchingShapes(a12, a10[1]),
            ReplacementTransform(a15, a10[2]),
            ReplacementTransform(a16, a10[3]),
            ReplacementTransform(a18, a10[4])
        )
        self.wait()

        a19 = MathTex("(a+b)^2=", "a^2", "+2ab", "+b^2").scale(1.5).move_to(-6*UP).set_color_by_gradient(BLUE, PINK)
        self.play(
            TransformMatchingShapes(a10[0], a19[0]),
            TransformMatchingShapes(a10[1], a19[1]),
            ReplacementTransform(VGroup(a10[2], a10[3]), a19[2]),
            TransformMatchingShapes(a10[4], a19[3])

        )
        self.wait()
        self.play(Circumscribe(a19, color=BLUE))
        self.wait()