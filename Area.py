from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class MyScene(Scene):
    def construct(self):
        a = [-4/3, 8*np.sqrt(2)/3, 0]
        b = [-2*np.sqrt(3), -2, 0]
        c = [+2*np.sqrt(3), -2, 0]
        d = [-4/3, -2, 0]
        e = [np.sqrt(3)-2/3, 4*np.sqrt(2)/3-1, 0]
        f = {"stroke_width": 8}

        a1 = Circle(radius=4, **f)
        a2 = Dot(point=a, **f).set_z_index(2)
        a3 = Dot(point=b, **f).set_z_index(2)
        a4 = Dot(point=c, **f).set_z_index(2)
        self.add(a1, a2, a3, a4)

        a5 = Polygon(a, b, c, color=BLUE_E, fill_opacity=0, **f).set_z_index(1)
        a6 = Dot(**f)
        self.play(Create(a5))
        self.play(FadeIn(a6))

        a7 = DashedLine(a6, a)
        a8 = DashedLine(a6, b)
        a9 = DashedLine(a6, c)
        self.play(Create(VGroup(a7, a8, a9)))

        a10 = Dot(point=d, **f)
        a14 = Dot(point=e, **f)
        self.play(FadeIn(VGroup(a10, a14).set_z_index(2)))

        a11 = Line(a, d)
        a15 = Line(a6, a14)
        self.play(Create(a11), Create(a15))

        a12 = RightAngle(a11, Line(d, b), quadrant=(-1, 1))
        a16 = RightAngle(a15, Line(a14, a2), quadrant=(-1, 1))
        self.play(Create(a12), Create(a16))

        # a17 = Arc(start_angle=0.65, angle=1.22, radius=0.5, arc_center=ORIGIN)
        #self.play(Create(a17))
        
        a20 = MathTex("a").move_to(1.6*RIGHT+1.1*UP).scale(1.3)
        a21 = MathTex("b").move_to(1.1*UP+2.8*LEFT).scale(1.3)
        a22 = MathTex("c").move_to(-2.5*UP).scale(1.3)
        self.play(Create(a20), Create(a21), Create(a22))

        a23 = MathTex("h").next_to(a11, buff=0.25).scale(1.3)
        self.play(Create(a23))

        a24 = MathTex("R").move_to(-1.4*UP-1.4*LEFT).scale(1.3)
        self.play(Create(a24))

        a25 = MathTex("\\frac{a}2").scale(1.3).rotate(0.69).move_to([0.4, 2.5, 0])
        self.play(Write(a25))

        a28 = MathTex("\\sim").scale(2).move_to(8*UP)
        
        a13 = Arc(start_angle=0, angle=1.22, radius=0.5, arc_center=b)
        a17 = Arc(start_angle=0.65, angle=1.22, radius=0.5, arc_center=ORIGIN)
        a26 = MathTex("\\varphi").scale(1.3).move_to([-2.75, -1.5, 0])
        a27 = a26.copy().move_to([0.2, 0.8, 0])
        self.play(FadeIn(VGroup(a13, a17, a26, a27)))

        a18 = Polygon(a, b, d, fill_opacity=0.5, color=BLUE)
        a19 = Polygon(a, ORIGIN, e, fill_opacity=0.5, color=PINK)
        self.play(GrowFromCenter(a18), GrowFromCenter(a19))

        self.play(
            a18.animate.shift(7.25*UP-0.5*LEFT),
            a19.animate.shift(6.5*UP-1.5*LEFT),
            FadeIn(a28)
        )
        
        a29 = MathTex(r"\frac{h}b=\frac{\frac{a}2}R").scale(2).move_to(7*UP)
        self.play(ReplacementTransform(VGroup(a18, a19, a28), a29))

        a30 = MathTex(r"h=\frac{ab}{2R}").scale(2).move_to(7*UP)
        self.play(TransformMatchingShapes(a29, a30))

        a31 = MathTex(r"S=\frac12hc").scale(1.8).move_to(6*UP)
        self.play(a30.animate.shift(1.5*UP).scale(0.8), FadeIn(a31))
        
        a32 = MathTex(r"S=\frac{abc}{4R}").scale(1.8).move_to(6*UP)
        self.play(Transform(VGroup(a31, a30), a32))
        self.play(Circumscribe(a32), FadeOut(a30))
        self.wait()