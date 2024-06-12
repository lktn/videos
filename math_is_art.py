from manim import *

config.pixel_height = 1920
config.pixel_width = 1080

class a(Scene):
    def construct(self):
        c = ValueTracker(-3)
        c1 = NumberPlane(x_range=[-8, 8, 1], y_range=[-13, 13, 1])
        
        c2 = always_redraw(lambda: ImplicitFunction(
            lambda x, y: np.sin(2*y) - 2*np.sin(x) - y - y*c.get_value(),
            y_range=[-13, 13],
            x_range=[-8, 8],
            stroke_width=10,
            color=BLUE))

        c3 = always_redraw(lambda: DecimalNumber(
            number=c.get_value(),
            num_decimal_places=1,
            include_sign=True,
            show_ellipsis=False,
            font_size=26,
            stroke_width=3).move_to(RIGHT*3.7 + UP*9).scale(3.1))

        c4 = MathTex(r"\sin(2y)-2\sin(x)-y=\ \ \ \ \ \ \times \ y", stroke_width=3).move_to(UP*9).scale(1.7)

        self.play(Create(c1))
        self.play(Create(c2), Write(c3), Write(c4))
        self.play(c.animate(run_time=7).set_value(3), rate_func=rate_functions.smooth)
        self.play(c.animate(run_time=7).set_value(-3), rate_func=rate_functions.smooth)
        self.wait()

        m = ValueTracker(-PI)
        
        a2 = always_redraw(lambda: ImplicitFunction(
            lambda x, y: np.sin(x) + np.sin(y) - 2 * np.cos(m.get_value()),
            y_range=[-13, 13],
            x_range=[-8, 8],
            stroke_width=10,
            color="#961CCE"))

        a3 = always_redraw(lambda: DecimalNumber(
            number=m.get_value(),
            num_decimal_places=1,
            include_sign=True,
            show_ellipsis=False,
            font_size=26,
            stroke_width=3).move_to(RIGHT*4.1 + UP*9).scale(3.1))

        a4 = MathTex(r"\sin(x)+\sin(y)=2\cos(\ \ \ \ \ \ )", stroke_width=3).move_to(UP*9).scale(1.7)

        self.play(ReplacementTransform(c2, a2), ReplacementTransform(c3, a3), ReplacementTransform(c4, a4))
        self.play(m.animate(run_time=7).set_value(PI), rate_func=rate_functions.smooth)
        self.wait()

        b1 = MathTex(r"\tan(x^2+y^2)=0", stroke_width=3).move_to(UP*9).scale(1.7).set_z_index(2)
        b2 = Circle(radius=PI**0.5, stroke_width=5, color=ORANGE)

        x = VGroup(a3, a4)
        b = VGroup(b2)
        for a in range(1, 34):
            b3 = Circle(radius=(2*a*PI)**0.5, stroke_width=5, color=ORANGE)
            b4 = Circle(radius=(2*a*PI + PI)**0.5, stroke_width=5, color=ORANGE)
            b.add(b3, b4)

        self.play(ReplacementTransform(a2, b), ReplacementTransform(x, b1))
        self.wait()
        self.play(FadeOut(b))

        c = MathTex(r"\sin(x^2+y^2)=\cos(xy)", stroke_width=3).move_to(UP*9).scale(1.7).set_z_index(2)
        d = VGroup().set_z_index(1)
        for n in range(1, 49):
            a = Ellipse(width=2*((4*n-3)*PI/3)**0.5, height=2*(PI*(4*n-3))**0.5, color=RED).rotate(PI/4)
            b = Ellipse(width=2*((4*n-3)*PI/3)**0.5, height=2*(PI*(4*n-3))**0.5, color=RED).rotate(-PI/4)
            d.add(a, b)
        
        self.play(Create(d), ReplacementTransform(b1, c))
        self.wait()