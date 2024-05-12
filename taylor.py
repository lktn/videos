import math
from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
class SinApproximation(Scene):
    def construct(self):
        axes = Axes(x_range=[-2*PI, 2*PI], y_range=[-3, 3])
        self.play(Create(axes))

        a = MathTex("\\sin(x)")
        a1 = MathTex("\\sin(x) \\approx x")
        a2 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}")
        a3 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}+\\frac{x^5}{5!}")
        a4 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}")
        a5 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}")
        a6 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}-\\frac{x^{11}}{11!}")
        a7 = MathTex("\\sin(x) \\approx x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}-\\frac{x^{11}}{11!}+\\frac{x^{13}}{13!}")
        a8 = MathTex(r"\sin(x)=\sum_{n=0}^{\infty}\frac{(-1)^n\cdot x^{2n+1}}{(2n+1)!}")
        nhom = VGroup(a, a1, a2, a3, a4, a5, a6, a7, a8).scale(1.25).move_to((4.5)*UP)

        sin = axes.plot(np.sin, color=RED)
        self.play(Create(sin), Write(a))

        taylor1 = axes.plot(lambda x: x, color=BLUE)
        self.play(Create(taylor1), ReplacementTransform(a, a1))
        self.wait(0.7)

        taylor2 = axes.plot(lambda x: x-(x**3)/6, color=BLUE)
        self.play(ReplacementTransform(taylor1, taylor2), ReplacementTransform(a1, a2))
        self.wait(0.7)

        taylor3 = axes.plot(lambda x: x-(x**3)/6+(x**5)/120, color=BLUE)
        self.play(ReplacementTransform(taylor2, taylor3), ReplacementTransform(a2, a3))
        self.wait(0.7)

        taylor4 = axes.plot(lambda x: x-(x**3)/6+(x**5)/120-(x**7)/5040, color=BLUE)
        self.play(ReplacementTransform(taylor3, taylor4), ReplacementTransform(a3, a4))
        self.wait(0.7)

        taylor5 = axes.plot(lambda x: x-(x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880, color=BLUE)
        self.play(ReplacementTransform(taylor4, taylor5), ReplacementTransform(a4, a5))
        self.wait(0.7)

        taylor6 = axes.plot(lambda x: x - (x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880-(x**11)/39916800, color=BLUE)
        self.play(ReplacementTransform(taylor5, taylor6), ReplacementTransform(a5, a6))
        self.wait(0.7)

        taylor7 = axes.plot(lambda x: x - (x**3)/6+(x**5)/120-(x**7)/5040+(x**9)/362880-(x**11)/39916800+(x**13)/math.factorial(13), color=BLUE)
        self.play(ReplacementTransform(taylor6, taylor7), ReplacementTransform(a6, a7))
        self.wait(0.7)

        taylor8 = axes.plot(lambda x: np.sin(x), color=BLUE)
        self.play(ReplacementTransform(taylor7, taylor8), ReplacementTransform(a7, a8))
        self.wait(0.7)
        
        nhom1 = VGroup(axes, taylor8, sin)
        self.play(FadeOut(nhom1))
        self.play(a8.animate.shift(UP*(-4.5)))
        self.play((Circumscribe(a8)))
        self.play(FadeOut(a8))
