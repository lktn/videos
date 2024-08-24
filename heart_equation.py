from manim import *
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class Heart(Scene):
    def construct(self):
        axes = Axes(x_range=(-2.5, 2.5, 1),
                    y_range=(-2, 3, 1),
                    x_length=5,
                    y_length=5).scale(0.7).scale(4).move_to(2*UP)

        m = ValueTracker(0)
        color = "#FF08CB"

        a1 = lambda x: np.cbrt(x**2)+0.9*np.sqrt(3.3-x**2)*np.sin(m.get_value()*PI*x)
        a2 = always_redraw(lambda: axes.plot(a1, x_range=[-np.sqrt(3.3), np.sqrt(3.3), 0.01], color=color))
        a3 = Text("Heart  Equation", font_size=20).scale(4).next_to(axes, DOWN, buff=0.8)
        a4 = MathTex(r"y=x^\dfrac{2}{3}+0.9(3.3-x^2)^\dfrac{1}{2}\cdot \sin(m\pi x)",
                                    font_size=20).scale(4).next_to(a3, DOWN, buff=0.8)
        a5 = Text(r"m=", font_size=26).scale(4).next_to(a4, DOWN*4).shift(LEFT*0.8)
        a6 = always_redraw(lambda:DecimalNumber(number=m.get_value(),
                                                num_decimal_places=2,
                                                show_ellipsis=False,
                                                font_size=26,
                                                color=color).scale(4).next_to(a5, RIGHT, buff=0.2))

        nhom = VGroup(axes, a2, a3, a4, a5, a6)
        self.play(Write(nhom))
        self.play(m.animate(run_time=7).set_value(6.5), rate_func=rate_functions.smooth)
        self.wait(2.5)
        self.play(FadeOut(nhom))
