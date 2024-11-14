from manim import *
x = 22
config.pixel_height = 4800
config.pixel_width = 2700
config.frame_height = x
config.frame_width = 9*x/16

class RiemannExplicit(Scene):
    def construct(self):
        a = "#8031D5"
        b = {"color": a, "fill_color": a, "fill_opacity": 1}

        f1 = Rectangle(width=4,   height=8/3, **b).move_to(UP*2/3)
        f3 = Rectangle(width=8/3, height=4/3, **b).move_to([2/3, -4/3, 0])
        a5 = Square(side_length=4/3, **b).move_to([-4/3, -4/3, 0])
        a1 = VGroup(f1, a5, f3)
        self.play(GrowFromCenter(a1))

        a2 = Brace(a1, UP, stroke_width=2)
        a3 = MathTex("a").next_to(a2, UP, buff=0.4).scale(1.5)
        a4 = MathTex("a^2", "-b^2", "=", "(a-b)", "(a+b)").move_to(-4*UP).scale(1.5)
        self.play(FadeIn(VGroup(a2, a3), shift=-2*UP))
        self.play(Write(a4[0]))
        self.play(FadeOut(a5))

        a6 = Brace(a5, LEFT, stroke_width=2)
        a7 = MathTex("b").next_to(a6, LEFT, buff=0.4).scale(1.5)
        self.play(FadeIn(VGroup(a6, a7), shift=-2*LEFT))
        self.play(Write(a4[1]))

        a8 = Brace(f1, LEFT, stroke_width=2)
        a9 = MathTex("a-b").next_to(a8, LEFT, buff=0.6).scale(1.5)
        self.play(Transform(VGroup(a6, a7), VGroup(a8, a9)))
        self.play(Rotate(f3, angle=PI/2, about_point=[2, -2/3, 0]))
        self.play(f3.animate.shift(UP*8/3))

        a10 = Brace(f3, UP, stroke_width=2)
        a11 = MathTex("b").next_to(a10, UP, buff=0.4).scale(1.5)
        self.play(Write(VGroup(a10, a11)))

        a12 = Brace(VGroup(f1, f3), UP, stroke_width=2)
        a13 = MathTex("a+b").next_to(a12, UP, buff=0.4).scale(1.5)
        self.play(
            Transform(VGroup(a2, a10), a12),
            TransformMatchingShapes(VGroup(a3, a11), a13)
        )
        self.wait()
        self.play(Write(a4[2]), TransformFromCopy(a9, a4[3]), TransformFromCopy(a13, a4[4]))
        self.play(Circumscribe(a4))
        self.wait(1)
