from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class B(Scene):
    def construct(self):
        a = [-np.sqrt(5)-1,-2, 0]
        b = [np.sqrt(5)-3, +2, 0]
        c = [1+np.sqrt(5), -2, 0]
        d = [np.sqrt(5)-3, -2, 0]
        a1 = Polygon(a, b, c)
        self.play(GrowFromCenter(a1))

        a2 = Line(b, d, color=BLUE)
        a3 = RightAngle(a2, Line(d, c), quadrant=(-1, 1))
        self.play(Create(a2), Create(a3))
        
        a4 = Angle(Line(a, b), a2, quadrant=(-1, 1), radius=0.6)
        a5 = Angle(a2, Line(b, c), quadrant=(1, 1), radius=0.8)
        a6 = MathTex("\\alpha").move_to([-1.05, 1, 0]).scale(1.2)
        a7 = MathTex("\\beta").move_to(0.4*LEFT+UP*0.9).scale(1.2)
        a8 = MathTex("a").move_to(2.3*LEFT+UP*0.3).scale(1.2)
        a9 = MathTex("b").move_to([1.5, 0.3, 0]).scale(1.2)
        a10 = MathTex("h").move_to(LEFT*0.4).scale(1.2)
        a11 = MathTex("x").move_to([-2, -2.4, 0]).scale(1.2)
        a12 = MathTex("y").move_to([np.sqrt(5)-1, -2.4, 0]).scale(1.2)
        self.play(Write(VGroup(a4, a5, a6, a7, a8, a9, a10, a11, a12)))

        a13 = MathTex("Area=", "\\frac12", "h", "(", "x", "+", "y", ")", "=", "\\frac{1}{2}", "a", "b", "\\sin(", "\\alpha", "+", "\\beta", ")")
        a13.move_to(-5*UP).scale(1.2)
        a14 = a1.copy()
        self.play(a14.animate.set_fill(RED, opacity = 0.5))
        self.play(ReplacementTransform(a14, a13[0]))
        self.play(Write(VGroup(a13[1], a13[3], a13[5], a13[7])))
        self.play(TransformFromCopy(a10, a13[2]), TransformFromCopy(a11, a13[4]), TransformFromCopy(a12, a13[6]))
        self.play(Write(VGroup(a13[8], a13[9], a13[12], a13[14], a13[16])))
        self.play(TransformFromCopy(a8, a13[10]), TransformFromCopy(a9, a13[11]), TransformFromCopy(a6, a13[13]), TransformFromCopy(a7, a13[15]))
        self.play(
            FadeOut(a13[0], run_time=0.5), 
            VGroup(a13[1], a13[2], a13[3], a13[4], a13[5], a13[6], a13[7], a13[8], a13[9], a13[10], a13[11], a13[12], a13[13], a13[14], a13[15], a13[16]).animate.move_to(-5*UP)
        )
        a15 = MathTex("h(x+y)", "=", r"ab\sin(\alpha+\beta)").move_to(-5*UP).scale(1.2)
        self.play(
            FadeOut(a13[1]), FadeOut(a13[9]),
            TransformMatchingShapes(VGroup(a13[2], a13[3], a13[4], a13[5], a13[6], a13[7]), a15[0]),
            TransformMatchingShapes(a13[8], a15[1]),
            TransformMatchingShapes(VGroup(a13[10], a13[11], a13[12], a13[13], a13[14], a13[15], a13[16]), a15[2])
        )
        a16 = MathTex(r"\frac{h(x+y)}{ab}=\sin(\alpha+\beta)").move_to(-5*UP).scale(1.2)
        self.play(TransformMatchingShapes(a15, a16))

        a17 = MathTex(r"\sin(\alpha+\beta)=\frac{h(x+y)}{ab}").move_to(-5*UP).scale(1.2)
        self.play(TransformMatchingShapes(a16, a17))

        a18 = MathTex(r"\sin(\alpha+\beta)=\frac{xh+yh}{ab}").move_to(-5*UP).scale(1.2)
        self.play(TransformMatchingShapes(a17, a18))

        a19 = MathTex(r"\sin(\alpha+\beta)=", r"\frac{x}{a}", r"\cdot", r"\frac{h}{b}+\frac{y}{b}\cdot\frac{h}{a}").move_to(-5*UP).scale(1.2)
        self.play(TransformMatchingShapes(a18, a19))

        a20 = MathTex(r"\sin(\alpha+\beta)=", r"\sin(\alpha)", r"\frac{h}{b}", r"+\frac{y}{b}\cdot\frac{h}{a}").move_to(-5*UP).scale(1.15)
        self.play(
            TransformMatchingShapes(a19[0], a20[0]),
            ReplacementTransform(a19[1], a20[1]),
            TransformMatchingShapes(a19[3], VGroup(a20[2], a20[3])),
            FadeOut(a19[2])
        )
        a21 = MathTex(r"\sin(\alpha+\beta)=", r"\sin(\alpha)", r"\cos(\beta)", r"+", r"\frac{y}{b}", r"\cdot\frac{h}{a}").move_to(-5*UP).scale(1.1)
        self.play(
            ReplacementTransform(a20[0], a21[0]),
            ReplacementTransform(a20[1], a21[1]),
            ReplacementTransform(a20[2], a21[2]),
            TransformMatchingShapes(a20[3], VGroup(a21[3], a21[4], a21[5]))
        )
        a22 = MathTex(r"\sin(\alpha+\beta)=", r"\sin(\alpha)", r"\cos(\beta)", "+", r"\sin(\beta)", r"\cdot", r"\frac{h}{a}").move_to(-5*UP).scale(1.08)
        self.play(
            ReplacementTransform(a21[0], a22[0]),
            ReplacementTransform(a21[1], a22[1]),
            ReplacementTransform(a21[2], a22[2]),
            ReplacementTransform(a21[3], a22[3]),
            ReplacementTransform(a21[4], a22[4]),
            TransformMatchingShapes(a21[5], VGroup(a22[5], a22[6]))
        )
        a23 = MathTex(r"\sin(\alpha+\beta)=", r"\sin(\alpha)", r"\cos(\beta)", "+", r"\sin(\beta)", r"\cos(\alpha)").move_to(-5*UP).scale(1.05)
        self.play(
            ReplacementTransform(a22[0], a23[0]),
            ReplacementTransform(a22[1], a23[1]),
            ReplacementTransform(a22[2], a23[2]),
            ReplacementTransform(a22[3], a23[3]),
            ReplacementTransform(a22[4], a23[4]),
            FadeOut(a22[5]),
            ReplacementTransform(a22[6], a23[5])
        )
        self.play(Circumscribe(a23))