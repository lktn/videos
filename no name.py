from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
class Scene(Scene):
    def construct(self):
        t = 1+np.sqrt(5)
        a = [+t, -2, 0]
        b = [-t, -2, 0]
        c = [-t, +2, 0]
        d = [(-4-t)/5, (2*t-2)/5, 0]
        a1 = Polygon(a, b, c, color=BLUE, fill_opacity=0, stroke_width=6)
        self.play(Create(a1))

        a2 = MathTex("a").next_to(a1, -UP, buff=0.3).scale(1.5)
        a3 = MathTex("b").next_to(a1, LEFT, buff=0.3).scale(1.5)
        a4 = MathTex("c").next_to(a1, UP, buff=-1.5).scale(1.5)
        self.play(Write(VGroup(a2, a3, a4)), Write(RightAngle(Line(b, c), Line(b, a), quadrant=(1, 1))))

        a5 = Line(b, d, color=BLUE, stroke_width=6)
        self.play(Create(a5))
        a6 = MathTex("h").next_to(a5, 1.1*UP+LEFT, buff=-1.5).scale(1.5)
        self.play(Write(a6), Write(RightAngle(a5, Line(a, d), quadrant=(-1, -1))))

        a7 = MathTex("hc=ab").move_to(-4*UP).scale(1.5)
        self.play(Write(a7))

        a8 = MathTex("c=", "\\frac{ab}{h}").move_to(-4*UP).scale(1.5)
        self.play(TransformMatchingShapes(a7, a8))

        a9 = MathTex("a^2+b^2=", "c", "^2")
        a10 = MathTex("a^2+b^2=", r"\left(\frac{ab}{h}\right)", "^2")
        a11 = MathTex("a^2", "+", "b^2", "=", "\\frac{a^2b^2}{h^2}")
        a12 = MathTex("\\frac{a^2}{a^2b^2}", "+", "\\frac{b^2}{a^2b^2}", "=", "\\frac{1}{h^2}")
        a13 = MathTex("\\frac{1}{b^2}", "+", "\\frac{1}{a^2}", "=", "\\frac{1}{h^2}")
        a14 = MathTex(r"\frac{1}{a^2}+\frac{1}{b^2}=\frac{1}{h^2}")
        V = VGroup(a9, a10, a11, a12, a13, a14).move_to(5*UP).scale(1.5)
        self.play(Write(a9))
        self.play(
            ReplacementTransform(a9[0], a10[0]),
            TransformFromCopy(a8[1], a10[1]),
            ReplacementTransform(a9[2], a10[2]),
            FadeOut(a9[1])
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(a10[0], VGroup(a11[0], a11[1], a11[2], a11[3])),
            ReplacementTransform(VGroup(a10[1], a10[2]), a11[4]), FadeOut(a8)
        )
        self.wait(0.5)
        self.play(ReplacementTransform(a11[i], a12[i]) for i in range(len(a11)))
        self.wait(0.5)
        self.play(ReplacementTransform(a12[i], a13[i]) for i in range(len(a12)))
        self.wait(0.5)
        self.play(TransformMatchingShapes(a13, a14))
        self.play(Circumscribe(a14))
        self.wait()