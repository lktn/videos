import math
from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
class SinApproximation(Scene):
    def construct(self):
        axes = Axes(x_range=[-2*PI, 2*PI], y_range=[-3, 3])
        self.play(Create(axes))

        g = VGroup(
            MathTex(r"\sin(x)"),
            MathTex(r"\sin(x)\approx x"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!}"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!}-\frac{x^{11}}{11!}"),
            MathTex(r"\sin(x)\approx x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!}-\frac{x^{11}}{11!}+\frac{x^{13}}{13!}"),
            MathTex(r"\sin(x)=\sum_{n=0}^{\infty}\frac{(-1)^n\cdot x^{2n+1}}{(2n+1)!}")
        ).scale(1.25).move_to(4.5*UP)

        sin = axes.plot(np.sin, color=RED)
        self.play(Create(sin), Write(g[0]))

        v = VGroup(
            axes.plot(lambda x: x),
            axes.plot(lambda x: x-x**3/6),
            axes.plot(lambda x: x-x**3/6+x**5/120),
            axes.plot(lambda x: x-x**3/6+x**5/120-x**7/5040),
            axes.plot(lambda x: x-x**3/6+x**5/120-x**7/5040+x**9/362880),
            axes.plot(lambda x: x-x**3/6+x**5/120-x**7/5040+x**9/362880-x**11/39916800),
            axes.plot(lambda x: x-x**3/6+x**5/120-x**7/5040+x**9/362880-x**11/39916800+(x**13)/math.factorial(13)),
            axes.plot(np.sin)
        ).set_color(BLUE)
        self.play(Create(v[0]), ReplacementTransform(g[0], g[1]))
        self.wait(0.7)

        for i in range(len(v)-1):
            self.play(ReplacementTransform(v[i], v[i+1]), ReplacementTransform(g[i+1], g[i+2]))
            self.wait(0.7)

        self.play(FadeOut(VGroup(axes, v[7], sin)))
        self.play(g[8].animate.shift(-4.5*UP))
        self.play(Circumscribe(g[8]))
        self.play(FadeOut(g[8]))
