from manim import *
import math
config.pixel_height = 1920*2
config.pixel_width = 1080*2
class MyScene(Scene):
    def construct(self):
        axes = Axes(x_range=[-2*PI, 2*PI, 1], y_range=[-3, 3, 1])
            
        v = [axes.plot(lambda x: np.sin(x), color=RED)]
        for n in range(1, 8):
            v.append(axes.plot(lambda x: sum(((-1)**i*x**(2*i+1))/math.factorial(2*i+1) for i in range(n)), color=BLUE))
        v.append(axes.plot(lambda x: np.sin(x), color=BLUE))

        g = VGroup(
            MathTex(r"\sin(x)"),
            MathTex(r"\sin(x)\approx x"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}+{x^5\over5!}"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}+{x^5\over5!}-{x^7\over7!}"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}+{x^5\over5!}-{x^7\over7!}+{x^9\over9!}"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}+{x^5\over5!}-{x^7\over7!}+{x^9\over9!}-{x^{11}\over11!}"),
            MathTex(r"\sin(x)\approx x-{x^3\over3!}+{x^5\over5!}-{x^7\over7!}+{x^9\over9!}-{x^{11}\over11!}+{x^{13}\over13!}"),
            MathTex(r"\sin(x)=\sum_{n=0}^\infty{(-1)^n\cdot x^{2n+1}\over(2n+1)!}")
        ).scale(1.25).move_to(4.5*UP)

        self.play(Create(axes))
        self.play(Create(v[0]), Write(g[0]))
        self.play(Create(v[1]), ReplacementTransform(g[0], g[1]))
        self.wait(0.7)

        for i in range(1, len(v)-1):
            self.play(ReplacementTransform(v[i], v[i+1]), ReplacementTransform(g[i], g[i+1]))
            self.wait(0.7)

        self.play(FadeOut(VGroup(axes, v[-1], v[0])))
        self.play(g[8].animate.shift(-4.5*UP))
        self.play(Circumscribe(g[8]))
        self.play(FadeOut(g[8]))
