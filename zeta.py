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
        
        def complex_function(z):
            return zeta(0.5 + 1j * z)
        
        def parametric_function(t):
            z = complex(t, 0)
            return complex_plane.n2p(complex_function(z))
        
        function_graph = ParametricFunction(parametric_function, t_range=[0, 100]).set_stroke([YELLOW, BLUE])
        b = MathTex(r"\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}").move_to(UP*8).scale(1.7)
        
        self.add(complex_plane, b)
        self.wait(1)
        self.play(Create(function_graph, rate_func=linear, run_time=15))
        self.wait(1)
        self.play(FadeOut(VGroup(b, function_graph, complex_plane, stroke_color=BLUE), run_time=1))
