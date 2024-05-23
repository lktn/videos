from manim import *
config.pixel_height = 2880
config.pixel_width = 1620
class TanGraph(Scene):
    def construct(self):
        axes = Axes(x_range=[-2*PI, 2*PI, 1], y_range=[-4, 4, 1], x_length=4*PI, y_length=8)
        self.play(Create(axes))

        sin = MathTex(r"y=\sin(x)")
        cos = MathTex(r"y=\cos(x)")
        tan = MathTex(r"y=\tan(x)")
        csc = MathTex(r"y=\csc(x)")
        sec = MathTex(r"y=\sec(x)")
        cot = MathTex(r"y=\cot(x)")
        arcsin = MathTex(r"y=\arcsin(x)")
        arccos = MathTex(r"y=\arccos(x)")
        arctan = MathTex(r"y=\arctan(x)")
        arccsc = MathTex(r"y=\text{arccsc}(x)")
        arcsec = MathTex(r"y=\text{arcsec}(x)")
        arccot = MathTex(r"y=\text{arccot}(x)")

        a = VGroup(sin, cos, tan, csc, sec, cot, arcsin, arccos, arctan, arccsc, arcsec, arccot).move_to(UP*5.5).scale(1.1)

        f1 = axes.plot(np.sin, color=PINK)
        self.play(Create(f1), Write(sin))
        self.wait(1)

        f2 = axes.plot(np.cos, color=PINK)
        self.play(ReplacementTransform(f1, f2), ReplacementTransform(sin, cos))
        self.wait(1)

        f3 = VGroup(
            axes.plot(lambda x: np.tan(x), x_range=[-5*PI/2 + 0.08, -3*PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: np.tan(x), x_range=[-3*PI/2 + 0.08,   -PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: np.tan(x), x_range=[  -PI/2 + 0.08,    PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: np.tan(x), x_range=[   PI/2 + 0.08,  3*PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: np.tan(x), x_range=[ 3*PI/2 + 0.08,  5*PI/2 - 0.08], color=PINK)
        )

        self.play(ReplacementTransform(f2, f3), ReplacementTransform(cos, tan))
        self.wait(1)

        f4 = VGroup(
            axes.plot(lambda x: 1/np.sin(x), x_range=[-3*PI + 0.08, -2*PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.sin(x), x_range=[-2*PI + 0.08,   -PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.sin(x), x_range=[  -PI + 0.08,       - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.sin(x), x_range=[        0.08,    PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.sin(x), x_range=[   PI + 0.08,  2*PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.sin(x), x_range=[ 2*PI + 0.08,  3*PI - 0.08], color=PINK)
        )
        self.play(ReplacementTransform(f3, f4), ReplacementTransform(tan, csc))
        self.wait(1)

        f5 = VGroup(
            axes.plot(lambda x: 1/np.cos(x), x_range=[-5*PI/2 + 0.08, -7*PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.cos(x), x_range=[-5*PI/2 + 0.08, -3*PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.cos(x), x_range=[-3*PI/2 + 0.08,   -PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.cos(x), x_range=[  -PI/2 + 0.08,    PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.cos(x), x_range=[   PI/2 + 0.08,  3*PI/2 - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.cos(x), x_range=[ 3*PI/2 + 0.08,  5*PI/2 - 0.08], color=PINK)
        )
        self.play(ReplacementTransform(f4, f5), ReplacementTransform(csc, sec))
        self.wait(1)

        f6 = VGroup(
            axes.plot(lambda x: 1/np.tan(x), x_range=[-3*PI + 0.08, -2*PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.tan(x), x_range=[-2*PI + 0.08,   -PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.tan(x), x_range=[  -PI + 0.08,       - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.tan(x), x_range=[        0.08,    PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.tan(x), x_range=[   PI + 0.08,  2*PI - 0.08], color=PINK),
            axes.plot(lambda x: 1/np.tan(x), x_range=[ 2*PI + 0.08,  3*PI - 0.08], color=PINK)
        )

        self.play(ReplacementTransform(f5, f6), ReplacementTransform(sec, cot))
        self.wait(1)

        f7 = VGroup(axes.plot(lambda x: np.arcsin(x), x_range=[-0.99, 0.99], color=PINK))
        self.play(ReplacementTransform(f6, f7), ReplacementTransform(cot, arcsin))
        self.wait(1)

        f8 = VGroup(axes.plot(lambda x: np.arccos(x), x_range=[-0.99, 1], color=PINK))
        self.play(ReplacementTransform(f7, f8), ReplacementTransform(arcsin, arccos))
        self.wait(1)

        f9 = VGroup(axes.plot(lambda x: np.arctan(x), x_range=[-8, 8], color=PINK))
        self.play(ReplacementTransform(f8, f9), ReplacementTransform(arccos, arctan))
        self.wait(1)

        f10 = VGroup(
            axes.plot(lambda x: np.arcsin(1/x), x_range=[-8, -1.01], color=PINK),
            axes.plot(lambda x: np.arcsin(1/x), x_range=[1.01, 8], color=PINK))
        self.play(ReplacementTransform(f9, f10), ReplacementTransform(arctan, arccsc))
        self.wait(1)

        f11 = VGroup(
            axes.plot(lambda x: np.arccos(1/x), x_range=[-8, -1.01], color=PINK),
            axes.plot(lambda x: np.arccos(1/x), x_range=[1.001, 8], color=PINK))
        self.play(ReplacementTransform(f10, f11), ReplacementTransform(arccsc, arcsec))
        self.wait(1)

        f12 = VGroup(
            axes.plot(lambda x: np.pi/2 - np.arctan(x), x_range=[-8, 8], color=PINK),
            axes.plot(lambda x: np.pi/2 - np.arctan(x), x_range=[-8, 8], color=PINK))
        self.play(ReplacementTransform(f11, f12), ReplacementTransform(arcsec, arccot))
        self.wait(2)
        self.play(FadeOut(f12), FadeOut(arccot), FadeOut(axes))
