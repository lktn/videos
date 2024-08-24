from manim import *
import numpy as np
from mpmath import zeta
config.pixel_height = 1920
config.pixel_width = 1080
a = config.frame_width
class ComplexFunctionPlot(Scene):
    def construct(self):
        complex_plane = ComplexPlane(
            x_range=[-2.5, 5.5, 1], 
            y_range=[-64/9, 64/9, 1], 
            x_length=a,
            y_length=16*a/9
        ).add_coordinates(font_size=45)
        
        def func(t):
            return complex_plane.n2p(zeta(0.5 + 1j * t))
        
        graph = ParametricFunction(func, t_range=[0, 100]).set_stroke([YELLOW, BLUE])
        b = MathTex(r"\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}").move_to(UP*8).scale(1.7)
        
        self.add(complex_plane, b, graph)
        self.play(Create(graph, rate_func=linear, run_time=15))
        self.play(FadeOut(VGroup(b, function_graph, complex_plane, stroke_color=BLUE), run_time=1))
