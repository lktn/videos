from manim import *
config.pixel_height = 1920
config.pixel_width = 1080

class Heron(Scene):
    def construct(self):
        a = 1.1*np.array([-1-np.sqrt(5),-2, 0])
        b = 1.1*np.array([-3+np.sqrt(5), 2, 0])
        c = 1.1*np.array([ 1+np.sqrt(5),-2, 0])
        a1 = Polygon(a, b, c, stroke_width=6)
        self.play(GrowFromCenter(a1))
        self.wait()

        a2 = MathTex("a").scale(1.3).move_to([0, -2.6, 0])
        a3 = MathTex("b").scale(1.3).move_to([1.8, 0.3, 0])
        a4 = MathTex("C").scale(1.2).move_to([4, -2.55, 0])
        a5 = VGroup(Dot(a),
            MathTex("A").scale(1.2).move_to([-0.85, 2.75, 0]),
            MathTex("c").scale(1.3).move_to([-2.5, 0.3, 0]), Dot(b),
            MathTex("B").scale(1.2).move_to([-4, -2.55, 0]),
            a2, Dot(c), a4, a3
        )
        self.play(Write(a5))
        self.wait()

        a6 = MathTex("Area=", "\\frac{ab}2", "\\sin(C)").scale(1.2).move_to(6*DOWN)
        a7 = a1.copy()
        self.play(a7.animate.set_fill(BLUE, opacity=0.5))
        self.play(ReplacementTransform(a7, a6[0]))
        self.play(Write(VGroup(a6[1], a6[2])))
        self.wait()

        a8 = MathTex("Area=\\frac{ab}2", r"\sqrt{1-\cos^2(C)}").scale(1.2).move_to(6*DOWN)
        self.play(VGroup(a6[0], a6[1]).animate.move_to(a8[0].get_center()), ReplacementTransform(a6[2], a8[1]))
        self.wait()

        a9 = MathTex("Area=\\frac{ab}2", r"\sqrt{1-\left(\frac{a^2+b^2-c^2}{2ab}\right)^2}").scale(1.2).move_to(6*DOWN)
        self.play(VGroup(a6[0], a6[1]).animate.move_to(a9[0].get_center()), ReplacementTransform(a8[1], a9[1]))
        self.wait()

        a10 = MathTex("Area=\\frac{ab}2", r"\sqrt{1-\frac{(a^2+b^2-c^2)^2}{(2ab)^2}}").scale(1.2).move_to(6*DOWN)
        self.play(VGroup(a6[0], a6[1]).animate.move_to(a10[0].get_center()), TransformMatchingShapes(a9[1], a10[1]))
        self.wait()

        a11 = MathTex("Area=\\frac{ab}2", r"\sqrt\frac{(2ab)^2-(a^2+b^2-c^2)^2}{(2ab)^2}").scale(1.2).move_to(6*DOWN)
        self.play(VGroup(a6[0], a6[1]).animate.move_to(a11[0].get_center()), TransformMatchingShapes(a10[1], a11[1]))
        self.wait()

        a12 = MathTex("Area=", "\\frac{ab}2", r"\cdot\frac{\sqrt{(2ab)^2-(a^2+b^2-c^2)^2}}{2ab}").scale(1.2).move_to(6*DOWN)
        self.play(VGroup(a6[0], a6[1]).animate.move_to(VGroup(a12[0], a12[1]).get_center()), ReplacementTransform(a11[1], a12[2]))
        self.wait()

        a13 = MathTex("Area=", r"\frac{\sqrt{(2ab)^2-(a^2+b^2-c^2)^2}}4").scale(1.2).move_to(6*DOWN)
        self.play(a6[0].animate.move_to(a13[0].get_center()), TransformMatchingShapes(VGroup(a6[1], a12[2]), a13[1]))
        self.wait()

        a14 = MathTex("Area=", r"\frac{\sqrt{(2ab-a^2-b^2+c^2)(2ab+a^2+b^2-c^2)}}4").scale(1.05).move_to(6*DOWN)
        self.play(a6[0].animate.scale(7/8).move_to(a14[0].get_center()), TransformMatchingShapes(a13[1], a14[1]))
        self.wait()

        a15 = MathTex("Area=", r"\frac{\sqrt{(c^2-(a-b)^2)((a+b)^2-c^2)}}4").scale(1.2).move_to(6*DOWN)
        self.play(a6[0].animate.scale(8/7).move_to(a15[0].get_center()), TransformMatchingShapes(a14[1], a15[1]))
        self.wait()

        a16 = MathTex("Area=", r"\frac{\sqrt{(c-a+b)(c+a-b)(a+b-c)(a+b+c)}}4").scale(1.05).move_to(6*DOWN)
        self.play(a6[0].animate.scale(7/8).move_to(a16[0].get_center()), TransformMatchingShapes(a15[1], a16[1]))
        self.wait()

        a17 = MathTex("Area=", r"\sqrt{\frac{c-a+b}2\cdot\frac{c+a-b}2\cdot\frac{a+b-c}2\cdot\frac{a+b+c}2}").scale(1.05).move_to(6*DOWN)
        self.play(a6[0].animate.move_to(a17[0].get_center()), TransformMatchingShapes(a16[1], a17[1]))
        self.wait()

        a18 = MathTex(r"p=\frac{a+b+c}{2}").scale(1.2).move_to(8*DOWN)
        self.play(Write(a18))
        self.wait()

        a19 = MathTex("Area=", "\\sqrt{(p-a)(p-b)(p-c)", "p}").scale(1.2).move_to(6*DOWN)
        self.play(a6[0].animate.scale(8/7).move_to(a19[0].get_center()), TransformMatchingShapes(a17[1], VGroup(a19[1], a19[2])))
        self.wait()

        a20 = MathTex("Area=", "\\sqrt{p(p-a)(p-b)(p-c)}").scale(1.2).move_to(6*DOWN)
        self.play(TransformMatchingShapes(a19[1], a20[1]), FadeOut(a19[2]))
        self.wait()
        self.play(Circumscribe(a20, color=GREEN, stroke_width=5))
        self.wait()
        self.play(FadeOut(VGroup(a20, a6[0], a18, a1, a2, a3, a4, a5)))
